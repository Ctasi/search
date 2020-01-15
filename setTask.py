from PyQt5.Qt import *
from PyQt5 import QtGui
import random
import win32gui
import win32api,win32con
import sys
import json
import requests
import os

class setTask(QWidget):

    def __init__(self):

        super().__init__()
        self.setup_ui()

    def check_file(self):
        if not os.path.exists('hydata'):
            os.makedirs('hydata')
        filename = 'hydata/{}'.format(self.filename)
        if not os.path.exists(filename):
            os.makedirs(filename)
        tparms['filedir'] = filename

    def setup_ui(self):
        with open("login.qss",'r') as f:
            qApp.setStyleSheet(f.read())
        labelbg = QLabel(self)
        labelbg.setWindowTitle('sss')
        labelbg.setObjectName('labelbgs')
        labelbg.resize(531, 329)
        #隐藏边框
        self.setWindowFlags(Qt.FramelessWindowHint)

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

        #自动检测关键词
        autoKeywords = QPushButton(self)
        autoKeywords.setObjectName('Minimum')
        autoKeywords.setFont(QFont("Microsoft YaHei" , 15, 75))
        autoKeywords.resize(150,150)
        autoKeywords.move(70,100)
        autoKeywords.setCursor(QCursor(Qt.PointingHandCursor))
        autoKeywords.clicked.connect(self.autoUi)
        autoKeywords.setText('自动检测关键词')

        #手动导入关键词
        manualKeywords = QPushButton(self)
        manualKeywords.setObjectName('Minimum')
        manualKeywords.setFont(QFont("Microsoft YaHei" , 15, 75))
        manualKeywords.resize(150,150)
        manualKeywords.move(300,100)
        manualKeywords.setCursor(QCursor(Qt.PointingHandCursor))
        # manualKeywords.clicked.connect(self.showMinimized)
        manualKeywords.setText('手动导入关键词')

        self.show()


    def autoUi(self):
        labelauto = QWidget()
        # labelauto.setParent(self.labelbg)
        labelauto.setWindowTitle('sss')
        labelauto.resize(800,300)
        labelauto.setObjectName('labelbgs')
        labelauto.show()
        print(1)

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
    ex = setTask()
    ex.autoUi()
    sys.exit(app.exec())