# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\admin\Desktop\pyqtQQ\ui\RegisterWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterWidget(object):
    def setupUi(self, RegisterWidget):
        RegisterWidget.setObjectName("RegisterWidget")
        RegisterWidget.resize(265, 267)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RegisterWidget.sizePolicy().hasHeightForWidth())
        RegisterWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(RegisterWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout_username = QtWidgets.QHBoxLayout()
        self.layout_username.setObjectName("layout_username")
        self.lb_username = CaptionLabel(RegisterWidget)
        self.lb_username.setObjectName("lb_username")
        self.layout_username.addWidget(self.lb_username)
        self.le_username = LineEdit(RegisterWidget)
        self.le_username.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhLatinOnly|QtCore.Qt.ImhNoAutoUppercase)
        self.le_username.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.le_username.setClearButtonEnabled(True)
        self.le_username.setObjectName("le_username")
        self.layout_username.addWidget(self.le_username)
        self.verticalLayout.addLayout(self.layout_username)
        self.layout_password = QtWidgets.QHBoxLayout()
        self.layout_password.setObjectName("layout_password")
        self.lb_password = CaptionLabel(RegisterWidget)
        self.lb_password.setObjectName("lb_password")
        self.layout_password.addWidget(self.lb_password)
        self.le_password = LineEdit(RegisterWidget)
        self.le_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhLatinOnly|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.le_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_password.setClearButtonEnabled(True)
        self.le_password.setObjectName("le_password")
        self.layout_password.addWidget(self.le_password)
        self.verticalLayout.addLayout(self.layout_password)
        self.layout_doublecheck = QtWidgets.QHBoxLayout()
        self.layout_doublecheck.setObjectName("layout_doublecheck")
        self.lb_doublecheck = CaptionLabel(RegisterWidget)
        self.lb_doublecheck.setObjectName("lb_doublecheck")
        self.layout_doublecheck.addWidget(self.lb_doublecheck)
        self.le_doublecheck = LineEdit(RegisterWidget)
        self.le_doublecheck.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhLatinOnly|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.le_doublecheck.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_doublecheck.setClearButtonEnabled(True)
        self.le_doublecheck.setObjectName("le_doublecheck")
        self.layout_doublecheck.addWidget(self.le_doublecheck)
        self.verticalLayout.addLayout(self.layout_doublecheck)
        self.layout_nickname = QtWidgets.QHBoxLayout()
        self.layout_nickname.setObjectName("layout_nickname")
        self.lb_nickname = CaptionLabel(RegisterWidget)
        self.lb_nickname.setObjectName("lb_nickname")
        self.layout_nickname.addWidget(self.lb_nickname)
        self.le_nickname = LineEdit(RegisterWidget)
        self.le_nickname.setText("")
        self.le_nickname.setClearButtonEnabled(True)
        self.le_nickname.setObjectName("le_nickname")
        self.layout_nickname.addWidget(self.le_nickname)
        self.verticalLayout.addLayout(self.layout_nickname)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_ok = PushButton(RegisterWidget)
        self.bt_ok.setAutoFillBackground(False)
        self.bt_ok.setObjectName("bt_ok")
        self.horizontalLayout.addWidget(self.bt_ok)
        self.bt_cancel = PushButton(RegisterWidget)
        self.bt_cancel.setObjectName("bt_cancel")
        self.horizontalLayout.addWidget(self.bt_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(RegisterWidget)
        QtCore.QMetaObject.connectSlotsByName(RegisterWidget)

    def retranslateUi(self, RegisterWidget):
        _translate = QtCore.QCoreApplication.translate
        RegisterWidget.setWindowTitle(_translate("RegisterWidget", "register"))
        self.lb_username.setText(_translate("RegisterWidget", "用户名"))
        self.lb_password.setText(_translate("RegisterWidget", "密码"))
        self.lb_doublecheck.setText(_translate("RegisterWidget", "确认密码"))
        self.lb_nickname.setText(_translate("RegisterWidget", "昵称"))
        self.le_nickname.setPlaceholderText(_translate("RegisterWidget", "默认名：mono"))
        self.bt_ok.setText(_translate("RegisterWidget", "确定"))
        self.bt_cancel.setText(_translate("RegisterWidget", "取消"))
from qfluentwidgets import CaptionLabel, LineEdit, PushButton
