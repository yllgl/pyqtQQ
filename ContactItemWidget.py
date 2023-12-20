from PyQt5.QtWidgets import QApplication,  QWidget
from PyQt5.QtCore import  pyqtProperty, Qt,QSize
from PyQt5.QtGui import  QPixmap,QFontMetrics
import resources_rc
import sys
from ui.Ui_ContactItemWidget import Ui_ContactItemWidget
from FriendChatWindow import FriendChatWindow
from GroupChatWindow import GroupChatWindow
import DataManager
class ContactItemWidget(Ui_ContactItemWidget,QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        #请注释掉下面三行代码
        self.AvatarWidget.setPixmap(QPixmap(":/images/DefaultContactAvatar.png").scaled(65,65,Qt.KeepAspectRatio,Qt.SmoothTransformation))
        self.username_or_groupID.setStyleSheet("color:rgb(70,70,70);")
        self.groupID = None
        self.username = None
        self.groupName = None
        self.nickname = None
        self.chatWindow = None
        self._avatar = None
    def setAvatar(self,avatar):
        if isinstance(avatar,bytes):
            pixmap = QPixmap()
            if pixmap.loadFromData(avatar):
                self.AvatarWidget.setPixmap(pixmap.scaled(65,65,Qt.KeepAspectRatio,Qt.SmoothTransformation))
        else:
            self.AvatarWidget.setPixmap(QPixmap(avatar).scaled(65,65,Qt.KeepAspectRatio,Qt.SmoothTransformation))
    def setUsername(self,username):
        text = f"(ID: {username})"
        elidfont = QFontMetrics(self.username_or_groupID.font())
        elidedText = elidfont.elidedText(text, Qt.ElideRight, self.width()-self.AvatarWidget.width()-5)
        self.username_or_groupID.setText(elidedText)
        self.username = username
        self.groupID = None

    def setNickname(self,nickname):
        text = nickname
        elidfont = QFontMetrics(self.nickname_or_groupName.font())
        elidedText = elidfont.elidedText(text, Qt.ElideRight, self.width()-self.AvatarWidget.width()-5)
        self.nickname_or_groupName.setText(elidedText)
        self.nickname = nickname
        self.groupName = None
    def setGroupID(self,groupID):
        text = f"(ID: {groupID})"
        elidfont = QFontMetrics(self.username_or_groupID.font())
        elidedText = elidfont.elidedText(text, Qt.ElideRight, self.width()-self.AvatarWidget.width()-5)
        self.username_or_groupID.setText(elidedText)
        self.groupID = groupID
        self.username = None
    def setGroupName(self,groupName):
        text = groupName
        elidfont = QFontMetrics(self.nickname_or_groupName.font())
        elidedText = elidfont.elidedText(text, Qt.ElideRight, self.width()-self.AvatarWidget.width()-5)
        self.nickname_or_groupName.setText(elidedText)
        self.groupName = groupName
        self.nickname = None
    def sizeHint(self):
        return QSize(super().sizeHint().width(),self.minimumHeight())
    def resizeEvent(self, event) -> None:
        ret = super().resizeEvent(event)
        if self.groupID:
            self.setGroupID(self.groupID)
        elif self.username:
            self.setUsername(self.username)
        if self.groupName:
            self.setGroupName(self.groupName)
        elif self.nickname:
            self.setNickname(self.nickname)
        return ret
    def mouseDoubleClickEvent(self, a0) -> None:
        ret =  super().mouseDoubleClickEvent(a0)
        self.openChatWindow()
        if self.username:
            print("ContactItemWidget:mouseDoubleClickEvent:username:",self.username)
            avatar = DataManager.db_manager.getAvatarByUsername(self.username)
            if avatar and self._avatar!=avatar:
                self.setAvatar(avatar)
        return ret
    def openChatWindow(self):
        if self.groupID is not None and self.groupName is not None:
            if self.chatWindow is None:
                self.chatWindow = GroupChatWindow(None,self.groupID,self.groupName)
                self.chatWindow.closed.connect(lambda : setattr(self,"chatWindow",None))
                self.chatWindow.show()
            else:
                self.chatWindow.show()
        elif self.username is not None and self.nickname is not None:
            if self.chatWindow is None:
                self.chatWindow = FriendChatWindow(None,self.username,self.nickname)
                self.chatWindow.closed.connect(lambda : setattr(self,"chatWindow",None))
                self.chatWindow.show()
            else:
                self.chatWindow.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    widget = ContactItemWidget(window)
    window.show()
    sys.exit(app.exec_())