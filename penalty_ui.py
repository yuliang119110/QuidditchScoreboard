# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'penalty.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Penalty(object):
    def setupUi(self, Penalty):
        Penalty.setObjectName("Penalty")
        Penalty.resize(1359, 921)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Penalty)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.teamLeftButton = QtWidgets.QRadioButton(Penalty)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teamLeftButton.setFont(font)
        self.teamLeftButton.setObjectName("teamLeftButton")
        self.horizontalLayout.addWidget(self.teamLeftButton)
        self.teamRightButton = QtWidgets.QRadioButton(Penalty)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teamRightButton.setFont(font)
        self.teamRightButton.setObjectName("teamRightButton")
        self.horizontalLayout.addWidget(self.teamRightButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(Penalty)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.frame.setFont(font)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.blueButton = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.blueButton.setFont(font)
        self.blueButton.setObjectName("blueButton")
        self.horizontalLayout_2.addWidget(self.blueButton)
        self.yellowButton = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yellowButton.setFont(font)
        self.yellowButton.setObjectName("yellowButton")
        self.horizontalLayout_2.addWidget(self.yellowButton)
        self.yellowredButton = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yellowredButton.setFont(font)
        self.yellowredButton.setObjectName("yellowredButton")
        self.horizontalLayout_2.addWidget(self.yellowredButton)
        self.redButton = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.redButton.setFont(font)
        self.redButton.setObjectName("redButton")
        self.horizontalLayout_2.addWidget(self.redButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(Penalty)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.input_number = QtWidgets.QLineEdit(Penalty)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_number.sizePolicy().hasHeightForWidth())
        self.input_number.setSizePolicy(sizePolicy)
        self.input_number.setObjectName("input_number")
        self.horizontalLayout_5.addWidget(self.input_number)
        self.label_2 = QtWidgets.QLabel(Penalty)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.list_players = QtWidgets.QComboBox(Penalty)
        self.list_players.setObjectName("list_players")
        self.horizontalLayout_5.addWidget(self.list_players)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(Penalty)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.input_reason = QtWidgets.QLineEdit(Penalty)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_reason.sizePolicy().hasHeightForWidth())
        self.input_reason.setSizePolicy(sizePolicy)
        self.input_reason.setObjectName("input_reason")
        self.horizontalLayout_6.addWidget(self.input_reason)
        self.label_4 = QtWidgets.QLabel(Penalty)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.list_reasons = QtWidgets.QComboBox(Penalty)
        self.list_reasons.setObjectName("list_reasons")
        self.horizontalLayout_6.addWidget(self.list_reasons)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(Penalty)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_7.addWidget(self.cancelButton)
        self.okButton = QtWidgets.QPushButton(Penalty)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_7.addWidget(self.okButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.retranslateUi(Penalty)
        self.cancelButton.clicked.connect(Penalty.accept)
        self.okButton.clicked.connect(Penalty.ok)
        self.teamLeftButton.clicked.connect(Penalty.team_chosen)
        self.teamRightButton.clicked.connect(Penalty.team_chosen)
        QtCore.QMetaObject.connectSlotsByName(Penalty)

    def retranslateUi(self, Penalty):
        _translate = QtCore.QCoreApplication.translate
        Penalty.setWindowTitle(_translate("Penalty", "Penalty"))
        self.teamLeftButton.setText(_translate("Penalty", "Team Left"))
        self.teamRightButton.setText(_translate("Penalty", "Team Right"))
        self.blueButton.setText(_translate("Penalty", "Blue Card"))
        self.yellowButton.setText(_translate("Penalty", "Yellow Card"))
        self.yellowredButton.setText(_translate("Penalty", "Yellow, Red Card"))
        self.redButton.setText(_translate("Penalty", "Red Card"))
        self.label.setText(_translate("Penalty", "Player number:"))
        self.label_2.setText(_translate("Penalty", "OR choose Player:"))
        self.label_3.setText(_translate("Penalty", "Give reason:"))
        self.label_4.setText(_translate("Penalty", "OR choose one:"))
        self.cancelButton.setText(_translate("Penalty", "Cancel"))
        self.okButton.setText(_translate("Penalty", "Ok"))

