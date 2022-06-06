from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(286, 300)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(8)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.edgeName_label = QLabel(Form)
        self.edgeName_label.setObjectName(u"edgeName_label")
        self.edgeName_label.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edgeName_label.sizePolicy().hasHeightForWidth())
        self.edgeName_label.setSizePolicy(sizePolicy)
        self.edgeName_label.setFocusPolicy(Qt.NoFocus)
        self.edgeName_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.edgeName_label, 0, 1, 1, 1)

        self.edgeType_label = QLabel(Form)
        self.edgeType_label.setObjectName(u"edgeType_label")
        sizePolicy.setHeightForWidth(self.edgeType_label.sizePolicy().hasHeightForWidth())
        self.edgeType_label.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.edgeType_label, 1, 1, 1, 1)

        self.weight_spinBox = QDoubleSpinBox(Form)
        self.weight_spinBox.setObjectName(u"weight_spinBox")
        self.weight_spinBox.setDecimals(3)

        self.gridLayout_2.addWidget(self.weight_spinBox, 2, 1, 1, 1)

        self.t_label = QLabel(Form)
        self.t_label.setObjectName(u"t_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.t_label.sizePolicy().hasHeightForWidth())
        self.t_label.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.t_label, 0, 0, 1, 1)

        self.t_label_2 = QLabel(Form)
        self.t_label_2.setObjectName(u"t_label_2")
        sizePolicy1.setHeightForWidth(self.t_label_2.sizePolicy().hasHeightForWidth())
        self.t_label_2.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.t_label_2, 1, 0, 1, 1)

        self.t_label_3 = QLabel(Form)
        self.t_label_3.setObjectName(u"t_label_3")
        sizePolicy1.setHeightForWidth(self.t_label_3.sizePolicy().hasHeightForWidth())
        self.t_label_3.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.t_label_3, 2, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.edgeName_label.setText(QCoreApplication.translate("Form", u"edge_name", None))
        self.edgeType_label.setText(QCoreApplication.translate("Form", u"edge_type", None))
        self.t_label.setText(QCoreApplication.translate("Form", u"Edge name:", None))
        self.t_label_2.setText(QCoreApplication.translate("Form", u"Type:", None))
        self.t_label_3.setText(QCoreApplication.translate("Form", u"Weight:", None))
    # retranslateUi

