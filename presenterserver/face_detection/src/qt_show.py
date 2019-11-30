# coding=utf-8

from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic.properties import QtGui


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import numpy as np
import face_detection.src.global_manager as global_var


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.app = None
        self.mainWidget = None
        self.layout = QGridLayout(self)
        self.imagebox = QLabel('no result')
        self.imagesize = 0
        self.currentsize=0
        self.alldata=b''
        self.initializecomponent()

    def img2pixmap(self, image_data):
        # image = QImage(image, image.shape[1], image.shape[0], image.shape[1] * 3, QImage.Format_RGB888)
        # pixmap = QPixmap(image)
        image = QImage.fromData(image_data)
        pixmap = QPixmap.fromImage(image)
        return pixmap

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def settitle(self, data):
        self.setWindowTitle(data)

    # 初始化UI界面控件
    def initializecomponent(self):
        self.setWindowTitle("showserver-Current Client Count is : 0")
        self.setFixedSize(600, 600)  # 设置窗体大小
        self.imagebox.setFixedSize(600, 600)  # 设置尺寸大小
        self.imagebox.setAlignment(QtCore.Qt.AlignCenter)  # 中心对齐
        self.imagebox.setStyleSheet('QWidget{background-color:rgb(0,255,0)}')  # 设置背景颜色
        self.layout.addWidget(self.imagebox)  # 添加控件

def run():
    global_var.qt_app = QApplication(sys.argv)  # 新建QApplication实例
    global_var.qt_mainWidget = MainWidget()  # 实例化一个类，继承自QWidget，也可以继承QMainWindow
    global_var.qt_mainWidget.show()  # 显示窗口
    sys.exit(global_var.qt_app.exec_())  # 进入消息主循环,sys.exit可以不写但是关闭窗口不会退出进程


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 新建QApplication实例
    mainWidget = MainWidget()  # 实例化一个类，继承自QWidget，也可以继承QMainWindow
    mainWidget.show()  # 显示窗口
    sys.exit(app.exec_())  # 进入消息主循环,sys.exit可以不写但是关闭窗口不会退出进程
