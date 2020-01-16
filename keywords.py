from PyQt5.Qt import *
from PyQt5 import QtGui
import random
import win32gui
import win32api,win32con
import sys
import json
import requests
import os



class autoUi(QWidget):

    def __init__(self):
        super(autoUi, self).__init__()
        with open("login.qss","r") as f:
            qApp.setStyleSheet(f.read())
        self.labelauto = QLabel(self)
        self.labelauto.setObjectName('labelbgs')
        self.labelauto.setWindowTitle('sss')
        self.labelauto.setFixedSize(397,297)
        self.labelauto.setObjectName('labelbgs')
        self.labelauto.resize(381, 251)
        #设置词数上限
        self.keywordMax = QLineEdit(self)
        self.keywordMax.setPlaceholderText('1000000')
        self.keywordMax.setObjectName('userInput')
        self.keywordMax.setFont(QFont('Microsoft YaHei' , 18 , 75))
        self.keywordMax.move(138,95)
        #标题
        self.textMax = QLabel(self)
        self.textMax.setFont(QFont('Microsoft YaHei' , 18,75))
        self.textMax.move(10,95)
        self.textMax.setText("设置上限")
        self.textMax.setObjectName('setAuto_textMax')
        #检测词数
        self.keywordTest = QLineEdit(self)
        self.keywordTest.setEnabled(False)
        self.keywordTest.setObjectName('userInput')
        self.keywordTest.setFont(QFont('Microsoft YaHei',18,75))
        self.keywordTest.move(138,160)
        #标题检测
        self.testIng = QLabel(self)
        self.testIng.setFont(QFont('Microsoft YaHei' , 18,75))
        self.testIng.move(10,160)
        self.testIng.setText("检测词数")
        self.testIng.setObjectName('setAuto_textMax')
class setTask(QWidget):

    def __init__(self):

        super(setTask, self).__init__()
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
        self.autoKeywords = QPushButton(self)
        self.autoKeywords.setObjectName('Minimum')
        self.autoKeywords.setFont(QFont("Microsoft YaHei" , 15, 75))
        self.autoKeywords.resize(150,150)
        self.autoKeywords.move(70,100)
        self.autoKeywords.setCursor(QCursor(Qt.PointingHandCursor))
        # a = autoUi()
        # autoKeywords.clicked.connect(a.show())
        self.autoKeywords.setText('自动检测关键词')

        #手动导入关键词
        manualKeywords = QPushButton(self)
        manualKeywords.setObjectName('Minimum')
        manualKeywords.setFont(QFont("Microsoft YaHei" , 15, 75))
        manualKeywords.resize(150,150)
        manualKeywords.move(300,100)
        manualKeywords.setCursor(QCursor(Qt.PointingHandCursor))
        # manualKeywords.clicked.connect(self.showMinimized)
        manualKeywords.setText('手动导入关键词')

class web_keywords(QWidget):


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
    ex.show()
    auto = autoUi()
    ex.autoKeywords.clicked.connect(auto.show)
    sys.exit(app.exec())