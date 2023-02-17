# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 22:35:57 2023

@author: 10858
"""
import datetime,os,time
from PyQt5.QtWidgets import *
import sys
class QTextEditDemo(QWidget) :
    def __init__(self):
        super(QTextEditDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('定时打开网站')#标题
        self.resize(300, 400)
        self.textEdit=QTextEdit()#文本编辑器
        self.hour=QPushButton("获取小时数时")#获取小时按钮
        self.minute=QPushButton("获取分")#获取分钟按钮
        self.web=QPushButton("获取打开的网站")#打开网站的按钮
        self.dinshi=QPushButton("定时")#定时按钮
        layout = QVBoxLayout()#准备装载
        layout.addWidget(self.textEdit)#添加文本编辑器
        layout.addWidget(self.hour)
        layout.addWidget(self.minute)
        layout.addWidget(self.web)
        layout.addWidget(self.dinshi)
        self.setLayout(layout)
        self.hour.clicked.connect(self.onClick_hour)
        self.minute.clicked.connect(self.onClick_minute)
        self.web.clicked.connect(self.onClick_web)
        self.dinshi.clicked.connect(self.onClick_dinshi)
    def onClick_hour(self):
        global inner_hour
        inner_hour=int(self.textEdit.toPlainText())
    def onClick_minute(self):
        global inner_minute
        inner_minute=int(self.textEdit.toPlainText())
    def onClick_web(self):
        global inner_web
        inner_web=self.textEdit.toPlainText()
    def onClick_dinshi(self):
        try:
            while True:
                time.sleep(5)
                nowTime=datetime.datetime.now()
                hour = nowTime.hour
                minu = nowTime.minute
                if hour == inner_hour and (minu == inner_minute):
                    os.system("start "+inner_web)
                    break
        except:
            self.textEdit.setPlainText("重新输入一遍")
"""out_hour=int(input("请输入几点打开"))
out_time=int(input("请输入几分打开"))
while True:
    time.sleep(5)
    nowTime=datetime.datetime.now()
    hour=nowTime.hour
    minu=nowTime.minute
    if hour==out_hour and (minu==out_time):
        os.system("start www.baidu.com")
        break
while True:
    time.sleep(5)
    nowTime=datetime.datetime.now()
    hour = nowTime.hour
    minu = nowTime.minute
    if hour == self.inner_hour and (minu == self.inner_minute):
        os.system("start"+inner_web)
        break    
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTextEditDemo()
    main.show()
    sys.exit(app.exec_())