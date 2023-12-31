# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\admin\Desktop\pyqtQQ\ui\ContactItemWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ContactItemWidget(object):
    def setupUi(self, ContactItemWidget):
        ContactItemWidget.setObjectName("ContactItemWidget")
        ContactItemWidget.resize(280, 72)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ContactItemWidget.sizePolicy().hasHeightForWidth())
        ContactItemWidget.setSizePolicy(sizePolicy)
        ContactItemWidget.setMinimumSize(QtCore.QSize(0, 70))
        ContactItemWidget.setMaximumSize(QtCore.QSize(16777215, 90))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(ContactItemWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AvatarWidget = AvatarWidget(ContactItemWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AvatarWidget.sizePolicy().hasHeightForWidth())
        self.AvatarWidget.setSizePolicy(sizePolicy)
        self.AvatarWidget.setMinimumSize(QtCore.QSize(70, 70))
        self.AvatarWidget.setMaximumSize(QtCore.QSize(70, 70))
        self.AvatarWidget.setObjectName("AvatarWidget")
        self.horizontalLayout.addWidget(self.AvatarWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(1, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.nickname_or_groupName = TitleLabel(ContactItemWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nickname_or_groupName.sizePolicy().hasHeightForWidth())
        self.nickname_or_groupName.setSizePolicy(sizePolicy)
        self.nickname_or_groupName.setMinimumSize(QtCore.QSize(150, 0))
        self.nickname_or_groupName.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.nickname_or_groupName.setProperty("pixelFontSize", 20)
        self.nickname_or_groupName.setObjectName("nickname_or_groupName")
        self.verticalLayout.addWidget(self.nickname_or_groupName)
        self.username_or_groupID = BodyLabel(ContactItemWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_or_groupID.sizePolicy().hasHeightForWidth())
        self.username_or_groupID.setSizePolicy(sizePolicy)
        self.username_or_groupID.setMinimumSize(QtCore.QSize(150, 27))
        self.username_or_groupID.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.username_or_groupID.setProperty("pixelFontSize", 20)
        self.username_or_groupID.setObjectName("username_or_groupID")
        self.verticalLayout.addWidget(self.username_or_groupID)
        spacerItem1 = QtWidgets.QSpacerItem(1, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(ContactItemWidget)
        QtCore.QMetaObject.connectSlotsByName(ContactItemWidget)

    def retranslateUi(self, ContactItemWidget):
        _translate = QtCore.QCoreApplication.translate
        ContactItemWidget.setWindowTitle(_translate("ContactItemWidget", "Form"))
        self.nickname_or_groupName.setText(_translate("ContactItemWidget", "Title label"))
        self.username_or_groupID.setText(_translate("ContactItemWidget", "Body label"))
from qfluentwidgets import AvatarWidget, BodyLabel, TitleLabel
