from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_NodeForm(object):
    def setupUi(self, NodeForm):
        if not NodeForm.objectName():
            NodeForm.setObjectName(u"NodeForm")
        NodeForm.resize(400, 300)
        self.gridLayout = QGridLayout(NodeForm)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.t_label = QLabel(NodeForm)
        self.t_label.setObjectName(u"t_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t_label.sizePolicy().hasHeightForWidth())
        self.t_label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.t_label, 0, 0, 1, 1)

        self.nodeName_label = QLabel(NodeForm)
        self.nodeName_label.setObjectName(u"nodeName_label")
        self.nodeName_label.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nodeName_label.sizePolicy().hasHeightForWidth())
        self.nodeName_label.setSizePolicy(sizePolicy1)
        self.nodeName_label.setFocusPolicy(Qt.NoFocus)
        self.nodeName_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.nodeName_label, 0, 1, 1, 1)

        self.t_label_2 = QLabel(NodeForm)
        self.t_label_2.setObjectName(u"t_label_2")
        sizePolicy.setHeightForWidth(self.t_label_2.sizePolicy().hasHeightForWidth())
        self.t_label_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.t_label_2, 1, 0, 1, 1)

        self.nodeType_label = QLabel(NodeForm)
        self.nodeType_label.setObjectName(u"nodeType_label")
        sizePolicy1.setHeightForWidth(self.nodeType_label.sizePolicy().hasHeightForWidth())
        self.nodeType_label.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.nodeType_label, 1, 1, 1, 1)

        self.availability_checkBox = QCheckBox(NodeForm)
        self.availability_checkBox.setObjectName(u"availability_checkBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.availability_checkBox.sizePolicy().hasHeightForWidth())
        self.availability_checkBox.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.availability_checkBox, 2, 0, 1, 1)

        self.leftSide_checkBox = QCheckBox(NodeForm)
        self.leftSide_checkBox.setObjectName(u"leftSide_checkBox")

        self.gridLayout.addWidget(self.leftSide_checkBox, 3, 0, 1, 1)

        self.rightSide_checkBox = QCheckBox(NodeForm)
        self.rightSide_checkBox.setObjectName(u"rightSide_checkBox")

        self.gridLayout.addWidget(self.rightSide_checkBox, 3, 1, 1, 1)


        self.retranslateUi(NodeForm)

        QMetaObject.connectSlotsByName(NodeForm)
    # setupUi

    def retranslateUi(self, NodeForm):
        NodeForm.setWindowTitle(QCoreApplication.translate("NodeForm", u"Form", None))
        self.t_label.setText(QCoreApplication.translate("NodeForm", u"Node name:", None))
        self.nodeName_label.setText(QCoreApplication.translate("NodeForm", u"node_name", None))
        self.t_label_2.setText(QCoreApplication.translate("NodeForm", u"Type:", None))
        self.nodeType_label.setText(QCoreApplication.translate("NodeForm", u"node_type", None))
        self.availability_checkBox.setText(QCoreApplication.translate("NodeForm", u"Available", None))
        self.leftSide_checkBox.setText(QCoreApplication.translate("NodeForm", u"Left Side", None))
        self.rightSide_checkBox.setText(QCoreApplication.translate("NodeForm", u"Right Side", None))
    # retranslateUi

