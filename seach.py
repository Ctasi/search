from PyQt5.Qt import *
from PyQt5 import QtGui
import sys
import json
import requests

class login(QWidget):

    def __init__(self):
        # 调用父级模块
        super().__init__()
        self.setup_ui()
    # UI界面方法
    def setup_ui(self):
        with open("qss/login.qss",'r') as f:
            qApp.setStyleSheet(f.read())
        labelbg = QLabel(self)
        labelbg.setObjectName('labelbgs')
        labelbg.resize(531, 329)
        title = self.setWindowTitle('查询软件')
        #隐藏边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 左侧图片s
        pix = QPixmap('img.jpg')
        label = QLabel(self)
        label.setGeometry(0, 0, 260, 329)
        label.setPixmap(pix)
        #关闭按钮
        btnExit = QPushButton(self)
        btnExit.setObjectName('Exit')
        btnExit.resize(50,20)
        btnExit.move(480,0)
        btnExit.clicked.connect(self.close)
        btnExit.setCursor(QCursor(Qt.PointingHandCursor))
        btnExit.setText('关闭')
        #最小化
        btnMinimum = QPushButton(self)
        btnMinimum.setObjectName('Minimum')
        btnMinimum.resize(50,20)
        btnMinimum.move(380,0)
        btnMinimum.setCursor(QCursor(Qt.PointingHandCursor))
        btnMinimum.clicked.connect(self.showMinimized)
        btnMinimum.setText('最小化')
        #最大化
        btnBig = QPushButton(self)
        btnBig.setObjectName('big')
        btnBig.resize(50,20)
        btnBig.move(430,0)
        btnBig.setCursor(QCursor(Qt.PointingHandCursor))
        btnBig.clicked.connect(self.showMaximized)
        btnBig.setText('最大化')
        #账号
        self.textbox = QLineEdit(self)
        self.textbox.move(290, 160)
        self.textbox.resize(220, 40)
        self.textbox.setObjectName('userInput')
        self.textbox.setFont(QFont("Microsoft YaHei" , 18, 75))
        #标题
        self.h1 = QLabel(self)
        self.h1.setText('cccccccc')
        self.h1.move(290, 80)
        self.textbox.setFont(QFont("Microsoft YaHei" , 18, 75))
        self.h1.setStyleSheet("color:#ffffff;font-size:50px;")

        #登录按钮
        btnLogin = QPushButton(self)
        btnLogin.setObjectName('btnLogin')
        btnLogin.resize(100,40)
        btnLogin.move(290,220)
        btnLogin.setCursor(QCursor(Qt.PointingHandCursor))
        btnLogin.setText('登录')
        btnLogin.clicked.connect(self.login_in)
        self.show()

    def login_in(self):
        username = self.textbox.text()
        # password = str(self.lineEdit_passwd.text())
        baseurl = 'http://api.yzt-tools.com/api/wtx/report/adminloginIn'
        data = {'username': str(username)}
        try:
            res = requests.post(url=baseurl, data=data, timeout=3)
        except Exception as e:
            #QtGui.QMessageBox.critical(self, u'错误', u'用户名或密码错误')
            return

        if res.status_code == 200:
            #QtGui.QMessageBox.critical(self, u'错误', u'用户名或密码错误')

    #可拖动边框窗口
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False

if __name__ == '__main__':

        app = QApplication(sys.argv)
        ex = login()
        sys.exit(app.exec())