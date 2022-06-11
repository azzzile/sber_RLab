import sys
import yaml
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl

from PySide6.QtWidgets import *
from PySide6.QtGui import *

from matplotlib.collections import PathCollection, LineCollection
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from ui.main_window import Ui_MainWindow
from ui.node_parametizer import Ui_NodeForm
from ui.edge_parametizer import Ui_EdgeForm

from graph_gen import generate

GREEN = (32, 162, 156)
DARK_GREY = (44, 55, 62)

# for common fonts in app
MAIN_FONT = QFont()
MAIN_FONT.setWeight(QFont.Bold)
TITLE_FONT = QFont()
TITLE_FONT.setWeight(QFont.DemiBold)
STANDART_FONT = QFont()

# colors for graph drawing, each node has two conditions: normal and picked
COLORS = {"normal": {"L": "#55efc4", "CS": "#ffeaa7", "A": "#74b9ff", "R": "#adef52", "E": "#ef8c69"},
          "picked": {"L": "#52D6AB", "CS": "#D7C38A", "A": "#6299D6", "R": "#8FCC54", "E": "#D57368"}}

# full node type name relationships with short type name
NODE_TYPE = {"A": "Aile", "CS": "Cross station", "L": "Lift", "R": "Recharge point", "E": "Enter point"}


class NodeParametizer(Ui_NodeForm, QWidget):
    """Special class for node parametizer block"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFonts()

    def setFonts(self):
        """Sets special font for each label"""
        t_labels = [self.t_label, self.t_label_2]

        for label in t_labels:
            label.setFont(TITLE_FONT)


class EdgeParametizer(Ui_EdgeForm, QWidget):
    """Class for edge parametizer block"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFonts()

    def setFonts(self):
        """Sets special font for each label"""
        t_labels = [self.t_label, self.t_label_2, self.t_label_3]

        for label in t_labels:
            label.setFont(TITLE_FONT)


class GraphGUI(QMainWindow, Ui_MainWindow):
    """Main class for app"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setFonts()
        self.setParametizersAndCanvas()
        self.connect_buttons()

        self.cur_config = None  # current config.yaml file, None when no file selected
        self.cur_graphml = None  # current .graphml file, None when no file selected
        self.prev_ind = None  # previous index for chosen node for graph drawing

        self.cur_params = 0  # current parametizer block in use, 0 if none selected, 1 if node selected, 2 if edge selected

    def setParametizersAndCanvas(self):
        """Sets canvas and empty parametizer when the app starts"""
        self.setEmptyParametizer()

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout.addWidget(self.canvas, 3, 0, 6, 7)

        self.toolbar = NavigationToolbar(self.canvas, self)
        self.gridLayout.addWidget(self.toolbar, 9, 0, 1, 5)

    def setFonts(self):
        """Sets special font for each label"""
        m_labels = [self.m_label, self.m_label_2, ]
        t_labels = [self.t_label, self.t_label_2, self.t_label_3, self.t_label_4, self.t_label_5,
                    self.t_label_6, self.t_label_7, self.t_label_8, self.t_label_9]
        s_labels = [self.label, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7,
                    self.label_8, self.label_9, self.label_10, self.label_11, self.label_12, self.label_13]

        for label in m_labels:
            label.setFont(MAIN_FONT)
        for label in t_labels:
            label.setFont(TITLE_FONT)
        for label in s_labels:
            label.setFont(STANDART_FONT)

    def connect_buttons(self):
        """Adds actions to buttons"""
        self.button_loadConf.clicked.connect(self.load_config)
        self.button_saveConf.clicked.connect(self.save_config)
        self.button_exit.clicked.connect(self.close)
        self.button_displayBase.clicked.connect(self.display_base)
        self.button_saveParams.clicked.connect(self.save_params)

    def load_config(self):
        """Loads selected .yaml file"""
        filename, filter = QFileDialog.getOpenFileName(
            parent=self, caption='Open config file',
            dir='.', filter='*.yaml')
        self.cur_config = filename
        self.load_config_data()

        self.statusBar.showMessage(f"{filename} was loaded", 5000)

    def load_config_data(self):
        """Loads all data from current config to configurator block"""
        with open(self.cur_config) as f:
            storage = yaml.safe_load(f)
        module = storage["modules"][0]
        # name
        self.name_lineEdit.setText(module["name"])
        # floor
        floor = module["floor"]
        self.floorCount_spinBox.setValue(floor["count"])
        self.floorWeight_spinBox.setValue(floor["weight"])
        # cross
        cross = module["cross"]
        self.crossCount_spinBox.setValue(cross["count"])
        self.crossWeight_SpinBox.setValue(cross["weight"])
        # lift
        lift = module["lift"]
        self.liftCSLink_lineEdit.setText(",".join(map(str, lift["cs_link"])))
        self.liftWeight_spinBox.setValue(lift["weight"])
        # rack
        rack = module["rack"]
        self.rackCSLink_lineEdit.setText(",".join(map(str, rack["cs_link"])))
        self.rackWeight_spinBox.setValue(rack["weight"])
        # section
        section = module["section"]
        self.sectionCount_spinBox.setValue(section["count"])
        self.sectionCellsPerSection_spinBox.setValue(section["cells_per_section"])
        self.sectionGap_spinBox.setValue(section["section_gap"])
        # cell
        self.cellWeight_spinBox.setValue(module["cell"]["weight"])
        # recharge
        recharge = module["recharge_point"]
        self.rechargeCross_spinBox.setValue(recharge["cross"])
        self.reachargeFloor_spinBox.setValue(recharge["floor"])
        self.rechargeWeight_spinBox.setValue(recharge["weight"])
        # enter
        enter = module["enter_point"]
        self.enterCross_spinBox.setValue(enter["cross"])
        self.enterFloor_spinBox.setValue(enter["floor"])
        self.enterWeight_spinBox.setValue(enter["weight"])
        # product classes
        p_class = module["class"]
        self.classA_spinBox.setValue(p_class["A"])
        self.classB_spinBox.setValue(p_class["B"])

    def save_config(self):
        """Saves all data from configurator widgets to config file"""
        if self.cur_config is None:
            filename, filter = QFileDialog.getSaveFileName(
                parent=self, caption='Save config file',
                dir='.', filter='*.yaml *.yml')
            self.cur_config = filename
        with open(self.cur_config, 'w', encoding='utf8') as f:
            yaml.dump(self.get_config_data(), f, sort_keys=False)

        self.statusBar.showMessage(f"{self.cur_config} was saved", 5000)

    def get_config_data(self):
        """Returns all config data from widgets"""
        fields_dict = {"name": self.name_lineEdit.text(),
                       "floor": {"count": self.floorCount_spinBox.value(), "weight": self.floorWeight_spinBox.value()},
                       "cross": {"count": self.crossCount_spinBox.value(), "weight": self.crossWeight_SpinBox.value()},
                       "lift": {"cs_link": list(map(int, self.liftCSLink_lineEdit.text().split(","))),
                                "weight": self.liftWeight_spinBox.value()},
                       "rack": {"cs_link": list(map(int, self.rackCSLink_lineEdit.text().split(","))),
                                "weight": self.rackWeight_spinBox.value()},
                       "section": {"count": self.sectionCount_spinBox.value(),
                                   "cells_per_section": self.sectionCellsPerSection_spinBox.value(),
                                   "section_gap": self.sectionGap_spinBox.value()},
                       "cell": {"weight": self.cellWeight_spinBox.value()},
                       "recharge_point": {"floor": self.reachargeFloor_spinBox.value(),
                                          "cross": self.rechargeCross_spinBox.value(),
                                          "weight": self.rechargeWeight_spinBox.value()},
                       "enter_point": {"floor": self.enterFloor_spinBox.value(),
                                       "cross": self.enterCross_spinBox.value(),
                                       "weight": self.enterWeight_spinBox.value()},
                       "class": {"A": self.classA_spinBox.value(), "B": self.classB_spinBox.value()}}
        storage = {"modules": [fields_dict]}
        return storage

    def display_base(self):
        """Makes xml and displays it to canvas
        Saves config data from widgets if a new file was created
        if at least on field is empty offers to open already existing file"""
        # [['id', 'cont_id', 'empty', 'class_type', 'floor', 'rack', 'cell', 'side'],
        # ['1_A_1_1_1_L', None, True, 'A', 1, 1, 1, 'L'],...]
        try:
            data = self.get_config_data()
            graph, db_predata, graph_path, db_predata_path = generate(data)
            self.cur_graphml = graph_path
            self.save_config()
            cur_floor = self.curFloor_spinBox.value()
            self.vis_graph(cur_floor, graph)
            self.statusBar.showMessage("temp files (xml and csv) were created", 5000)
        except Exception as e:
            self.statusBar.showMessage(f"{e.__class__.__name__} error occured! check the entered data for correctness", 5000)

    def vis_graph(self, cur_floor, G):
        self.figure.clf()
        ax = self.figure.add_subplot(111)
        ax.axis('off')

        with open(self.cur_config) as f:
            storage = yaml.safe_load(f)

        modules = storage["modules"]

        pos = {}
        nodes = G.nodes()

        base_gap_x = 20
        base_gap_y = 30
        scale = 10

        self.COLOR_MAP = []
        cur_nodes = []

        for node in nodes:
            module_id, typo, floor, rack, cell = map(lambda i: int(i) if i.isdigit() else i, node.split("_"))
            if floor == cur_floor or typo == "L":
                cur_nodes.append(node)

        cur_floor_G = G.subgraph(cur_nodes).to_undirected()

        for node in cur_floor_G.nodes():
            module_id, typo, floor, rack, cell = map(lambda i: int(i) if i.isdigit() else i, node.split("_"))
            if typo == "L":
                pos[node] = [
                    # x
                    base_gap_x * max(modules[module_id - 1]["cross"]["count"],
                                     len(modules[module_id - 1]["rack"]["cs_link"])) // len(
                        modules[module_id - 1]["lift"]["cs_link"]) + base_gap_x * rack,
                    # y
                    -base_gap_y * scale * modules[module_id - 1]["lift"]["weight"]
                ]

            elif typo == "CS":
                pos[node] = [
                    base_gap_x * max(modules[module_id - 1]["cross"]["count"],
                                     len(modules[module_id - 1]["rack"]["cs_link"])) // len(
                        modules[module_id - 1]["lift"]["cs_link"]) + base_gap_x * rack,
                    10
                ]

            elif typo == "A":
                pos[node] = [
                    base_gap_x * max(modules[module_id - 1]["cross"]["count"],
                                     len(modules[module_id - 1]["rack"]["cs_link"])) // len(
                        modules[module_id - 1]["lift"]["cs_link"]) + base_gap_x * rack,
                    base_gap_y * scale * cell
                ]
            elif typo == "R":
                pos[node] = [
                    # x
                    base_gap_x * max(modules[module_id - 1]["cross"]["count"],
                                     len(modules[module_id - 1]["rack"]["cs_link"])) // len(
                        modules[module_id - 1]["lift"]["cs_link"]) + base_gap_x * rack,
                    # y
                    -base_gap_y * scale * modules[module_id - 1]["lift"]["weight"]
                ]

            elif typo == "E":
                pos[node] = [
                    # x
                    base_gap_x * max(modules[module_id - 1]["cross"]["count"],
                                     len(modules[module_id - 1]["rack"]["cs_link"])) // len(
                        modules[module_id - 1]["lift"]["cs_link"]) + base_gap_x * rack,
                    # y
                    -base_gap_y * scale * modules[module_id - 1]["lift"]["weight"]
                ]
            self.COLOR_MAP.append(COLORS["normal"][typo])

        # draw graph
        # plt.gca().set_axis_off()
        nodes = nx.draw_networkx_nodes(cur_floor_G, pos, node_color=self.COLOR_MAP, label=1, node_size=500)

        nodes.set_picker(5)

        nx.draw_networkx_labels(cur_floor_G, pos, font_size=5)
        edges = nx.draw_networkx_edges(cur_floor_G, pos, width=1)

        edges.set_picker(5)

        nx.draw_networkx_edge_labels(cur_floor_G, pos, edge_labels=nx.get_edge_attributes(cur_floor_G, 'weight'),
                                     font_size=5)
        # artist = plot_network(cur_floor_G, pos=pos, node_style=use_attributes(), edge_style=use_attributes())
        # print(artist)
        # artist.set_picker(10)

        self.pos = pos
        # Bind our onpick() function to pick events:
        self.canvas.mpl_connect('pick_event', self.onpick)
        self.canvas.draw_idle()

    def onpick(self, event):
        if isinstance(event.artist, PathCollection):
            self.nodeChosedEvent(event)
        elif isinstance(event.artist, LineCollection):
            self.edgeChosedEvent(event)

    def save_params(self):
        if self.cur_params == 0:
            return
        elif self.cur_params == 1:
            db_predata_path = 'output/temp_db_predata.csv'
            df = pd.read_csv(db_predata_path, header=0)
            name = self.nodeBlock.nodeName_label.text()
            r = self.nodeBlock.rightSide_checkBox.isChecked()
            l = self.nodeBlock.leftSide_checkBox.isChecked()
            availability = self.nodeBlock.availability_checkBox.isChecked()
            #print(df.head())
        else:
            pass  # надо прописать для ребер

    def setEmptyParametizer(self):
        self.emptyParametizer_label = QLabel("Nothing selected")
        self.emptyParametizer_label.setFont(TITLE_FONT)
        self.emptyParametizer_label.setMargin(25)
        self.emptyParametizer_label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)

        self.gridLayout.addWidget(self.emptyParametizer_label, 7, 8, 1, 2)

    def change_params(self, status):
        """Changes parametizer block from one condition to another"""
        # removing of current parametizer
        if self.cur_params == 0:
            self.gridLayout.removeWidget(self.emptyParametizer_label)
            self.emptyParametizer_label.deleteLater()
        else:
            layout = self.nodeBlock.gridLayout if self.cur_params == 1 else self.edgeBlock.gridLayout
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                widget.deleteLater()
        # setting new block depending on wanted condition
        if status == 1:
            self.nodeBlock = NodeParametizer()
            self.nodeBlock.setupUi(self.nodeBlock)
            self.gridLayout.addLayout(self.nodeBlock.gridLayout, 7, 8, 1, 2)
        elif status == 0:
            self.setEmptyParametizer()
        else:
            self.edgeBlock = EdgeParametizer()
            self.edgeBlock.setupUi(self.edgeBlock)
            self.gridLayout.addLayout(self.edgeBlock.gridLayout, 7, 8, 1, 2)
        self.cur_params = status

    def nodeChosedEvent(self, event):
        """Displays Node Parametizer Widget"""
        all_nodes = event.artist
        ind = event.ind[0]  # event.ind is a single element array.
        nodes = list(self.pos.keys())
        this_node_name = nodes[ind]
        type = this_node_name.split("_")[1]

        # Set the colours for all the nodes, highlighting the picked node with
        # a different colour:

        self.COLOR_MAP[ind] = COLORS['picked'][type]
        if self.prev_ind is not None:
            self.COLOR_MAP[self.prev_ind] = COLORS["normal"][nodes[self.prev_ind].split("_")[1]]

        all_nodes.set_facecolors(self.COLOR_MAP)
        # Update the plot to show the change:
        self.canvas.draw_idle()
        self.prev_ind = ind

        if self.cur_params != 1:
            self.change_params(1)

        self.nodeBlock.nodeName_label.setText(this_node_name)
        self.nodeBlock.nodeType_label.setText(NODE_TYPE[type])

        db_predata_path = 'output/temp_db_predata.csv'
        df = pd.read_csv(db_predata_path, header=0)
        #cur_node_L = df[df.id == this_node_name+"_L"]
        #cur_node_R = df[df.id == this_node_name+"_R"]

        #self.nodeBlock.rightSide_checkBox.setChecked()
        #l = self.nodeBlock.leftSide_checkBox.isChecked()

        self.nodeBlock.availability_checkBox.setChecked(True)
        self.nodeBlock.rightSide_checkBox.setChecked(True)
        self.nodeBlock.leftSide_checkBox.setChecked(True)

    def edgeChosedEvent(self, event):
        """Displays Edge Parametizer Widget"""
        all_edges = event.artist
        ind = event.ind[0]
        #edges = list(self)

        # тут надо дописать все для ребер, но я не нашла (пока) изменение толщины линии отдельного ребра, я доделаю после

        if self.cur_params != 2:
            self.change_params(2)

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, "Message",
            "Are you sure you want to quit? Any unsaved work will be lost.",
            QMessageBox.Save | QMessageBox.Close | QMessageBox.Cancel,
            QMessageBox.Save)

        if reply == QMessageBox.Close:
            app.quit()
        elif reply == QMessageBox.Save:
            pass
        else:
            event.ignore()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GraphGUI()
    gui.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())