# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main1.02.ui'
#
# Created: Sat Jan 25 10:48:08 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow007(object):
    def setupUi(self, MainWindow007):
        MainWindow007.setObjectName(_fromUtf8("MainWindow007"))
        MainWindow007.resize(1349, 701)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow007.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/new/Users/Gurvinder/Desktop/indian-cricket-logo.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow007.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow007)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 0, 281, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Calligraphy"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(30, 0, 0);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(300, 40, 1051, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 340, 1331, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 430, 621, 151))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 140, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1000, 130, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1000, 210, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(830, 50, 20, 211))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 220, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(150, 220, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(860, 140, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(860, 210, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(860, 350, 20, 311))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(840, 180, 511, 20))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(840, 100, 511, 20))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(860, 60, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(_fromUtf8(""))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(330, 90, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 260, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(150, 260, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setText(_fromUtf8(""))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1000, 70, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setText(_fromUtf8(""))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(500, 90, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setText(_fromUtf8(""))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(300, 190, 541, 20))
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(20, 300, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(140, 300, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setText(_fromUtf8(""))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(230, 280, 851, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setText(_fromUtf8(""))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(900, 430, 241, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(900, 380, 421, 31))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_3 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(900, 480, 69, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_7 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_7.setGeometry(QtCore.QRect(990, 480, 121, 22))
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.label_20 = QtGui.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(40, 360, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1220, 550, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.line_8 = QtGui.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(870, 510, 471, 20))
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.line_9 = QtGui.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(840, 250, 511, 20))
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 400, 211, 241))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.layoutWidget)
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.verticalLayout.addWidget(self.commandLinkButton)
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.layoutWidget)
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.verticalLayout.addWidget(self.commandLinkButton_2)
        self.commandLinkButton_3 = QtGui.QCommandLinkButton(self.layoutWidget)
        self.commandLinkButton_3.setObjectName(_fromUtf8("commandLinkButton_3"))
        self.verticalLayout.addWidget(self.commandLinkButton_3)
        self.commandLinkButton_5 = QtGui.QCommandLinkButton(self.layoutWidget)
        self.commandLinkButton_5.setObjectName(_fromUtf8("commandLinkButton_5"))
        self.verticalLayout.addWidget(self.commandLinkButton_5)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1120, 560, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(250, 350, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(990, 560, 111, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(900, 560, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 151, 151))
        self.frame.setStyleSheet(_fromUtf8("background-image: url(:/newPrefix/pics/530605_274550266005931_288515751_n.jpg);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(150, 0, 151, 151))
        self.frame_2.setStyleSheet(_fromUtf8("background-image: url(:/newPrefix/pics/download (1).jpg);"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_21 = QtGui.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(1080, 620, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        MainWindow007.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow007)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1349, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow007.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow007)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow007.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow007)
        QtCore.QMetaObject.connectSlotsByName(MainWindow007)

    def retranslateUi(self, MainWindow007):
        MainWindow007.setWindowTitle(_translate("MainWindow007", "CRICKET APP", None))
        self.label.setText(_translate("MainWindow007", "M.M.N.C.T 2014", None))
        self.label_7.setText(_translate("MainWindow007", "EXTRAS", None))
        self.label_9.setText(_translate("MainWindow007", "Strike", None))
        self.label_10.setText(_translate("MainWindow007", "Non Strike", None))
        self.label_11.setText(_translate("MainWindow007", "BATTING", None))
        self.label_12.setText(_translate("MainWindow007", "BOWLING", None))
        self.label_13.setText(_translate("MainWindow007", "Run Rate", None))
        self.label_17.setText(_translate("MainWindow007", "LAST OVER", None))
        self.comboBox.setItemText(0, _translate("MainWindow007", "Not Out", None))
        self.comboBox.setItemText(1, _translate("MainWindow007", "Bowled", None))
        self.comboBox.setItemText(2, _translate("MainWindow007", "Runout", None))
        self.comboBox.setItemText(3, _translate("MainWindow007", "Caught", None))
        self.comboBox.setItemText(4, _translate("MainWindow007", "Stumped", None))
        self.comboBox.setItemText(5, _translate("MainWindow007", "LBW", None))
        self.comboBox.setItemText(6, _translate("MainWindow007", "Hit wicket", None))
        self.comboBox.setItemText(7, _translate("MainWindow007", "Others", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow007", "RUN SCORED", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow007", "0", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow007", "1", None))
        self.comboBox_2.setItemText(3, _translate("MainWindow007", "2", None))
        self.comboBox_2.setItemText(4, _translate("MainWindow007", "3", None))
        self.comboBox_2.setItemText(5, _translate("MainWindow007", "4", None))
        self.comboBox_2.setItemText(6, _translate("MainWindow007", "5", None))
        self.comboBox_2.setItemText(7, _translate("MainWindow007", "6", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow007", "Extras", None))
        self.comboBox_3.setItemText(1, _translate("MainWindow007", "No ball", None))
        self.comboBox_3.setItemText(2, _translate("MainWindow007", "Wide", None))
        self.comboBox_3.setItemText(3, _translate("MainWindow007", "Leg bye", None))
        self.comboBox_3.setItemText(4, _translate("MainWindow007", "Bye", None))
        self.comboBox_3.setItemText(5, _translate("MainWindow007", "Others", None))
        self.comboBox_7.setItemText(0, _translate("MainWindow007", "0", None))
        self.comboBox_7.setItemText(1, _translate("MainWindow007", "1", None))
        self.comboBox_7.setItemText(2, _translate("MainWindow007", "2", None))
        self.comboBox_7.setItemText(3, _translate("MainWindow007", "3", None))
        self.comboBox_7.setItemText(4, _translate("MainWindow007", "4", None))
        self.comboBox_7.setItemText(5, _translate("MainWindow007", "5", None))
        self.comboBox_7.setItemText(6, _translate("MainWindow007", "6", None))
        self.label_20.setText(_translate("MainWindow007", "STATISTICS", None))
        self.pushButton.setText(_translate("MainWindow007", "SUBMIT", None))
        self.commandLinkButton.setText(_translate("MainWindow007", "Scorecard", None))
        self.commandLinkButton_2.setText(_translate("MainWindow007", "Batting stats", None))
        self.commandLinkButton_3.setText(_translate("MainWindow007", "Bowing Stats", None))
        self.commandLinkButton_5.setText(_translate("MainWindow007", "Fall of wickets", None))
        self.pushButton_2.setText(_translate("MainWindow007", "Declare", None))
        self.pushButton_3.setText(_translate("MainWindow007", "Change Strike", None))
        self.pushButton_4.setText(_translate("MainWindow007", "Back", None))
        self.label_21.setText(_translate("MainWindow007", "Developed By -> Gurvinder Singh", None))

import pro2