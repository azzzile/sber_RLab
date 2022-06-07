from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_EdgeForm(object):
    def setupUi(self, EdgeForm):
        if not EdgeForm.objectName():
            EdgeForm.setObjectName(u"EdgeForm")
        EdgeForm.resize(280, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EdgeForm.sizePolicy().hasHeightForWidth())
        EdgeForm.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(EdgeForm)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.t_label_2 = QLabel(EdgeForm)
        self.t_label_2.setObjectName(u"t_label_2")
        sizePolicy.setHeightForWidth(self.t_label_2.sizePolicy().hasHeightForWidth())
        self.t_label_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.t_label_2, 1, 0, 1, 1)

        self.t_label = QLabel(EdgeForm)
        self.t_label.setObjectName(u"t_label")
        sizePolicy.setHeightForWidth(self.t_label.sizePolicy().hasHeightForWidth())
        self.t_label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.t_label, 0, 0, 1, 1)

        self.edgeName_label = QLabel(EdgeForm)
        self.edgeName_label.setObjectName(u"edgeName_label")
        self.edgeName_label.setEnabled(True)
        sizePolicy.setHeightForWidth(self.edgeName_label.sizePolicy().hasHeightForWidth())
        self.edgeName_label.setSizePolicy(sizePolicy)
        self.edgeName_label.setFocusPolicy(Qt.NoFocus)
        self.edgeName_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.edgeName_label, 0, 1, 1, 1)

        self.edgeType_label = QLabel(EdgeForm)
        self.edgeType_label.setObjectName(u"edgeType_label")
        sizePolicy.setHeightForWidth(self.edgeType_label.sizePolicy().hasHeightForWidth())
        self.edgeType_label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.edgeType_label, 1, 1, 1, 1)

        self.t_label_3 = QLabel(EdgeForm)
        self.t_label_3.setObjectName(u"t_label_3")
        sizePolicy.setHeightForWidth(self.t_label_3.sizePolicy().hasHeightForWidth())
        self.t_label_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.t_label_3, 2, 0, 1, 1)

        self.weight_spinBox = QDoubleSpinBox(EdgeForm)
        self.weight_spinBox.setObjectName(u"weight_spinBox")
        self.weight_spinBox.setDecimals(3)

        self.gridLayout.addWidget(self.weight_spinBox, 2, 1, 1, 1)


        self.retranslateUi(EdgeForm)

        QMetaObject.connectSlotsByName(EdgeForm)
    # setupUi

    def retranslateUi(self, EdgeForm):
        EdgeForm.setWindowTitle(QCoreApplication.translate("EdgeForm", u"Form", None))
        self.t_label_2.setText(QCoreApplication.translate("EdgeForm", u"Type:", None))
        self.t_label.setText(QCoreApplication.translate("EdgeForm", u"Edge name:", None))
        self.edgeName_label.setText(QCoreApplication.translate("EdgeForm", u"edge_name", None))
        self.edgeType_label.setText(QCoreApplication.translate("EdgeForm", u"edge_type", None))
        self.t_label_3.setText(QCoreApplication.translate("EdgeForm", u"Weight:", None))
    # retranslateUi




