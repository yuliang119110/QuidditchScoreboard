# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scores.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(661, 467)
        self.verticalLayout = QtWidgets.QVBoxLayout(main)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.time_header = QtWidgets.QLabel(main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_header.sizePolicy().hasHeightForWidth())
        self.time_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.time_header.setFont(font)
        self.time_header.setTextFormat(QtCore.Qt.AutoText)
        self.time_header.setAlignment(QtCore.Qt.AlignCenter)
        self.time_header.setObjectName("time_header")
        self.gridLayout_2.addWidget(self.time_header, 0, 0, 1, 1)
        self.timerLayout = QtWidgets.QHBoxLayout()
        self.timerLayout.setObjectName("timerLayout")
        self.startTimer = QtWidgets.QPushButton(main)
        self.startTimer.setObjectName("startTimer")
        self.timerLayout.addWidget(self.startTimer)
        self.stopTimer = QtWidgets.QPushButton(main)
        self.stopTimer.setObjectName("stopTimer")
        self.timerLayout.addWidget(self.stopTimer)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.setTimer = QtWidgets.QPushButton(main)
        self.setTimer.setObjectName("setTimer")
        self.verticalLayout_3.addWidget(self.setTimer)
        self.timeEdit = QtWidgets.QTimeEdit(main)
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout_3.addWidget(self.timeEdit)
        self.timerLayout.addLayout(self.verticalLayout_3)
        self.gridLayout_2.addLayout(self.timerLayout, 2, 0, 1, 1)
        self.time_label = QtWidgets.QLabel(main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_label.sizePolicy().hasHeightForWidth())
        self.time_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.time_label.setFont(font)
        self.time_label.setTextFormat(QtCore.Qt.AutoText)
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.gridLayout_2.addWidget(self.time_label, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.extratimerButton = QtWidgets.QPushButton(main)
        self.extratimerButton.setObjectName("extratimerButton")
        self.horizontalLayout_4.addWidget(self.extratimerButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(main)
        self.line.setMinimumSize(QtCore.QSize(0, 8))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(4)
        self.line.setMidLineWidth(4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.score_header = QtWidgets.QLabel(main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.score_header.sizePolicy().hasHeightForWidth())
        self.score_header.setSizePolicy(sizePolicy)
        self.score_header.setBaseSize(QtCore.QSize(3, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.score_header.setFont(font)
        self.score_header.setAlignment(QtCore.Qt.AlignCenter)
        self.score_header.setObjectName("score_header")
        self.verticalLayout_4.addWidget(self.score_header)
        self.scoreLayout = QtWidgets.QGridLayout()
        self.scoreLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.scoreLayout.setHorizontalSpacing(12)
        self.scoreLayout.setVerticalSpacing(0)
        self.scoreLayout.setObjectName("scoreLayout")
        self.score_labels = QtWidgets.QHBoxLayout()
        self.score_labels.setSpacing(0)
        self.score_labels.setObjectName("score_labels")
        self.score_left = QtWidgets.QLabel(main)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.score_left.setFont(font)
        self.score_left.setObjectName("score_left")
        self.score_labels.addWidget(self.score_left)
        self.point = QtWidgets.QLabel(main)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.point.setFont(font)
        self.point.setAlignment(QtCore.Qt.AlignCenter)
        self.point.setObjectName("point")
        self.score_labels.addWidget(self.point)
        self.score_right = QtWidgets.QLabel(main)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.score_right.setFont(font)
        self.score_right.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.score_right.setObjectName("score_right")
        self.score_labels.addWidget(self.score_right)
        self.scoreLayout.addLayout(self.score_labels, 1, 2, 1, 1)
        self.scorebutton_left = QtWidgets.QVBoxLayout()
        self.scorebutton_left.setSpacing(0)
        self.scorebutton_left.setObjectName("scorebutton_left")
        self.add10_left = QtWidgets.QPushButton(main)
        self.add10_left.setDefault(False)
        self.add10_left.setFlat(False)
        self.add10_left.setObjectName("add10_left")
        self.scorebutton_left.addWidget(self.add10_left)
        self.resetscore_left = QtWidgets.QPushButton(main)
        self.resetscore_left.setObjectName("resetscore_left")
        self.scorebutton_left.addWidget(self.resetscore_left)
        self.sub10_left = QtWidgets.QPushButton(main)
        self.sub10_left.setObjectName("sub10_left")
        self.scorebutton_left.addWidget(self.sub10_left)
        self.scoreLayout.addLayout(self.scorebutton_left, 1, 1, 1, 1)
        self.scorebutton_right = QtWidgets.QVBoxLayout()
        self.scorebutton_right.setSpacing(0)
        self.scorebutton_right.setObjectName("scorebutton_right")
        self.add10_right = QtWidgets.QPushButton(main)
        self.add10_right.setObjectName("add10_right")
        self.scorebutton_right.addWidget(self.add10_right)
        self.resetscore_right = QtWidgets.QPushButton(main)
        self.resetscore_right.setObjectName("resetscore_right")
        self.scorebutton_right.addWidget(self.resetscore_right)
        self.sub10_right = QtWidgets.QPushButton(main)
        self.sub10_right.setObjectName("sub10_right")
        self.scorebutton_right.addWidget(self.sub10_right)
        self.scoreLayout.addLayout(self.scorebutton_right, 1, 3, 1, 1)
        self.teamname_left = QtWidgets.QLabel(main)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teamname_left.setFont(font)
        self.teamname_left.setObjectName("teamname_left")
        self.scoreLayout.addWidget(self.teamname_left, 1, 0, 1, 1)
        self.teamname_right = QtWidgets.QLabel(main)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teamname_right.setFont(font)
        self.teamname_right.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.teamname_right.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.teamname_right.setObjectName("teamname_right")
        self.scoreLayout.addWidget(self.teamname_right, 1, 4, 1, 1)
        self.verticalLayout_4.addLayout(self.scoreLayout)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.snitchCatchButton = QtWidgets.QPushButton(main)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.snitchCatchButton.setFont(font)
        self.snitchCatchButton.setObjectName("snitchCatchButton")
        self.horizontalLayout.addWidget(self.snitchCatchButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(main)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.settingsButton = QtWidgets.QPushButton(main)
        self.settingsButton.setObjectName("settingsButton")
        self.horizontalLayout_5.addWidget(self.settingsButton)
        self.timekeeperButton = QtWidgets.QPushButton(main)
        self.timekeeperButton.setObjectName("timekeeperButton")
        self.horizontalLayout_5.addWidget(self.timekeeperButton)
        self.penaltyButton = QtWidgets.QPushButton(main)
        self.penaltyButton.setObjectName("penaltyButton")
        self.horizontalLayout_5.addWidget(self.penaltyButton)
        self.closeButton = QtWidgets.QPushButton(main)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_5.addWidget(self.closeButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.stopTimer.setEnabled(False);

        self.retranslateUi(main)
        self.add10_left.clicked.connect(lambda x: main.add_left(10))
        self.sub10_left.clicked.connect(lambda x: main.add_left(-10))
        self.add10_right.clicked.connect(lambda x: main.add_right(10))
        self.sub10_right.clicked.connect(lambda x: main.add_right(-10))
        self.startTimer.clicked.connect(main.start_timer)
        self.stopTimer.clicked.connect(main.stop_timer)
        self.setTimer.clicked.connect(main.set_timer)
        self.resetscore_left.clicked.connect(main.reset_left)
        self.resetscore_right.clicked.connect(main.reset_right)
        self.closeButton.clicked.connect(main.close)
        self.timekeeperButton.clicked.connect(main.timekeeper_start)
        self.settingsButton.clicked.connect(main.settings_start)
        self.penaltyButton.clicked.connect(main.open_penalty)
        self.snitchCatchButton.clicked.connect(main.snitch_catch)
        self.extratimerButton.clicked.connect(main.add_timer)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Main"))
        self.time_header.setText(_translate("main", "Game Time"))
        self.startTimer.setText(_translate("main", "Start"))
        self.stopTimer.setText(_translate("main", "Stop"))
        self.setTimer.setText(_translate("main", "Set"))
        self.timeEdit.setDisplayFormat(_translate("main", "mm:ss"))
        self.time_label.setText(_translate("main", "00:00"))
        self.extratimerButton.setText(_translate("main", "Get extra timer"))
        self.score_header.setText(_translate("main", "Scores"))
        self.score_left.setText(_translate("main", "score"))
        self.point.setText(_translate("main", ":"))
        self.score_right.setText(_translate("main", "score"))
        self.add10_left.setText(_translate("main", "+10"))
        self.resetscore_left.setText(_translate("main", "reset"))
        self.sub10_left.setText(_translate("main", "-10"))
        self.add10_right.setText(_translate("main", "+10"))
        self.resetscore_right.setText(_translate("main", "reset"))
        self.sub10_right.setText(_translate("main", "-10"))
        self.teamname_left.setText(_translate("main", "Team A"))
        self.teamname_right.setText(_translate("main", "Team B"))
        self.snitchCatchButton.setText(_translate("main", "Snitch Catch"))
        self.label.setText(_translate("main", "Only clickable if the gametime is paused"))
        self.settingsButton.setText(_translate("main", "Settings"))
        self.timekeeperButton.setText(_translate("main", "Start Timekeeper"))
        self.penaltyButton.setText(_translate("main", "Set Penalty"))
        self.closeButton.setText(_translate("main", "Close"))
    '''
    # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scores.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(661, 467)
        self.verticalLayout = QtWidgets.QVBoxLayout(main)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.time_header = QtWidgets.QLabel(main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_header.sizePolicy().hasHeightForWidth())
        self.time_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.time_header.setFont(font)
        self.time_header.setTextFormat(QtCore.Qt.AutoText)
        self.time_header.setAlignment(QtCore.Qt.AlignCenter)
        self.time_header.setObjectName("time_header")
        self.gridLayout_2.addWidget(self.time_header, 0, 0, 1, 1)
        self.timerLayout = QtWidgets.QHBoxLayout()
        self.timerLayout.setObjectName("timerLayout")
        self.startTimer = QtWidgets.QPushButton(main)
        self.startTimer.setObjectName("startTimer")
        self.timerLayout.addWidget(self.startTimer)
        self.stopTimer = QtWidgets.QPushButton(main)
        self.stopTimer.setObjectName("stopTimer")
        self.timerLayout.addWidget(self.stopTimer)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.setTimer = QtWidgets.QPushButton(main)
        self.setTimer.setObjectName("setTimer")
        self.verticalLayout_3.addWidget(self.setTimer)
        self.timeEdit = QtWidgets.QTimeEdit(main)
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout_3.addWidget(self.timeEdit)
        self.timerLayout.addLayout(self.verticalLayout_3)
        self.gridLayout_2.addLayout(self.timerLayout, 2, 0, 1, 1)
        self.time_label = QtWidgets.QLabel(main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_label.sizePolicy().hasHeightForWidth())
        self.time_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.time_label.setFont(font)
        self.time_label.setTextFormat(QtCore.Qt.AutoText)
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.gridLayout_2.addWidget(self.time_label, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.extratimerButton = QtWidgets.QPushButton(main)
        self.extratimerButton.setObjectName("extratimerButton")
        self.horizontalLayout_4.addWidget(self.extratimerButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(main)
        self.line.setMinimumSize(QtCore.QSize(0, 8))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(4)
        self.line.setMidLineWidth(4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.score_header = QtWidgets.QLabel(main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.score_header.sizePolicy().hasHeightForWidth())
        self.score_header.setSizePolicy(sizePolicy)
        self.score_header.setBaseSize(QtCore.QSize(3, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.score_header.setFont(font)
        self.score_header.setAlignment(QtCore.Qt.AlignCenter)
        self.score_header.setObjectName("score_header")
        self.verticalLayout_4.addWidget(self.score_header)
        self.scoreLayout = QtWidgets.QGridLayout()
        self.scoreLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.scoreLayout.setHorizontalSpacing(12)
        self.scoreLayout.setVerticalSpacing(0)
        self.scoreLayout.setObjectName("scoreLayout")
        self.score_labels = QtWidgets.QHBoxLayout()
        self.score_labels.setSpacing(0)
        self.score_labels.setObjectName("score_labels")
        self.score_left = QtWidgets.QLabel(main)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.score_left.setFont(font)
        self.score_left.setObjectName("score_left")
        self.score_labels.addWidget(self.score_left)
        self.point = QtWidgets.QLabel(main)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.point.setFont(font)
        self.point.setAlignment(QtCore.Qt.AlignCenter)
        self.point.setObjectName("point")
        self.score_labels.addWidget(self.point)
        self.score_right = QtWidgets.QLabel(main)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.score_right.setFont(font)
        self.score_right.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.score_right.setObjectName("score_right")
        self.score_labels.addWidget(self.score_right)
        self.scoreLayout.addLayout(self.score_labels, 1, 2, 1, 1)
        self.scorebutton_left = QtWidgets.QVBoxLayout()
        self.scorebutton_left.setSpacing(0)
        self.scorebutton_left.setObjectName("scorebutton_left")
        self.add10_left = QtWidgets.QPushButton(main)
        self.add10_left.setDefault(False)
        self.add10_left.setFlat(False)
        self.add10_left.setObjectName("add10_left")
        self.scorebutton_left.addWidget(self.add10_left)
        self.resetscore_left = QtWidgets.QPushButton(main)
        self.resetscore_left.setObjectName("resetscore_left")
        self.scorebutton_left.addWidget(self.resetscore_left)
        self.sub10_left = QtWidgets.QPushButton(main)
        self.sub10_left.setObjectName("sub10_left")
        self.scorebutton_left.addWidget(self.sub10_left)
        self.scoreLayout.addLayout(self.scorebutton_left, 1, 1, 1, 1)
        self.scorebutton_right = QtWidgets.QVBoxLayout()
        self.scorebutton_right.setSpacing(0)
        self.scorebutton_right.setObjectName("scorebutton_right")
        self.add10_right = QtWidgets.QPushButton(main)
        self.add10_right.setObjectName("add10_right")
        self.scorebutton_right.addWidget(self.add10_right)
        self.resetscore_right = QtWidgets.QPushButton(main)
        self.resetscore_right.setObjectName("resetscore_right")
        self.scorebutton_right.addWidget(self.resetscore_right)
        self.sub10_right = QtWidgets.QPushButton(main)
        self.sub10_right.setObjectName("sub10_right")
        self.scorebutton_right.addWidget(self.sub10_right)
        self.scoreLayout.addLayout(self.scorebutton_right, 1, 3, 1, 1)
        self.teamname_left = QtWidgets.QLabel(main)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teamname_left.setFont(font)
        self.teamname_left.setObjectName("teamname_left")
        self.scoreLayout.addWidget(self.teamname_left, 1, 0, 1, 1)
        self.teamname_right = QtWidgets.QLabel(main)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teamname_right.setFont(font)
        self.teamname_right.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.teamname_right.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.teamname_right.setObjectName("teamname_right")
        self.scoreLayout.addWidget(self.teamname_right, 1, 4, 1, 1)
        self.verticalLayout_4.addLayout(self.scoreLayout)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.snitchCatchButton = QtWidgets.QPushButton(main)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.snitchCatchButton.setFont(font)
        self.snitchCatchButton.setObjectName("snitchCatchButton")
        self.horizontalLayout.addWidget(self.snitchCatchButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(main)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.settingsButton = QtWidgets.QPushButton(main)
        self.settingsButton.setObjectName("settingsButton")
        self.horizontalLayout_5.addWidget(self.settingsButton)
        self.timekeeperButton = QtWidgets.QPushButton(main)
        self.timekeeperButton.setObjectName("timekeeperButton")
        self.horizontalLayout_5.addWidget(self.timekeeperButton)
        self.penaltyButton = QtWidgets.QPushButton(main)
        self.penaltyButton.setObjectName("penaltyButton")
        self.horizontalLayout_5.addWidget(self.penaltyButton)
        self.closeButton = QtWidgets.QPushButton(main)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_5.addWidget(self.closeButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.stopTimer.setEnabled(False);

        self.retranslateUi(main)
        self.add10_left.clicked.connect(lambda x: main.add_left(10))
        self.sub10_left.clicked.connect(lambda x: main.add_left(-10))
        self.add10_right.clicked.connect(lambda x: main.add_right(10))
        self.sub10_right.clicked.connect(lambda x: main.add_right(-10))
        self.startTimer.clicked.connect(main.start_timer)
        self.stopTimer.clicked.connect(main.stop_timer)
        self.setTimer.clicked.connect(main.set_timer)
        self.resetscore_left.clicked.connect(main.reset_left)
        self.resetscore_right.clicked.connect(main.reset_right)
        self.closeButton.clicked.connect(main.close)
        self.timekeeperButton.clicked.connect(main.timekeeper_start)
        self.settingsButton.clicked.connect(main.settings_start)
        self.penaltyButton.clicked.connect(main.open_penalty)
        self.snitchCatchButton.clicked.connect(main.snitch_catch)
        self.extratimerButton.clicked.connect(main.add_timer)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Main"))
        self.time_header.setText(_translate("main", "Game Time"))
        self.startTimer.setText(_translate("main", "Start"))
        self.stopTimer.setText(_translate("main", "Stop"))
        self.setTimer.setText(_translate("main", "Set"))
        self.timeEdit.setDisplayFormat(_translate("main", "mm:ss"))
        self.time_label.setText(_translate("main", "00:00"))
        self.extratimerButton.setText(_translate("main", "Get extra timer"))
        self.score_header.setText(_translate("main", "Scores"))
        self.score_left.setText(_translate("main", "score"))
        self.point.setText(_translate("main", ":"))
        self.score_right.setText(_translate("main", "score"))
        self.add10_left.setText(_translate("main", "+10"))
        self.resetscore_left.setText(_translate("main", "reset"))
        self.sub10_left.setText(_translate("main", "-10"))
        self.add10_right.setText(_translate("main", "+10"))
        self.resetscore_right.setText(_translate("main", "reset"))
        self.sub10_right.setText(_translate("main", "-10"))
        self.teamname_left.setText(_translate("main", "Team A"))
        self.teamname_right.setText(_translate("main", "Team B"))
        self.snitchCatchButton.setText(_translate("main", "Snitch Catch"))
        self.label.setText(_translate("main", "Only clickable if the gametime is paused"))
        self.settingsButton.setText(_translate("main", "Settings"))
        self.timekeeperButton.setText(_translate("main", "Start Timekeeper"))
        self.penaltyButton.setText(_translate("main", "Set Penalty"))
        self.closeButton.setText(_translate("main", "Close"))

    def expand(self, main):
        main.resize(661,700)
        self.extratimerButtonchecked = True
        self.extratimerlabel = QtWidgets.QLabel(main)
        self.extratimerlabel.setObjectName("extratimerlabel")
        self.extratimerlabel.setText("Extra Timer")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.extratimerlabel.setFont(font)
        self.extratimerlabel.setTextFormat(QtCore.Qt.AutoText)
        self.extratimerlabel.setAlignment(QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addWidget(self.extratimerlabel)

    def shrink(self, main):
        self.extratimerButtonchecked = False
        self.horizontalLayout_3.removeWidget(self.extratimerlabel)
        main.resize(661, 500)
    '''