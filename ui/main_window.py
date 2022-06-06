from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(739, 606)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_exit = QPushButton(self.centralwidget)
        self.pushButton_exit.setObjectName(u"pushButton_exit")

        self.gridLayout.addWidget(self.pushButton_exit, 0, 4, 1, 1)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 3, 6, 1, 2)

        self.pushButton_saveParams = QPushButton(self.centralwidget)
        self.pushButton_saveParams.setObjectName(u"pushButton_saveParams")

        self.gridLayout.addWidget(self.pushButton_saveParams, 4, 7, 1, 1)

        self.pushButton_geterateGraph = QPushButton(self.centralwidget)
        self.pushButton_geterateGraph.setObjectName(u"pushButton_geterateGraph")

        self.gridLayout.addWidget(self.pushButton_geterateGraph, 0, 2, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 506, 535))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout.addWidget(self.scrollArea, 2, 0, 5, 5)

        self.pushButton_loadConf = QPushButton(self.centralwidget)
        self.pushButton_loadConf.setObjectName(u"pushButton_loadConf")

        self.gridLayout.addWidget(self.pushButton_loadConf, 0, 0, 1, 1)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 4, 6, 1, 1)

        self.pushButton_saveConf = QPushButton(self.centralwidget)
        self.pushButton_saveConf.setObjectName(u"pushButton_saveConf")

        self.gridLayout.addWidget(self.pushButton_saveConf, 0, 1, 1, 1)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 1, 6, 1, 2)

        self.pushButton_generateBase = QPushButton(self.centralwidget)
        self.pushButton_generateBase.setObjectName(u"pushButton_generateBase")

        self.gridLayout.addWidget(self.pushButton_generateBase, 0, 7, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_ = QLabel(self.centralwidget)
        self.label_.setObjectName(u"label_")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_)

        self.spinBox_modules = QSpinBox(self.centralwidget)
        self.spinBox_modules.setObjectName(u"spinBox_modules")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_modules.sizePolicy().hasHeightForWidth())
        self.spinBox_modules.setSizePolicy(sizePolicy)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.spinBox_modules)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.spinBox_floors = QSpinBox(self.centralwidget)
        self.spinBox_floors.setObjectName(u"spinBox_floors")
        sizePolicy.setHeightForWidth(self.spinBox_floors.sizePolicy().hasHeightForWidth())
        self.spinBox_floors.setSizePolicy(sizePolicy)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.spinBox_floors)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.spinBox_cross = QSpinBox(self.centralwidget)
        self.spinBox_cross.setObjectName(u"spinBox_cross")
        sizePolicy.setHeightForWidth(self.spinBox_cross.sizePolicy().hasHeightForWidth())
        self.spinBox_cross.setSizePolicy(sizePolicy)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.spinBox_cross)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.spinBox_racks = QSpinBox(self.centralwidget)
        self.spinBox_racks.setObjectName(u"spinBox_racks")
        sizePolicy.setHeightForWidth(self.spinBox_racks.sizePolicy().hasHeightForWidth())
        self.spinBox_racks.setSizePolicy(sizePolicy)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.spinBox_racks)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.spinBox_cells = QSpinBox(self.centralwidget)
        self.spinBox_cells.setObjectName(u"spinBox_cells")
        sizePolicy.setHeightForWidth(self.spinBox_cells.sizePolicy().hasHeightForWidth())
        self.spinBox_cells.setSizePolicy(sizePolicy)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.spinBox_cells)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.spinBox_lifts = QSpinBox(self.centralwidget)
        self.spinBox_lifts.setObjectName(u"spinBox_lifts")
        sizePolicy.setHeightForWidth(self.spinBox_lifts.sizePolicy().hasHeightForWidth())
        self.spinBox_lifts.setSizePolicy(sizePolicy)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.spinBox_lifts)


        self.gridLayout.addLayout(self.formLayout_2, 2, 6, 1, 2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 5, 7, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 6, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 5)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_5, 5, 6, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 3, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GraphGUI", None))
        self.pushButton_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton_saveParams.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_geterateGraph.setText(QCoreApplication.translate("MainWindow", u"Generate .graphml", None))
        self.pushButton_loadConf.setText(QCoreApplication.translate("MainWindow", u"Load Config", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Parametizer", None))
        self.pushButton_saveConf.setText(QCoreApplication.translate("MainWindow", u"Save Config", None))
        self.pushButton_generateBase.setText(QCoreApplication.translate("MainWindow", u"Generate Baseline", None))
        self.label_.setText(QCoreApplication.translate("MainWindow", u"Modules", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Floors", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cross", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Racks", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cells", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Lifts", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Configurator", None))
    # retranslateUi

