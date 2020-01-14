from PyQt5.Qt import *
from PyQt5 import QtGui
import random
import win32gui
import win32api,win32con
import sys
import json
import requests
import setTask

tparms = {'username': '', 'password': '', 'count': 0, 'update_url': 'http://{}/admin/api/saveKeyword', 'code': '', 'company': '', 'filedir': '', 'news_list': [], 'admin_id': ''}

class login(QWidget):

    def __init__(self):
        # 调用父级模块
        super().__init__()
        self.setup_ui()
    # UI界面方法
    def setup_ui(self):
        with open("login.qss",'r') as f:
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
        btnMinimum.move(430,0)
        btnMinimum.setCursor(QCursor(Qt.PointingHandCursor))
        btnMinimum.clicked.connect(self.showMinimized)
        btnMinimum.setText('最小化')
        # #最大化
        # btnBig = QPushButton(self)
        # btnBig.setObjectName('big')
        # btnBig.resize(50,20)
        # btnBig.move(430,0)
        # btnBig.setCursor(QCursor(Qt.PointingHandCursor))
        # btnBig.clicked.connect(self.showMaximized)
        # btnBig.setText('最大化')
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
        btnLogin.setStyleSheet("QPushButton:hover{border-image: url(bg.jpg)}")
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
            # self.QMessageBox.critical(self, u'错误', u'用户名或密码错误')
            reply = QMessageBox.information(self,
                                            "提示",
                                            "用户名或密码错误",
                                            QMessageBox.Yes)
            return

        if res.status_code == 200:
            content = json.loads(res.content)
            if content['status'] == 1:
                tparms['username'] = username
                # tparms['password'] = password
                tparms['admin_id'] = content['data']['admin_id']
                tparms['company'] = content['data']['company']
                tparms['code'] = content['data']['code']
                tparms['update_url'] = 'http://api.yzt-tools.com/api/wtx/report/saveKeyword'
                try:
                    news_list = []
                    yuming_url = 'http://tidan.yzt-tools.com/admin/api/getMuluUrl'
                    res = json.loads(requests.get(yuming_url, data={"type": 1}).content)['data']
                    for i in res:
                        if 'http' in i:
                            i = i.replace('http://', '').replace('www', '').replace('https://', '')
                        news_list.append(i)
                    tparms['news_list'] = list(set(news_list))
                except:
                    tparms['news_list'] = []
                QMessageBox.information(self,
                                        "提示",
                                        "登录成功",
                                        QMessageBox.Yes)
                self.close()
            else :

                reply = QMessageBox.information(self,
                                                "提示",
                                                "用户名或密码错误",
                                                QMessageBox.Yes)
            return

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