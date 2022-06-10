from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1127, 786)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(7)
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 4, 8, 1, 2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(8)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.liftCSLink_lineEdit = QLineEdit(self.centralwidget)
        self.liftCSLink_lineEdit.setObjectName(u"liftCSLink_lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liftCSLink_lineEdit.sizePolicy().hasHeightForWidth())
        self.liftCSLink_lineEdit.setSizePolicy(sizePolicy)
        self.liftCSLink_lineEdit.setDragEnabled(False)

        self.gridLayout_5.addWidget(self.liftCSLink_lineEdit, 6, 1, 1, 1)

        self.sectionGap_spinBox = QDoubleSpinBox(self.centralwidget)
        self.sectionGap_spinBox.setObjectName(u"sectionGap_spinBox")
        self.sectionGap_spinBox.setDecimals(3)

        self.gridLayout_5.addWidget(self.sectionGap_spinBox, 9, 3, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 2, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 5, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)

        self.classA_spinBox = QSpinBox(self.centralwidget)
        self.classA_spinBox.setObjectName(u"classA_spinBox")
        self.classA_spinBox.setMaximum(999)

        self.horizontalLayout.addWidget(self.classA_spinBox)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.classB_spinBox = QSpinBox(self.centralwidget)
        self.classB_spinBox.setObjectName(u"classB_spinBox")
        self.classB_spinBox.setMaximum(999)

        self.horizontalLayout_2.addWidget(self.classB_spinBox)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_7.addLayout(self.horizontalLayout)


        self.gridLayout_5.addLayout(self.horizontalLayout_7, 15, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 10, 1, 1, 1)

        self.rackCSLink_lineEdit = QLineEdit(self.centralwidget)
        self.rackCSLink_lineEdit.setObjectName(u"rackCSLink_lineEdit")
        sizePolicy.setHeightForWidth(self.rackCSLink_lineEdit.sizePolicy().hasHeightForWidth())
        self.rackCSLink_lineEdit.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.rackCSLink_lineEdit, 7, 1, 1, 1)

        self.cellWeight_spinBox = QDoubleSpinBox(self.centralwidget)
        self.cellWeight_spinBox.setObjectName(u"cellWeight_spinBox")
        sizePolicy.setHeightForWidth(self.cellWeight_spinBox.sizePolicy().hasHeightForWidth())
        self.cellWeight_spinBox.setSizePolicy(sizePolicy)
        self.cellWeight_spinBox.setDecimals(3)

        self.gridLayout_5.addWidget(self.cellWeight_spinBox, 11, 1, 1, 1)

        self.t_label_3 = QLabel(self.centralwidget)
        self.t_label_3.setObjectName(u"t_label_3")

        self.gridLayout_5.addWidget(self.t_label_3, 6, 0, 1, 1)

        self.t_label_2 = QLabel(self.centralwidget)
        self.t_label_2.setObjectName(u"t_label_2")

        self.gridLayout_5.addWidget(self.t_label_2, 4, 0, 1, 1)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 5, 2, 1, 1)

        self.t_label = QLabel(self.centralwidget)
        self.t_label.setObjectName(u"t_label")

        self.gridLayout_5.addWidget(self.t_label, 3, 0, 1, 1)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 8, 2, 1, 1)

        self.liftWeight_spinBox = QDoubleSpinBox(self.centralwidget)
        self.liftWeight_spinBox.setObjectName(u"liftWeight_spinBox")
        sizePolicy.setHeightForWidth(self.liftWeight_spinBox.sizePolicy().hasHeightForWidth())
        self.liftWeight_spinBox.setSizePolicy(sizePolicy)
        self.liftWeight_spinBox.setDecimals(3)

        self.gridLayout_5.addWidget(self.liftWeight_spinBox, 6, 2, 1, 1)

        self.t_label_8 = QLabel(self.centralwidget)
        self.t_label_8.setObjectName(u"t_label_8")

        self.gridLayout_5.addWidget(self.t_label_8, 14, 0, 1, 1)

        self.sectionCellsPerSection_spinBox = QSpinBox(self.centralwidget)
        self.sectionCellsPerSection_spinBox.setObjectName(u"sectionCellsPerSection_spinBox")
        sizePolicy.setHeightForWidth(self.sectionCellsPerSection_spinBox.sizePolicy().hasHeightForWidth())
        self.sectionCellsPerSection_spinBox.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.sectionCellsPerSection_spinBox, 9, 2, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 8, 1, 1, 1)

        self.rackWeight_spinBox = QDoubleSpinBox(self.centralwidget)
        self.rackWeight_spinBox.setObjectName(u"rackWeight_spinBox")
        sizePolicy.setHeightForWidth(self.rackWeight_spinBox.sizePolicy().hasHeightForWidth())
        self.rackWeight_spinBox.setSizePolicy(sizePolicy)
        self.rackWeight_spinBox.setDecimals(3)

        self.gridLayout_5.addWidget(self.rackWeight_spinBox, 7, 2, 1, 1)

        self.crossCount_spinBox = QSpinBox(self.centralwidget)
        self.crossCount_spinBox.setObjectName(u"crossCount_spinBox")
        sizePolicy.setHeightForWidth(self.crossCount_spinBox.sizePolicy().hasHeightForWidth())
        self.crossCount_spinBox.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.crossCount_spinBox, 4, 1, 1, 1)

        self.t_label_4 = QLabel(self.centralwidget)
        self.t_label_4.setObjectName(u"t_label_4")

        self.gridLayout_5.addWidget(self.t_label_4, 7, 0, 1, 1)

        self.name_lineEdit = QLineEdit(self.centralwidget)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setEnabled(True)
        sizePolicy.setHeightForWidth(self.name_lineEdit.sizePolicy().hasHeightForWidth())
        self.name_lineEdit.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.name_lineEdit, 1, 1, 1, 2)

        self.floorWeight_spinBox = QDoubleSpinBox(self.centralwidget)
        self.floorWeight_spinBox.setObjectName(u"floorWeight_spinBox")
        sizePolicy.setHeightForWidth(self.floorWeight_spinBox.sizePolicy().hasHeightForWidth())
        self.floorWeight_spinBox.setSizePolicy(sizePolicy)
        self.floorWeight_spinBox.setDecimals(3)

        self.gridLayout_5.addWidget(self.floorWeight_spinBox, 3, 2, 1, 1)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 8, 3, 1, 1)

        self.floorCount_spinBox = QSpinBox(self.centralwidget)
        self.floorCount_spinBox.setObjectName(u"floorCount_spinBox")
        sizePolicy.setHeightForWidth(self.floorCount_spinBox.sizePolicy().hasHeightForWidth())
        self.floorCount_spinBox.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.floorCount_spinBox, 3, 1, 1, 1)

        self.t_label_6 = QLabel(self.centralwidget)
        self.t_label_6.setObjectName(u"t_label_6")

        self.gridLayout_5.addWidget(self.t_label_6, 11, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 2, 2, 1, 1)

        self.t_label_5 = QLabel(self.centralwidget)
        self.t_label_5.setObjectName(u"t_label_5")

        self.gridLayout_5.addWidget(self.t_label_5, 9, 0, 1, 1)

        self.crossWeight_SpinBox = QDoubleSpinBox(self.centralwidget)
        self.crossWeight_SpinBox.setObjectName(u"crossWeight_SpinBox")
        sizePolicy.setHeightForWidth(self.crossWeight_SpinBox.sizePolicy().hasHeightForWidth())
        self.crossWeight_SpinBox.setSizePolicy(sizePolicy)
        self.crossWeight_SpinBox.setDecimals(3)

        self.gridLayout_5.addWidget(self.crossWeight_SpinBox, 4, 2, 1, 1)

        self.f_label = QLabel(self.centralwidget)
        self.f_label.setObjectName(u"f_label")

        self.gridLayout_5.addWidget(self.f_label, 1, 0, 1, 1)

        self.sectionCount_spinBox = QSpinBox(self.centralwidget)
        self.sectionCount_spinBox.setObjectName(u"sectionCount_spinBox")
        sizePolicy.setHeightForWidth(self.sectionCount_spinBox.sizePolicy().hasHeightForWidth())
        self.sectionCount_spinBox.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.sectionCount_spinBox, 9, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.reachargeFloor_spinBox = QSpinBox(self.centralwidget)
        self.reachargeFloor_spinBox.setObjectName(u"reachargeFloor_spinBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.reachargeFloor_spinBox.sizePolicy().hasHeightForWidth())
        self.reachargeFloor_spinBox.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.reachargeFloor_spinBox)

        self.enterFloor_spinBox = QSpinBox(self.centralwidget)
        self.enterFloor_spinBox.setObjectName(u"enterFloor_spinBox")
        sizePolicy1.setHeightForWidth(self.enterFloor_spinBox.sizePolicy().hasHeightForWidth())
        self.enterFloor_spinBox.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.enterFloor_spinBox)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.rechargeCross_spinBox = QSpinBox(self.centralwidget)
        self.rechargeCross_spinBox.setObjectName(u"rechargeCross_spinBox")
        sizePolicy1.setHeightForWidth(self.rechargeCross_spinBox.sizePolicy().hasHeightForWidth())
        self.rechargeCross_spinBox.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.rechargeCross_spinBox)

        self.enterCross_spinBox = QSpinBox(self.centralwidget)
        self.enterCross_spinBox.setObjectName(u"enterCross_spinBox")
        sizePolicy1.setHeightForWidth(self.enterCross_spinBox.sizePolicy().hasHeightForWidth())
        self.enterCross_spinBox.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.enterCross_spinBox)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.rechargeWeight_spinBox = QDoubleSpinBox(self.centralwidget)
        self.rechargeWeight_spinBox.setObjectName(u"rechargeWeight_spinBox")
        self.rechargeWeight_spinBox.setDecimals(3)

        self.verticalLayout_4.addWidget(self.rechargeWeight_spinBox)

        self.enterWeight_spinBox = QDoubleSpinBox(self.centralwidget)
        self.enterWeight_spinBox.setObjectName(u"enterWeight_spinBox")
        self.enterWeight_spinBox.setDecimals(3)

        self.verticalLayout_4.addWidget(self.enterWeight_spinBox)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)


        self.gridLayout_5.addLayout(self.horizontalLayout_5, 12, 1, 3, 2)

        self.t_label_7 = QLabel(self.centralwidget)
        self.t_label_7.setObjectName(u"t_label_7")

        self.gridLayout_5.addWidget(self.t_label_7, 13, 0, 1, 1)

        self.t_label_9 = QLabel(self.centralwidget)
        self.t_label_9.setObjectName(u"t_label_9")

        self.gridLayout_5.addWidget(self.t_label_9, 15, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_5, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_4, 3, 8, 1, 2)

        self.button_displayBase = QPushButton(self.centralwidget)
        self.button_displayBase.setObjectName(u"button_displayBase")
        sizePolicy.setHeightForWidth(self.button_displayBase.sizePolicy().hasHeightForWidth())
        self.button_displayBase.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.button_displayBase, 1, 9, 1, 1, Qt.AlignRight)

        self.curFloor_spinBox = QSpinBox(self.centralwidget)
        self.curFloor_spinBox.setObjectName(u"curFloor_spinBox")
        self.curFloor_spinBox.setMinimum(1)
        self.curFloor_spinBox.setMaximum(999)

        self.gridLayout.addWidget(self.curFloor_spinBox, 1, 4, 1, 1)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 1, 3, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.button_lockFloor = QPushButton(self.centralwidget)
        self.button_lockFloor.setObjectName(u"button_lockFloor")
        self.button_lockFloor.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button_lockFloor.sizePolicy().hasHeightForWidth())
        self.button_lockFloor.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"ui/unlock.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"ui/block.png", QSize(), QIcon.Normal, QIcon.On)
        self.button_lockFloor.setIcon(icon)
        self.button_lockFloor.setCheckable(True)
        self.button_lockFloor.setChecked(True)
        self.button_lockFloor.setAutoDefault(False)
        self.button_lockFloor.setFlat(False)

        self.horizontalLayout_6.addWidget(self.button_lockFloor, 0, Qt.AlignRight)

        self.button_saveParams = QPushButton(self.centralwidget)
        self.button_saveParams.setObjectName(u"button_saveParams")
        sizePolicy.setHeightForWidth(self.button_saveParams.sizePolicy().hasHeightForWidth())
        self.button_saveParams.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.button_saveParams, 0, Qt.AlignRight)


        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 9, 1, 1)

        self.button_saveGraph = QPushButton(self.centralwidget)
        self.button_saveGraph.setObjectName(u"button_saveGraph")

        self.gridLayout.addWidget(self.button_saveGraph, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 5, 1, 1)

        self.button_saveConf = QPushButton(self.centralwidget)
        self.button_saveConf.setObjectName(u"button_saveConf")

        self.gridLayout.addWidget(self.button_saveConf, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_2, 8, 8, 1, 1)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_5, 6, 8, 1, 2)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 2, 8, 1, 2)

        self.button_loadConf = QPushButton(self.centralwidget)
        self.button_loadConf.setObjectName(u"button_loadConf")

        self.gridLayout.addWidget(self.button_loadConf, 1, 0, 1, 1)

        self.m_label_2 = QLabel(self.centralwidget)
        self.m_label_2.setObjectName(u"m_label_2")

        self.gridLayout.addWidget(self.m_label_2, 5, 8, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 7, 8, 1)

        self.m_label = QLabel(self.centralwidget)
        self.m_label.setObjectName(u"m_label")

        self.gridLayout.addWidget(self.m_label, 1, 8, 1, 1)

        self.button_exit = QPushButton(self.centralwidget)
        self.button_exit.setObjectName(u"button_exit")

        self.gridLayout.addWidget(self.button_exit, 1, 6, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 3, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.button_lockFloor.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GraphGUI", None))
        self.liftCSLink_lineEdit.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"count:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"cs_link:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"A:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"B:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"weight:", None))
        self.t_label_3.setText(QCoreApplication.translate("MainWindow", u"Lift:", None))
        self.t_label_2.setText(QCoreApplication.translate("MainWindow", u"Cross:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"weight:", None))
        self.t_label.setText(QCoreApplication.translate("MainWindow", u"Floor:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"cells_per_section:", None))
        self.t_label_8.setText(QCoreApplication.translate("MainWindow", u"Enter:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"count:", None))
        self.t_label_4.setText(QCoreApplication.translate("MainWindow", u"Rack:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"section_gap:", None))
        self.t_label_6.setText(QCoreApplication.translate("MainWindow", u"Cell:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"weight:", None))
        self.t_label_5.setText(QCoreApplication.translate("MainWindow", u"Section:", None))
        self.f_label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"floor:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"cross:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"weight:", None))
        self.t_label_7.setText(QCoreApplication.translate("MainWindow", u"Recharge:", None))
        self.t_label_9.setText(QCoreApplication.translate("MainWindow", u"Class:", None))
        self.button_displayBase.setText(QCoreApplication.translate("MainWindow", u"Display Baseline", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Current floor:", None))
        self.button_lockFloor.setText("")
        self.button_saveParams.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.button_saveGraph.setText(QCoreApplication.translate("MainWindow", u"Save .graphml", None))
        self.button_saveConf.setText(QCoreApplication.translate("MainWindow", u"Save Config", None))
        self.button_loadConf.setText(QCoreApplication.translate("MainWindow", u"Load Config", None))
        self.m_label_2.setText(QCoreApplication.translate("MainWindow", u"Parametizer", None))
        self.m_label.setText(QCoreApplication.translate("MainWindow", u"Configurator", None))
        self.button_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi



