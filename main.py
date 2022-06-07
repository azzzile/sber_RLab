import sys
import yaml
import csv
import os
import networkx as nx
import matplotlib.pyplot as plt

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from ui.main_window import Ui_MainWindow
from ui.node_parametizer import Ui_NodeForm
from ui.edge_parametizer import Ui_EdgeForm

from graph_gen import generate
from lizkins import draw_graph


GREEN = (32, 162, 156)
DARK_GREY = (44, 55, 62)

MAIN_FONT = QFont()
MAIN_FONT.setWeight(QFont.Bold)
TITLE_FONT = QFont()
TITLE_FONT.setWeight(QFont.DemiBold)
STANDART_FONT = QFont()


class NodeParametizer(Ui_NodeForm, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setFonts(self):
        """Sets special font for each label"""
        t_labels = [self.label, self.t_label_2]

        for label in t_labels:
            label.setFont(TITLE_FONT)


class EdgeParametizer(Ui_EdgeForm, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setFonts(self):
        """Sets special font for each label"""
        t_labels = [self.t_label, self.t_label_2, self.t_label_3]

        for label in t_labels:
            label.setFont(TITLE_FONT)




class GraphGUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setFonts()
        self.setParametizers()
        self.setCanvas()
        self.connect_buttons()


        self.cur_config = None    # current config.yaml file, None when no file selected   поле под вопросом
        # можно через generate baseline создавать временный файл, хранящий все параметры конфига до его сохранения
        # возможно нужно сделать файлик по умолчанию в котором можно хранить настройки и после сохранить, типо новый создать ???

        self.cur_params = 0 # 0 if none selected, 1 if node selected, 2 if edge selected


    def setParametizers(self):
        self.emptyParametizer_label = QLabel("Nothing selected")
        self.emptyParametizer_label.setFont(TITLE_FONT)
        self.emptyParametizer_label.setMargin(25)
        self.emptyParametizer_label.setAlignment(Qt.AlignVCenter|Qt.AlignLeft)
        self.gridLayout.addWidget(self.emptyParametizer_label, 7, 8, 1, 2)

    def setCanvas(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout.addWidget(self.canvas, 3, 0, 6, 7)

    def plot(self, data):
        self.figure.clf()
        draw_graph(data)

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
        """Adds actions to all buttons"""
        self.button_loadConf.clicked.connect(self.load_config)
        self.button_saveConf.clicked.connect(self.save_config)
        self.button_exit.clicked.connect(self.close)
        self.button_displayBase.clicked.connect(self.display_base)
        #self.button_saveGraph.clicked.connect(self.nodeChosedEvent)

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
        """Loads all data from current config to configurator block"""
        filename, filter = QFileDialog.getSaveFileName(
            parent=self, caption='Save config file',
            dir='.', filter='*.yaml *.yml')
        with open(filename, 'w', encoding='utf8') as f:
            yaml.dump(self.get_config_data(), f, sort_keys=False)
        self.statusBar.showMessage(f"{self.cur_config} was saved", 5000)

    def get_config_data(self):
        """Returns all config data from widgets"""
        fields_dict = {"name": self.name_lineEdit.text(),
                       "floor": {"count": self.floorCount_spinBox.value(), "weight": self.floorWeight_spinBox.value()},
                       "cross": {"count": self.crossCount_spinBox.value(), "weight": self.crossWeight_SpinBox.value()},
                       "lift": {"cs_link": list(map(int, self.liftCSLink_lineEdit.text().split(","))), "weight": self.liftWeight_spinBox.value()},
                       "rack": {"cs_link": list(map(int, self.rackCSLink_lineEdit.text().split(","))), "weight": self.rackWeight_spinBox.value()},
                       "section": {"count": self.sectionCount_spinBox.value(), "cells_per_section": self.sectionCellsPerSection_spinBox.value(), "section_gap": self.sectionGap_spinBox.value()},
                       "cell": {"weight": self.cellWeight_spinBox.value()},
                       "recharge_point": {"floor": self.reachargeFloor_spinBox.value(), "cross": self.rechargeCross_spinBox.value(), "weight": self.rechargeWeight_spinBox.value()},
                       "enter_point": {"floor": self.enterFloor_spinBox.value(), "cross": self.enterCross_spinBox.value(), "weight": self.enterWeight_spinBox.value()},
                       "class": {"A": self.classA_spinBox.value(), "B": self.classB_spinBox.value()}}
        storage = {"modules": [fields_dict]}
        return storage

    def display_base(self):
        """Makes xml and displays it to canvas"""
        if self.cur_config is None:
            self.load_config()
        graph, db_predata = generate(self.get_config_data()) # [['id', 'cont_id', 'empty', 'class_type', 'floor', 'rack', 'cell', 'side'], ['1_A_1_1_1_L', None, True, 'A', 1, 1, 1, 'L'],...]
        self.plot(db_predata[1:])

        self.statusBar.showMessage(f"temp files (xml and csv) were created", 5000)

    def nodeChosedEvent(self):
        """Displays Node Parametizer Widget"""
        self.nodeBlock = NodeParametizer()
        self.nodeBlock.setupUi(self)
        self.gridLayout.addLayout(self.nodeBlock.gridLayout, 7, 8, 1, 2)

    def edgeChosedEvent(self):
        """Displays Edge Parametizer Widget"""
        self.edgeBlock = EdgeParametizer()
        self.edgeBlock.setupUi(self)
        self.gridLayout.addLayout(self.edgeBlock.gridLayout, 7, 8, 1, 2)

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