# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoStudentClass.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 292)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 93, 81, 21))
        self.label_2.setObjectName("label_2")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(30, 190, 321, 31))
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.ButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.ButtonClickMe.setGeometry(QtCore.QRect(150, 250, 75, 23))
        self.ButtonClickMe.setObjectName("ButtonClickMe")
        self.lineEditCode = QtWidgets.QLineEdit(Dialog)
        self.lineEditCode.setGeometry(QtCore.QRect(130, 40, 211, 21))
        self.lineEditCode.setObjectName("lineEditCode")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(130, 100, 211, 21))
        self.lineEditName.setObjectName("lineEditName")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Student Code"))
        self.label_2.setText(_translate("Dialog", "Student Name"))
        self.ButtonClickMe.setText(_translate("Dialog", "Click"))
