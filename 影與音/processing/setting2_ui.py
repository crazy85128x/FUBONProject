# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting2_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
import qtawesome
import sys
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(470, 671)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 31, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 20, 31, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 20, 31, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(0, 50, 467, 201))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_6.addWidget(self.lineEdit_9, 2, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_6.addWidget(self.lineEdit_8, 3, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_7.setObjectName("lineEdit")
        self.gridLayout_6.addWidget(self.lineEdit_7, 1, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.pushButton_8.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton_8, 2, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.pushButton_9.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_9.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton_9, 1, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.pushButton_11.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton_11, 3, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_6.addWidget(self.pushButton_10, 0, 0, 1, 2)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(-4, 247, 471, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_20 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_20.setObjectName("pushButton")
        self.gridLayout_7.addWidget(self.pushButton_20, 3, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_7.addWidget(self.lineEdit_10, 3, 1, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_7.addWidget(self.lineEdit_11, 2, 1, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_21.setObjectName("pushButton")
        self.gridLayout_7.addWidget(self.pushButton_21, 2, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_7.addWidget(self.lineEdit_12, 1, 1, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_22.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_22.setObjectName("pushButton")
        self.gridLayout_7.addWidget(self.pushButton_22, 1, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_7.addWidget(self.pushButton_12, 0, 0, 1, 2)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(-12, 448, 481, 231))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_13 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_5.addWidget(self.pushButton_13)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_23 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_23.setObjectName("pushButton")
        self.gridLayout_8.addWidget(self.pushButton_23, 1, 0, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_24.setObjectName("pushButton")
        self.gridLayout_8.addWidget(self.pushButton_24, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_8.addWidget(self.label_4, 1, 1, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_25.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_25.setObjectName("pushButton")
        self.gridLayout_8.addWidget(self.pushButton_25, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 2, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_14 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_14.setMinimumSize(QtCore.QSize(20, 0))
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_2.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_15.setMinimumSize(QtCore.QSize(20, 0))
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_2.addWidget(self.pushButton_15)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", ""))
        self.pushButton_2.setText(_translate("Dialog", ""))
        self.pushButton_3.setText(_translate("Dialog", ""))
        self.pushButton_8.setText(_translate("Dialog", "人臉辨識"))
        self.pushButton_9.setText(_translate("Dialog", "相機位置"))
        self.pushButton_11.setText(_translate("Dialog", "處理圖像大小"))
        self.pushButton_10.setText(_translate("Dialog", "圖片相關設置"))
        self.pushButton_20.setText(_translate("Dialog", "SECRET_KEY"))
        self.pushButton_21.setText(_translate("Dialog", "APP_ID"))
        self.pushButton_22.setText(_translate("Dialog", "API_KEY"))
        self.pushButton_12.setText(_translate("Dialog", "語音相關設置"))
        self.pushButton_13.setText(_translate("Dialog", "專案團隊"))
        self.pushButton_23.setText(_translate("Dialog", "YouTube"))
        self.pushButton_24.setText(_translate("Dialog", "信箱"))
        self.label_4.setText(_translate("Dialog", "https://www.youtube.com/channel/UCKSc5DQ5YHy4RNv_-ief27A"))
        self.pushButton_25.setText(_translate("Dialog", "黑客ＦＢ"))
        self.label_5.setText(_translate("Dialog", "https://www.facebook.com/profile.php?id=100009698772103"))
        self.label_6.setText(_translate("Dialog", "jason85128x@gmail.com"))
        self.pushButton_14.setText(_translate("Dialog", "套用"))
        self.pushButton_15.setText(_translate("Dialog", "退出"))
#------------------------------------美化设置
        self.pushButton.setFixedSize(30, 30) # 设置关闭按钮的大小
        self.pushButton_2.setFixedSize(30, 30)  # 设置按钮大小
        self.pushButton_3.setFixedSize(30, 30) # 设置最小化按钮大小

        #然後，通過setStyleSheet()方法，設置按鈕部件的QSS樣式，在這裡，左側按鈕默認為淡綠色，
        # 鼠標懸浮時為深綠色；中間按鈕默認為淡黃色，鼠標懸浮時為深黃色；右側按鈕默認為淺紅色，鼠標懸浮時為紅色。
        # 所以它們的QSS樣式設置如下所示：
        self.pushButton.setStyleSheet('''QPushButton{background:#F76677;border-radius:15px;}QPushButton:hover{background:red;}''')
        self.pushButton_2.setStyleSheet('''QPushButton{background:#F7D674;border-radius:15px;}QPushButton:hover{background:yellow;}''')
        self.pushButton_3.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:15px;}QPushButton:hover{background:green;}''')

        Dialog.setWindowOpacity(0.9) # 設置窗口透明度
        #Ui_Dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 設置窗口背景透明
        Dialog.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隱藏邊框
        pe = QPalette()
        Dialog.setAutoFillBackground(True)
        pe.setColor(QPalette.Window,Qt.lightGray)  #設置背景色
        #pe.setColor(QPalette.Background,Qt.blue)
        Dialog.setPalette(pe)

        spin_icon = qtawesome.icon('fa5s.sliders-h', color='black')
        #self.pushButton.setIcon(spin_icon)#設置圖標
        Dialog.setWindowIcon(spin_icon)
        self.gridLayoutWidget_5.setStyleSheet('''QPushButton{border:none;color:white;padding-left:5px;
                            height:50px;font-size:20px;font-weight:500;padding-right:10px;font-family: "Helvetica Neue"}
                             QPushButton:hover{border-right:4px solid black;font-weight:500;
                            }''')
        self.verticalLayoutWidget_4.setStyleSheet('''QPushButton{border:none;color:white;padding-left:5px;
                            height:50px;font-size:20px;font-weight:500;padding-right:10px;font-family: "Helvetica Neue";}
                            QLabel{ font-size:20px;
                        font-weight:600;color:white;
                        font-family: "Helvetica Neue";}QPushButton:hover{color:white;border:2px solid #F3F3F5;
                                border-radius:10px;
                                background:LightGray;
                            } ''')
        self.layoutWidget.setStyleSheet('''QPushButton{border:none;color:white;padding-left:5px;
                            height:50px;font-size:20px;font-weight:500;padding-right:10px;font-family: "Helvetica Neue"}
                            QPushButton:hover{border-right:4px solid black;font-weight:500;
                            } ''')



        big_pushbutton=[self.pushButton_10,self.pushButton_12,self.pushButton_13]
        for bigpushbutton in big_pushbutton:
            bigpushbutton.setStyleSheet('''QPushButton{
                    border:none;
                    border-bottom:2px solid white;
                    font-size:30px;
                    font-weight:700;
                    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                } QPushButton:hover{color:white;border:0px solid #F3F3F5;
                                border-radius:0px;
                                background:LightGray;
                            }''')

        line_edit=[self.lineEdit_7,self.lineEdit_8,self.lineEdit_9,self.lineEdit_10,self.lineEdit_11,self.lineEdit_12]
        for lineedit in line_edit:
            lineedit.setStyleSheet('''QLineEdit{
                        border:2px solid gray;
                        font-size:13px;font-weight:700;
                    font-family: "Helvetica Neue";
                        border-radius:15px;
                        height:30px;
                         }''')
            lineedit.setAlignment(Qt.AlignCenter)  #输入的字放到中间
        list_below_button=[self.pushButton_14,self.pushButton_15]
        for below_button in list_below_button:
            below_button.setStyleSheet(''' QPushButton{
                    color:black;
                    border:none;
                    border-bottom:2px solid white;
                    font-size:30px;
                    font-weight:700;
                    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                } QPushButton:hover{color:black;
                            } ''')

        self.lineEdit_7.setPlaceholderText("默認0,ip攝像頭查詢rtsp地址放入")#攝像頭地址
        self.lineEdit_8.setPlaceholderText("默認0.33,太高處理慢，太低識別效果不好") #處理圖像大小
        self.lineEdit_9.setPlaceholderText("默認0.42,太低無法識別，太高容易混淆") #人臉識別閾值 閾值太低容易造成無法成功識別人臉，太高容易造成人臉識別混淆
        self.lineEdit_10.setPlaceholderText("找不到這三個值的，百度ai可以解決")  #識別語音類型
        self.lineEdit_11.setPlaceholderText("進入百度ai，創建語音類應用，應用列表中即可查看")  #語音合成語速 spd 選填 語速，取值0-15，默認為5中語速
        self.lineEdit_12.setPlaceholderText("語音類功能調用的百度的api接口，可以免費註冊，此為永久性")  #語音合成類型 發音人選擇, 0為普通女聲，1為普通男生，3為情感合成-度逍遙，4為情感合成-度丫丫，默認為普通女聲
    #  能夠移動 無邊框界面
    def mousePressEvent(self, event):
        if event.button()==QtCore.Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #獲取鼠標相對窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  #更改鼠標圖標

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(widgets)
    widgets.show()
    sys.exit(app.exec_())