from PyQt5.Qt import *
from PyQt5 import QtGui
import random
import win32gui
import win32api,win32con
import sys
import json
import requests

class setTask(QWidget):

    def __init__(self):

        super().__init__()
        self.setup_ui()
    def setup_ui(self):
        labelbg = QLabel(self)
        labelbg.setWindowTitle('sss')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = setTask()
    sys.exit(app.exec())
