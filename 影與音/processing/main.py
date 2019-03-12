import sys  #
import face_recognition  #人臉識別模型
import os  #打開文件
from xlutils.copy import copy   #紀錄訊息
import xlrd    # 寫入excel
from os import listdir,getcwd  # 地址 用於打開位置
import cv2  #打開相機
import threading  #多工處理
from PyQt5.QtWidgets import QApplication ,QMainWindow,QMessageBox,QFileDialog,QLabel
from PyQt5.QtCore import QBasicTimer,pyqtSignal,Qt,QSize,QThread
from PyQt5.QtGui import *
from datetime import datetime  #可以獲取當下的時間
from time import time   #計算時間差 計算模型運作時間
from speech_synthesis_ui import Ui_MainWindow2  # 介面２　語音合成
from speech_reco_ui import Ui_MainWindow3
from register import Ui_Dialog2
from setting2_ui import Ui_Dialog #設置介面
from new_ui import Ui_MainWindow  # ＵＩ視窗
from baiduyuyin import baidu_voice,baidu_speech_reco ,ping  #百度語音合成
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import qtawesome
import pyaudio
import wave
from configparser import ConfigParser

conf=ConfigParser()  #
conf.read('config.conf')#讀取設定文件 得到一些參數
CAPTURE_SOURCE=conf.get('image_config','capture_source')
TOLERANCE=float(conf.get('image_config','tolerance'))
SET_SIZE=float(conf.get('image_config','set_size'))
print(CAPTURE_SOURCE,TOLERANCE,SET_SIZE)
t=time()
class MyMainWindow(QMainWindow,Ui_MainWindow):
    signal=pyqtSignal()  #設定初始化（雙開介面）
    signal2=pyqtSignal()
    signal3=pyqtSignal() #設置介面的訊息
    signal4=pyqtSignal()
    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)

        # self.timer_camera = QTimer()  # 需要定時器刷新相機介面
        self.cap = cv2.VideoCapture()
        self.video_btn=0
        self.need_record_name1=([])

# 訊號設置  ------------------------------

        self.left_close.clicked.connect(self.close_window)  #關閉視窗
        self.left_mini.clicked.connect(self.showMinimized)#最小化
        #self.left_visit.clicked.connect(self.showMaximized)  #最大化
        self.pushButton_8.clicked.connect(self.btn_open_cam_click)
        self.pushButton_4.clicked.connect(self.face_recognition_btn) # 人臉識別連結函數 使用face_recogniton_btn
        self.pushButton_5.clicked.connect(self.photo_face)  # 拍照按鈕　連結
        self.pushButton_3.clicked.connect(self.signal_emit) #呼叫視窗２
        self.left_button_6.clicked.connect(self.signal_speech_reco)  #打開語音識別的視窗
        self.pushButton.clicked.connect(self.signal_register)  # 顯示訊息打開文件夾 self.open_file
        self.pushButton_2.clicked.connect(self.open_record)  # 顯示紀錄
        self.pushButton_9.clicked.connect(self.video_announce)  #語音播報
        self.left_button_9.clicked.connect(self.signal_setting)  #設定
        print('mainwindow  is running')
        self.progressbarr_move()
        self.show()
# 訊號對應的函數






    def close_window(self):
        flag2=self.cap.isOpened()
        if flag2==True:
            QMessageBox.information(self,'warning','請先關閉相機在退出')
        else:
            self.close()
    def btn_open_cam_click(self):  #打開相機，按鈕函數


        self.source = 0
        self.t3=time()
        flag2=self.cap.isOpened()  #判斷相機是否被打開 如果被打開flag2就是ture反之就false
        #print(flag2,' flag')
        if flag2 == False:

            self.cap.open(self.source)

            try:
                 self.show_camera()
            except:
                QMessageBox.about(self,'warning','相機不能正常被打開')
        else:
            print('關閉相機')

            # self.timer_camera.stop()
            self.cap.release()
            #
            self.pushButton_8.setText(u'打開相機')
            #self.label_5 = QLabel('\n\nImage and Speech\n\nProcessing')
            self.label_5.setPixmap(QPixmap(""))
            #
            self.label_5.setText('AI智能辨識\n\n富邦創新科技辦公室')
            #
        #self.qingping()
    def face_recognition_btn(self):  # 人臉識別按鈕
        flag2=self.cap.isOpened()
        if flag2== False:
            QMessageBox.information(self, "Warning",
                                self.tr("請先打開相機!"))
        else:
            self.t2=time()
            self.time_step=0
            if self.video_btn==0:
                self.video_btn=1
                self.pushButton_4.setText(u'關閉人臉識別')
                self.show_camera()
                #由于
            elif self.video_btn==1:
                self.video_btn=0
                self.time_step=0
                self.pushButton_4.setText(u'人臉識別')
                self.qingping()
                self.show_camera()
                self.qingping()
    def progressbarr_move(self):
        self.timer = QBasicTimer()
        self.step = 0
        self.timer.start(100, self)
    def timerEvent(self, e):
        if self.step >= 100:

            self.progressBar.setValue(0)
            self.step=0
            self.time_step=1
            return
        if self.video_btn==1 and self.time_step==0:
            self.step = self.step+18
        elif self.video_btn==0:
            self.step=0
        else :
            self.step=self.step
        self.progressBar.setValue(self.step)

    def show_camera(self):  #開啟相機並展現出人臉識別的功能
        #print('show_camera is open ')
        if self.video_btn==0:

            self.pushButton_8.setText(u'關閉相機')

            while (self.cap.isOpened()):

                ret, self.image = self.cap.read()
                QApplication.processEvents()
                show = cv2.resize(self.image, (800, 494))
                show = cv2.cvtColor(show,cv2.COLOR_BGR2RGB)  # 顯示原圖

                self.showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
                self.label_5.setPixmap(QPixmap.fromImage(self.showImage))


            self.label_5.setPixmap(QPixmap(""))
            print('打開相機時間',time()-self.t3)

        elif self.video_btn==1:
            #讀取photo文件中的訊息
             filepath='photo'
             filename_list=listdir(filepath)
             known_face_names=[]
             known_face_encodings=[]
             a=0
             print('2')
             for filename in filename_list:
                a+=1
                QApplication.processEvents()
                if filename.endswith('jpg'):
                    known_face_names.append(filename[:-4])
                    file_str='photo'+'/'+filename
                    a_images=face_recognition.load_image_file(file_str)
                    print(file_str)
                    a_face_encoding = face_recognition.face_encodings(a_images)[0]
                    known_face_encodings.append(a_face_encoding)
             print(known_face_names,a)


             face_locations = []
             face_encodings = []
             face_names =[]
             process_this_frame = True
             while (self.cap.isOpened()):
                 ret, frame = self.cap.read()
                 QApplication.processEvents()

                 small_frame = cv2.resize(frame, (0, 0), fx=SET_SIZE, fy=SET_SIZE)


                 rgb_small_frame = small_frame[:, :, ::-1]
                 #print('4 is running')
                 if process_this_frame:
                     QApplication.processEvents()

                     face_locations = face_recognition.face_locations(rgb_small_frame)
                     face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                     face_names = []
                    # print('5 is  running')
                     for face_encoding in face_encodings:

                         matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=TOLERANCE)

                            #print(matches)
                         name = "Unknown"
                         if True in matches:
                             first_match_index = matches.index(True)
                             name = known_face_names[first_match_index]

                         face_names.append(name)
                 process_this_frame = not process_this_frame
                    # 捕捉到人臉
                 self.set_name=set(face_names)
                 self.set_names=tuple(self.set_name) # 把名字設為一個 集合 把重複的取代掉 再設為tuple 以便於顯示其他訊息和紀錄 調用
                 voice_syn=str()
                 print(self.set_names) #把人臉識別檢測到的人 用set_names 這個集合收集起來
                 self.write_record() #把名字記錄到excel上
                 #self.video_announce()
                 for (top, right, bottom, left), name in zip(face_locations, face_names):
                        #由於我們檢測到的幀被縮放到1/4大小，所以要縮小面位置
                     top *= int(1/SET_SIZE)
                     right *=int(1/SET_SIZE)
                     bottom *= int(1/SET_SIZE)
                     left *= int(1/SET_SIZE)
                        # 矩形框
                     cv2.rectangle(frame, (left, top), (right, bottom), (60, 20, 220), 3)

                     print('face recognition is running')
                        #def draw_text(self, image, pos, text, text_size, text_color)
                     #由於opencv無法顯示漢字之前使用的方法當照片很小時會報錯，此次採用了另一種方法使用PIL進行轉換
                     cv2img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # CV2和PIL中顏色的十六進制碼的儲存順序不同
                     pilimg = Image.fromarray(cv2img)
                     draw = ImageDraw.Draw(pilimg) # 圖片上印出
                     font = ImageFont.truetype("msyh.ttf", 27, encoding="UTF-8") # 參數1：字體文件路徑，參數2：字體大小
                     draw.text((left+10 , bottom ), name, (220, 20, 60), font=font) # 參數1：打印坐標，參數2：文本，參數3：字體顏色，參數4：字體

                    # PIL圖片轉cv2圖片
                     frame = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)

                 self.show_picture()  #調用顯示詳細信息的函數

                 show_video = cv2.resize(frame, (800, 494))
                 show_video = cv2.cvtColor(show_video,cv2.COLOR_BGR2RGB)  # 這裡指的是顯示原圖
                 #opencv讀取圖片的樣式，不能通過Qlabel進行顯示，需要轉換為Qimage QImage（uchar * data，int width，
                 self.showImage = QImage(show_video.data, show_video.shape[1], show_video.shape[0], QImage.Format_RGB888)
                 self.label_5.setPixmap(QPixmap.fromImage(self.showImage))
             print('打開人臉識別所需要的時間',time()-self.t2)


    def photo_face(self):  #實現保存截圖的功能圖片保存在了video_screenshot文件夾裡面名字是根據時間命名
        photo_save_path = os.path.join(os.path.dirname(os.path.abspath('__file__')),
                                       'video_screenshot/')
        # self.time_flag.append(datetime.now().strftime("%Y%m%d%H%M%S")
        self.showImage.save(photo_save_path + datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg")


        QMessageBox.information(self, "Information",
                                self.tr("拍照成功!"))

    def show_picture(self):  #  在人臉識別的右邊顯示識別出來人的詳細信息
         if self.video_btn==1:
             conf = ConfigParser()
             conf.read('information.conf')
             inforation={}
             for names in conf.sections():
                more_infor={}
                for detils in conf.items(names):
                    more_infor[detils[0]]=detils[1]

                inforation[names]=more_infor
             #fr = open（“information.txt”，'rb'）#讀取信息.txt中的信息裡面是錄入信息時寫入的
             infor_dic = inforation   #從information.txt文件中讀取的STR轉換為字
             #fr.close()
             photo_message={0:[self.label_2,self.label_7],1:[self.label,self.label_6],2:[self.label_3,self.label_4]}
             #使用photo_message記錄出現人物數以及需要放置的lable使用下面的遍歷來達到效果
             if len(self.set_names)>3:
                 show_person=3
             else:
                 show_person=len(self.set_names)
             if show_person!=0:
                 for person in range(show_person):
                     try:
                         person_name=self.set_names[person]   #識別出人物的名字
                         person_infor=photo_message[person][0] #信息所對應的標籤lable
                         person_photo=photo_message[person][1] #信息所對應的標籤lable
                         infor_names=infor_dic[person_name] #從txt文檔中獲取的該人的信息
                         name_str='photo//'+person_name+'.jpg'
                         picture=QPixmap(name_str)

                         infor_str='姓名：'+person_name+'                '+'年齡：'+infor_names['年齡']+'                 '+'性別：'+infor_names['性別']+'                 '+'更多信息： '+infor_names['更多信息']

                         person_infor.setText(infor_str)
                         person_infor.setStyleSheet("color:white;font-size:20px;font-family:Microsoft YaHei;")
                         person_infor.setWordWrap(True)  #自適應大小換行
                         person_photo.setPixmap(picture)  #把照片放到label_7上面去
                         person_photo.setScaledContents(True)  #讓照片能夠在標籤上面自適應大小
                     except :
                         QMessageBox.about(self,'warning','請檢察'+person_name+'的訊息')


             if show_person!=3:
                 for empty in range(3)[show_person:]:
                     person_infor=photo_message[empty][0] #信息所對應的lable
                     person_photo=photo_message[empty][1] #照片所對對應的lable
                     person_infor.setText("")
                     person_photo.setPixmap(QPixmap(""))

    def qingping(self):  # 不需要顯示信息的時候把顯示到信息的那部分清除掉在循環中保存了幾次那些lable就不在發生變化了
          self.label_7.setPixmap(QPixmap(""))  # 照片1
          self.label_2.setText("")  # 訊息1
          self.label.setPixmap(QPixmap(""))
          self.label_6.setText("")
          self.label_3.setPixmap(QPixmap(""))
          self.label_4.setText("")


    def signal_emit(self):
        self.signal.emit()#  訊號飛出
        #baidu_voice('歡迎來到富邦創新科技辦公室')
    def signal_speech_reco(self):#進行語音合成頁面的打開
        self.signal2.emit()
    def signal_setting(self):  #發出信號打開新的界面
        self.signal3.emit()
    def signal_register(self):
        self.signal4.emit()
    def open_file(self): #下面這個路徑是絕對路徑無法更改
        file_rute=getcwd()+'\\'+'photo'
        file_name = QFileDialog.getOpenFileName(self,"登入",file_rute)#  打開這個文件夾選擇打開的文件phot裡面的照片是打不開的因為.py文件在外面
        print(file_name)   # file_name 是一個返回值類似於這種（'E：/ Python code / gui / hkvideo / information.txt'，'所有文件（*）'）想要打開需要一些處理
        try:
            file_name2=list(file_name)[0] # 想要的是information，text 所以需要需要對file_name進行處理 需要注意的是打開的是 photo文件夾是向裡面傳照片的再返回出來 填寫information
            t_file=0
            for i in file_name2:
                if i=='/':
                    num=t_file
                t_file=t_file+1
            open_file3=file_name2[(num+1):]
            os.popen(open_file3)
        except:
            QMessageBox.about(self,'warning','無法打開文件')

    def write_record(self):
        #self.need_record_name=set(self.need_record_name)
        print('need_record_names1 is',self.need_record_name1)

        if self.set_name.issubset(self.need_record_name1):  # 如果self.set_names是self.need_record_names 的子集返回ture
            pass                                             # need_record_name1是要寫進excel中的名字信息 set_name是從攝像頭中讀出人臉的tuple形式
        else :
            print('ready to write')
            self.different_name1=self.set_name.difference(self.need_record_name1) # 獲取到self.set_name有 而self.need_record_name 無的名字
            self.need_record_name1=self.set_name.union(self.need_record_name1)  # 把self.need_record_name 變成兩個集合的並集
                                        #different_name是為了獲取到之前沒有捕捉到的人臉 並且再次將need_recore_name1進行更新

            filename='data.xls'            #文件名准備打開excel
            book = xlrd.open_workbook(filename)  # 打開excel
            new_book = copy(book)  # 複製excel
            sheet2 = new_book.get_sheet(0)  # 獲取第一個表格的數據
            sheet0 = book.sheet_by_index(0)
            nrows = sheet0.nrows    # 獲取第一個表格的數據
            print("行數",nrows)
            ncols = sheet0.ncols    #獲取列總數
            print("列數",ncols)
            write_in_data=tuple(self.different_name1)  #上面的different-name1還是一個集合需要變成一個tuple
            names_length=len(write_in_data)      # 獲取到需要寫入表格 人數的長度
            for i in range(names_length):
                #baidu_voice(write_in_data[i])  對進入的人臉進行播報
                str_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                sheet2.write(nrows+i,0,str_time)
                sheet2.write(nrows+i,2,write_in_data[i])
                sheet2.write(nrows+i,1,'相機')
                sheet2.write(nrows+i,3,'使用相機進行測試')

            new_book.save('secondsheet.xls')  # 保存新的excel
            os.remove(filename)  # 刪除舊的excel
            os.rename('secondsheet.xls', filename)  # 將新excel重命名

    def video_announce(self):  #語音播報模塊 點擊之後會對已經記錄下來的人臉名字進行播報
        try:
            need_voice_name=list(self.need_record_name1)
        except:
            need_voice_name=[]
        if need_voice_name!=[]:
            print(need_voice_name)
            if 'Unknown' in need_voice_name :# 把unknown去掉 不進行播報
                need_voice_name.remove('Unknown')
            tuple_voice_name=tuple(need_voice_name)
            if tuple_voice_name==():
                QMessageBox.about(self,'warning','還未識別出這張人臉')
            else:
                voice_str='歡迎'
                for i in tuple_voice_name:
                    voice_str=voice_str+i+' '
                voice_str=voice_str+'的到來'
                baidu_voice(voice_str)  # 歡迎 某 某某 的到來

        else :
            QMessageBox.about(self,'warning',"沒有看到人無法進行播報")


    def open_record(self):
        os.popen('data.xls')# 使用popen會新開一個進程 而使用os.system會佔用原來的進程


class MineWindow(QMainWindow,Ui_MainWindow2): # ui_mainwindow2 是baiduyuyin這個ui裡面的 為了實現雙重界面 使用信號
    def __init__(self,parent=None):
        #super(MineWindow, self).__init__(None, Qt.FramelessWindowHint) # 這句和普通的不一樣 因為可以實現無邊框
        super(MineWindow,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.baidu_voice2)  #合成按鈕 執行合成函數
        self.pushButton_2.clicked.connect(self.close_voice) #退出按鈕 執行退出窗口
        self.pushbutton_close.clicked.connect(self.close)  #關閉窗口
        self.pushbutton_mini.clicked.connect(self.showMinimized)#最小化窗口

    def baidu_voice2(self):
        check_net=ping()
        if check_net==True:
            print ('ping ok')
    #def baidu_voice2(self):
            self.text_Edit = self.textEdit.text()  #獲取 輸入到 textEdit上的字體 並傳遞給語音合成函數
            print(self.text_Edit)
            baidu_voice(self.text_Edit)#  調用百度語音合成的模塊
        else:
            QMessageBox.information(self,'warning',"請檢察您的網路，沒有網路無法使用語音功能")
    def close_voice(self):
        os.system('taskkill /f /im PotPlayerMini64.exe')  #關閉播放音頻的軟件
        self.close()  #關閉界面
class MineWindow2(QMainWindow,Ui_MainWindow3): # ui_mainwindow2 是baiduyuyin這個ui裡面的 為了實現雙重界面 使用信號

    def __init__(self,parent=None):
        #super(MineWindow, self).__init__(None, Qt.FramelessWindowHint)  # 這句和普通的不一樣 因為可以實現無邊框
        super(MineWindow2,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.main_speech_reco)  #合成按鈕 執行合成函數

        self.pushbutton_close.clicked.connect(self.close)  #關閉窗口

        self.pushbutton_mini.clicked.connect(self.showMinimized)#最小化窗口
        self.button_click=0  #第一次點擊 是錄音第二次點擊錄音結束開始識別
        #self.text_label.setText("點擊下面的按鈕開始錄製音頻\n再次點擊停止錄音開始識別") #第二次打開需要再設置不然會出現之前的畫面
        self.recode_switch=1



        self.thread = MyThread() # 創建一個線程
        self.thread.sec_changed_signal.connect(self.get_flames) # 線程發過來的信號掛接到槽：updat

    def get_flames(self,flames):  #進行槽函數的連接 能夠獲取到錄音
        self.flames=flames
        #print(self.flames)
    def main_speech_reco(self):

        if self.button_click==0:
            self.text_label.setText('錄音中... ')
            spin_icon = qtawesome.icon('fa5s.microphone-alt-slash', color='white')
            self.pushButton.setIcon(spin_icon)#設置圖標
            self.pushButton.setIconSize(QSize(50,50))
            #self.pushButton
            self.button_click=1

            self.thread.start()  #開啟線程 進行錄音


        elif self.button_click==1:

            # stream.stop_stream() #結束錄音 進行保存
            # stream.close()
            # p.terminate()
            self.thread.terminate() #結束錄音

            spin_icon = qtawesome.icon('fa5s.microphone-alt', color='white')
            self.pushButton.setIcon(spin_icon)#設置圖標
            self.pushButton.setIconSize(QSize(50,50))

            p = pyaudio.PyAudio()   #進行保存
            wf = wave.open('recode.wav', 'wb')
            wf.setnchannels(1)
            wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
            wf.setframerate(16000)
            wf.writeframes(b''.join(self.flames))
            wf.close()


            self.button_click=0
            speech_recogntion='識別結果：'+baidu_speech_reco()
            self.text_label.setText(speech_recogntion)

class MineWindow3(QMainWindow,Ui_Dialog): # ui_mainwindow2 是baiduyuyin這個ui裡面的 為了實現雙重界面 使用信號

    def __init__(self,parent=None):
        #super(MineWindow, self).__init__(None, Qt.FramelessWindowHint)  # 這句和普通的不一樣 因為可以實現無邊框
        super(MineWindow3,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)  #關閉窗口
        self.pushButton_15.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(self.showMinimized)#最小化窗口
        self.pushButton_14.clicked.connect(self.change_config)
        self.lineEdit_7.setPlaceholderText('0')#攝像頭地址
        self.lineEdit_8.setPlaceholderText(str(SET_SIZE)) #處理圖像大小
        self.lineEdit_9.setPlaceholderText(str(TOLERANCE)) #人臉識別閾值 閾值太低容易造成無法成功識別人臉，太高容易造成人臉識別混淆
        self.lineEdit_10.setPlaceholderText("**************")  #
        self.lineEdit_11.setPlaceholderText("**************")  #
        self.lineEdit_12.setPlaceholderText("**************")
    def change_config(self):
        conf = ConfigParser()
        conf.read('config.conf') #打開配置文件
        button=0
        source_text=self.lineEdit_7.text()
        size_text=self.lineEdit_8.text()
        tolerance_text=self.lineEdit_9.text()
        secretkey_text=self.lineEdit_10.text()
        apiid_text=self.lineEdit_11.text()
        apikey_text=self.lineEdit_12.text()
        if source_text!='':
            conf.set('image_config','capture_source',source_text)
            button=1
        if size_text!='':
            try:
                if float(size_text)>0 and float(size_text)<1:
                    conf.set('image_config','set_size',size_text)
                    button=1
                else:
                    QMessageBox.about(self,'warning','處理圖像大小的值應該取值0-1')
            except:
                QMessageBox.about(self,'warning','處理圖像大小的值 輸入格式有問題')
        if tolerance_text!='':
            try:
                if float(tolerance_text)>0 and float(tolerance_text)<1:
                    conf.set('image_config','tolerance',tolerance_text)
                    button=1
                else:
                    QMessageBox.about(self,'warning','人臉識別閾值應該取值0-1')
            except:
                QMessageBox.about(self,'warning','人臉識別閾值 輸入格式有問題')
        if secretkey_text!='':
            conf.set('speech_config','SECRET_KEY',secretkey_text)
            button=1
        if apiid_text!='':
            conf.set('speech_config','APP_ID',apiid_text)
            button=1
        if apikey_text!='':
            conf.set('speech_config','API_KEY',apikey_text)
            button=1
        conf.write(open("config.conf","w"))
        if button ==1:
            QMessageBox.about(self,'news','配置參數已重置，再次打開即可應用')

class MineWindow4(QMainWindow,Ui_Dialog2): # ui_mainwindow2 是baiduyuyin這個ui裡面的 為了實現雙重界面 使用信號

    def __init__(self,parent=None):
        #super(MineWindow, self).__init__(None, Qt.FramelessWindowHint)  #這句和普通的不一樣 因為可以實現無邊框
        super(MineWindow4,self).__init__(parent)
        self.setupUi(self)
        self.pushButton_5.clicked.connect(self.close_clear)
        self.pushButton_25.clicked.connect(self.close_clear)
        self.pushButton_6.clicked.connect(self.showMinimized)
        self.pushButton_3.clicked.connect(self.search_infor)
        self.pushButton_24.clicked.connect(self.new_register)
        self.conf = ConfigParser()
        self.conf.read('information.conf')
    def close_clear(self):
        linetext=[self.lineEdit,self.lineEdit_13,self.lineEdit_14,self.lineEdit_15,self.lineEdit_16,self.lineEdit_17,
                  self.lineEdit_18,self.lineEdit_20]
        i=0
        for lineedit in linetext:
            lineedit.setPlaceholderText(str(i))
            if i<5 and i>0 :
                lineedit.setPlaceholderText("請輸入訊息")
            if i>=5 and i <=7:
                lineedit.setPlaceholderText('***')
            i=i+1
        self.close()

    def search_infor(self):
        search_name=self.lineEdit.text()
        if search_name in self.conf.sections():
            self.lineEdit_17.setPlaceholderText(self.conf.get(search_name,'年齡'))
            self.lineEdit_18.setPlaceholderText(self.conf.get(search_name,'性別'))
            self.lineEdit_20.setPlaceholderText(self.conf.get(search_name,'更多訊息'))

        else:
            QMessageBox.about(self,'warning','找不到'+search_name+'的訊息')




    def new_register(self):
        button=0  #當都輸入正確的時候寫入 配置文件
        name=self.lineEdit_15.text()
        age=self.lineEdit_13.text()
        sex=self.lineEdit_14.text()
        more_infor=self.lineEdit_16.text()
        button2=0
        search_name=self.lineEdit.text()
        age2=self.lineEdit_17.text()
        sex2=self.lineEdit_18.text()
        mor_infor2=self.lineEdit_20.text()
        if name not in self.conf.sections():
            if name != '':
                self.conf.add_section(name)
                if age == '':
                    age='未知'
                elif str.isdigit(age)!= True:
                    button=1
                    QMessageBox.about(self,'warning','年齡請輸入正確的格式')
                self.conf.set(name,'年齡',str(age))

                if sex == '':
                    sex='未知'
                elif sex!='男' and sex!='女':
                    button=1
                    QMessageBox.about(self,'warning','性別請輸入正確')
                    sex='未知'
                self.conf.set(name,'性別',sex)
                if more_infor == '':
                    more_infor='未知'
                self.conf.set(name,'更多訊息',more_infor)

                if button==0:
                    self.conf.write(open("information.conf","w"))
                    QMessageBox.about(self,'news','請將以'+name+'.jpg為命名的照片放入'+getcwd()+'\\'+'photo路徑下完成註冊')
                elif button == 1:
                    self.conf.remove_section(name)

            else:
                QMessageBox.about(self,'warning','註冊信息必須要輸入姓名')

        else:
            QMessageBox.about(self,'warning',name+'已經註冊過了')

        if age2!=''and str.isdigit(age2)== True:
            self.conf.set(search_name,'年齡',age)
            button2=1
        if sex2!='' and (sex2=='男' or sex2=='女'):
            self.conf.set(search_name,'性別',sex2)
            button2=1
        if mor_infor2!='':
            self.conf.set(search_name,'更多訊息',mor_infor2)
            button2=1
        if button2==1:
            self.conf.write(open("information.conf","w"))
            QMessageBox.about(self,'news',search_name+'的部分訊息已修改')
class MyThread(QThread):  #錄音功能需要使用到 多線程

    sec_changed_signal = pyqtSignal(list) # 信號類型：int

    def __init__(self,  parent=None):
        super().__init__(parent)
        #self.sec = sec # 默認1000秒
    def run(self):
        CHUNK = 1024              #wav文件是由若干個CHUNK組成的，CHUNK我們就理解成數據包或者數據片段。 1024
        FORMAT = pyaudio.paInt16  #這個參數後面寫的pyaudio.paInt16表示我們使用量化位數 16位來進行錄音。
        CHANNELS = 1              #代表的是聲道，這裡使用的單聲道。 1
        RATE = 16000              # 採樣率16k
        #RECORD_SECONDS = Time     #採樣時間
        WAVE_OUTPUT_FILENAME = 'recode22.wav'   #輸出文件名
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
        frames = []

        while True:
             data = stream.read(CHUNK)
             frames.append(data)  #進行錄音
             self.sec_changed_signal.emit(frames)
            # i=i+1
            # print('dd')


if __name__=="__main__" :
    app=QApplication(sys.argv)
    myWin=MyMainWindow()
    Mine=MineWindow()
    speech_reco=MineWindow2()
    setting=MineWindow3()
    register=MineWindow4()
    myWin.signal.connect(Mine.show)  #連接信號
    myWin.signal2.connect(speech_reco.show)
    myWin.signal3.connect(setting.show)
    myWin.signal4.connect(register.show)
    print('打開ui介面所需的時間',time()-t)
    sys.exit(app.exec_())
