# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("font: 13pt \"Cantarell\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 461, 41))
        self.label.setStyleSheet("font: 75 oblique 25pt \"Cantarell\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 80, 151, 31))
        self.label_2.setStyleSheet("font: 13pt \"Cantarell\";")
        self.label_2.setObjectName("label_2")
        self.choocie_line = QtWidgets.QComboBox(self.centralwidget)
        self.choocie_line.setGeometry(QtCore.QRect(370, 80, 191, 28))
        self.choocie_line.setEditable(False)
        self.choocie_line.setObjectName("choocie_line")
        self.choocie_line.addItem("")
        self.choocie_line.addItem("")
        self.choocie_line.addItem("")
        self.choocie_line.addItem("")
        self.choocie_line.setItemText(3, "")
        self.table_line = QtWidgets.QTableView(self.centralwidget)
        self.table_line.setGeometry(QtCore.QRect(70, 130, 651, 241))
        self.table_line.setObjectName("table_line")
        self.get_1 = QtWidgets.QPushButton(self.centralwidget)
        self.get_1.setGeometry(QtCore.QRect(410, 390, 84, 51))
        self.get_1.setObjectName("get_1")
        self.get_2 = QtWidgets.QPushButton(self.centralwidget)
        self.get_2.setGeometry(QtCore.QRect(410, 460, 84, 51))
        self.get_2.setObjectName("get_2")
        self.num_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.num_1.setGeometry(QtCore.QRect(320, 400, 49, 29))
        self.num_1.setObjectName("num_1")
        self.select_1 = QtWidgets.QComboBox(self.centralwidget)
        self.select_1.setGeometry(QtCore.QRect(150, 400, 79, 28))
        self.select_1.setObjectName("select_1")
        self.select_2 = QtWidgets.QComboBox(self.centralwidget)
        self.select_2.setGeometry(QtCore.QRect(150, 470, 79, 28))
        self.select_2.setObjectName("select_2")
        self.show_result = QtWidgets.QTextEdit(self.centralwidget)
        self.show_result.setGeometry(QtCore.QRect(580, 390, 141, 121))
        self.show_result.setObjectName("show_result")
        self.num_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.num_2.setGeometry(QtCore.QRect(320, 470, 49, 29))
        self.num_2.setObjectName("num_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 410, 63, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 470, 63, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 410, 63, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 480, 63, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(510, 429, 61, 41))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.choocie_line.setCurrentIndex(0)
        self.choocie_line.currentIndexChanged['int'].connect(MainWindow.change_table)
        self.get_1.clicked.connect(MainWindow.get_ticket1)
        self.get_2.clicked.connect(MainWindow.get_ticket2)
        self.select_1.currentIndexChanged['int'].connect(MainWindow.getBusNum)
        self.select_2.currentIndexChanged['int'].connect(MainWindow.getBusNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "city bus centern"))
        self.label.setText(_translate("MainWindow", "City Saling Bus Tickets System"))
        self.label_2.setText(_translate("MainWindow", "SELECT ROADLINE:"))
        self.choocie_line.setItemText(0, _translate("MainWindow", "JiangMen==>>GuangZhou"))
        self.choocie_line.setItemText(1, _translate("MainWindow", "GuangZhou==>>ShenZhen"))
        self.choocie_line.setItemText(2, _translate("MainWindow", "ShenZhen==>>JiangMen"))
        self.get_1.setText(_translate("MainWindow", "get from 1"))
        self.get_2.setText(_translate("MainWindow", "get from 2"))
        self.label_3.setText(_translate("MainWindow", "TimeTable"))
        self.label_4.setText(_translate("MainWindow", "TimeTable"))
        self.label_5.setText(_translate("MainWindow", "NumTic"))
        self.label_6.setText(_translate("MainWindow", "NumTic"))
        self.label_7.setText(_translate("MainWindow", "Result"))

