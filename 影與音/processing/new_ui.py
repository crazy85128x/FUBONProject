# coding:utf-8

from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import qtawesome
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1096,800)
    # def __init__(self):
    #     super().__init__()
    #     self.init_ui()
    #
    # def init_ui(self):
    #     self.setFixedSize(1096,800)

        self.main_widget = QtWidgets.QWidget(MainWindow)  # 創建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 創建主部件的網格佈局
        self.main_widget.setLayout(self.main_layout)  # 設置窗口主部件佈局為網格佈局

        self.left_widget = QtWidgets.QWidget(MainWindow)  # 創建左側部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 創建左側部件的網格佈局層
        self.left_widget.setLayout(self.left_layout) # 設置左側部件佈局為網格

        self.right_widget = QtWidgets.QWidget(MainWindow) # 創建右側部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout) # 設置右側部件佈局為網格

        self.main_layout.addWidget(self.left_widget,0,0,12,2) # 左側部件在第0行第0列，佔8行3列
        self.main_layout.addWidget(self.right_widget,0,2,12,10) # 右側部件在第0行第3列，佔8行9列
        MainWindow.setCentralWidget(self.main_widget) # 設置窗口主部件
        #在左側菜單模塊中，繼續使用網格對部件進行佈局。在左側菜單的佈局中添加按鈕部件QPushButton()左側菜單的按鈕、
        # 菜單列提示和整個窗口的最小化和關閉按鈕。
        #在MainUi()類的init_ui()方法中，使用如下代碼實例化創建按鈕：



        self.left_close = QtWidgets.QPushButton("") # 關閉按鈕
        self.left_visit = QtWidgets.QPushButton("") # 空白按鈕
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按鈕

        self.left_label_1 = QtWidgets.QPushButton("IMAGE")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("VOICE")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("ELSE")
        self.left_label_3.setObjectName('left_label')



        self.pushButton_8 = QtWidgets.QPushButton(qtawesome.icon('fa5s.video',color='white'),"打開相機")
        self.pushButton_8.setObjectName('left_button')
        self.pushButton_5 = QtWidgets.QPushButton(qtawesome.icon('fa5s.camera',color='white'),"拍照")
        #self.pushButton_5.setIconSize(QtCore.QSize(25,25))
        self.pushButton_5.setObjectName('left_button')
        self.pushButton_4 = QtWidgets.QPushButton(qtawesome.icon('fa5s.eye',color='white'),"人臉識別")
        self.pushButton_4.setObjectName('left_button')
        self.pushButton_9 = QtWidgets.QPushButton(qtawesome.icon('fa5s.volume-up',color='white'),"語音播報")
        self.pushButton_9.setObjectName('left_button')
        self.pushButton_3 = QtWidgets.QPushButton(qtawesome.icon('fa5s.microphone',color='white'),"語音合成")
        self.pushButton_3.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa5s.microphone-alt',color='white'),"語音識別")
        self.left_button_6.setObjectName('left_button')
        self.pushButton = QtWidgets.QPushButton(qtawesome.icon('fa5s.folder-open',color='white'),"註冊")
        self.pushButton.setObjectName('left_button')
        self.pushButton_2 = QtWidgets.QPushButton(qtawesome.icon('fa5s.file-excel',color='white'),"查詢紀錄")
        self.pushButton_2.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa5s.sliders-h',color='white'),"設置")
        self.left_button_9.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")

        # 在這裡，我們使用qtawesome這個第三方庫來實現按鈕中的Font Awesome字體圖標的顯示。
        # 然後將創建的按鈕添加到左側部件的網格佈局層中：

        self.left_layout.addWidget(self.left_close, 0, 0,1,1)
        self.left_layout.addWidget(self.left_mini, 0, 2,1,1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1,1,0,1,3)
        self.left_layout.addWidget(self.pushButton_8, 2, 0,1,3)
        self.left_layout.addWidget(self.pushButton_5, 3, 0,1,3)
        self.left_layout.addWidget(self.pushButton_4, 4, 0,1,3)
        self.left_layout.addWidget(self.left_label_2, 5, 0,1,3)
        self.left_layout.addWidget(self.pushButton_9, 6, 0,1,3)
        self.left_layout.addWidget(self.pushButton_3, 7, 0,1,3)
        self.left_layout.addWidget(self.left_button_6, 8, 0,1,3)
        self.left_layout.addWidget(self.left_label_3, 9, 0,1,3)
        self.left_layout.addWidget(self.pushButton, 10, 0,1,3)
        self.left_layout.addWidget(self.pushButton_2, 11, 0,1,3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)


        #進行設置右側控件
        self.label_5 = QtWidgets.QLabel('\n\nAI智能辨識\n富邦創新科技辦公室\n')
        self.label_5.setAlignment(Qt.AlignCenter)
        # self.label_5.setFont(QFont("Roman times",20,QFont.Bold))

        self.label_5.setStyleSheet("QLabel{background:darkgray;}"
                   "QLabel{color:white;font-size:80px;font-weight:bold;font-family:Roman times;}"
                  )

        self.label_5.setObjectName('lable_')
        self.label_7 = QtWidgets.QLabel('')
        self.label_7.setObjectName('lable_')
        self.label_2 = QtWidgets.QLabel('')
        self.label_2.setObjectName('lable_')
        self.label_6 = QtWidgets.QLabel('')
        self.label_6.setObjectName('lable_')
        self.label = QtWidgets.QLabel('')
        self.label.setObjectName('lable_')
        self.label_4 = QtWidgets.QLabel('')
        self.label_4.setObjectName('lable_')
        self.label_3 = QtWidgets.QLabel('')
        self.label_3.setObjectName('lable_')

        list_label=[self.label_7,self.label_2,self.label_6,self.label_4,self.label_3,self.label]




        self.progressBar = QtWidgets.QProgressBar()  #
        self.progressBar.setValue(100)
        self.progressBar.setFixedHeight(11)  # 設置進度條高度

        #self.right_lable_layout.addWidget(self.progressBar,0,0,1,1)
        # self.right_lable_layout.addWidget(self.label_5,0,1,1,8)
        # self.right_layout.addWidget(self.right_lable_widget,0,0,1,9)
        self.right_layout.addWidget(self.progressBar,0,0,1,8)  #進度條
        self.right_layout.addWidget(self.label_5,1,0,3,8) #顯示攝像頭畫面的label
        self.right_layout.addWidget(self.label_7,5,0,)
        self.right_layout.addWidget(self.label_2,5,1,)
        self.right_layout.addWidget(self.label_6,5,2,)
        self.right_layout.addWidget(self.label_4,5,4,)
        self.right_layout.addWidget(self.label_3,5,5,)
        self.right_layout.addWidget(self.label,5,3,)

        self.label_5.setMinimumSize(QtCore.QSize(894, 560))
        self.label_5.setMaximumSize(QtCore.QSize(894, 560))
        for labe_size in list_label:
            labe_size.setMinimumSize(QtCore.QSize(149, 210))
            labe_size.setMaximumSize(QtCore.QSize(149, 210))

        # self.label_5.setPixmap(QPixmap('face3.jpg'))  #把照片放到label_7上面去
        # self.label_5.setScaledContents(True)  #讓照片能夠在label上面自適應大小
        # for lables in list_label:
        #     lables.setPixmap(QPixmap('shishi.jpg'))
        #     lables.setScaledContents(True)

 #----------------------------------------美化
        self.left_close.setFixedSize(30, 30) # 設置關閉按鈕的大小
        self.left_visit.setFixedSize(30, 30)  # 設置按鈕大小
        self.left_mini.setFixedSize(30, 30) # 設置最小化按鈕大小

        #然後，通過setStyleSheet()方法，設置按鈕部件的QSS樣式，在這裡，左側按鈕默認為淡綠色，
        # 鼠標懸浮時為深綠色；中間按鈕默認為淡黃色，鼠標懸浮時為深黃色；右側按鈕默認為淺紅色，鼠標懸浮時為紅色。
        # 所以它們的QSS樣式設置如下所示：
        self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:15px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:15px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:15px;}QPushButton:hover{background:green;}''')
    #左側菜單按鈕
    # 因為最後的圖形界面中，左側的部件背景是灰色的，
    # 所以我們需要將左側菜單中的按鈕和文字顏色設置為白色，並且將按鈕的邊框去掉，在left_widget中設置qss樣式為：
        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;padding-left:5px;
                    height:35px;
                    font-size:15px;
                    padding-right:10px;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:20px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }

            QWidget#left_widget{
                background:Gray;

                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
            QPushButton#left_button:hover{ color:white;
                    border:2px solid #F3F3F5;
                    border-radius:15px;
                    background:black;}
        ''')

        self.right_widget.setStyleSheet('''
                QWidget#right_widget{
                    color:#232C51;
                    background:darkGray;
                    border-top-right-radius:10px;
                    border-bottom-right-radius:10px;

                }

            ''')
        #進度條 美化
        self.progressBar.setStyleSheet('''
            QProgressBar::chunk {
                background-color: darkgray;
            }
        ''')
        self.progressBar.setTextVisible(False)  # 不顯示進度條文字
        MainWindow.setWindowOpacity(1) # 設置窗口透明度
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 設置窗口背景透明
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隱藏邊框

        self.right_layout.setContentsMargins(0,0,2,1)  #設置右邊佈局 左右間距為0 去掉間隙 左 上 右 下
        self.main_layout.setSpacing(0) #们通过设置布局内部件的间隙来把那条缝隙去除掉：
        self.right_layout.setSpacing(0)
        self.left_layout.setSpacing(0)
    #下面這三個函數通過重寫 能夠實現隱藏邊框進行拖動窗口
        MainWindow.setWindowTitle("人臉識別")# 設置標題
        MainWindow.setWindowIcon(QIcon('Amg.jpg'))#設置logo



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




# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     gui = MainUi()
#     gui.show()
#     sys.exit(app.exec_())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(widgets)
    widgets.show()
    sys.exit(app.exec_())