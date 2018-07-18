import sys
from PyQt5.QtWidgets import *
from ui import *
from businfo import *
from PyQt5.QtGui import *
import os
import threading
import time


class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.model=QtGui.QStandardItemModel(4,3)
        self.model.setHorizontalHeaderLabels(timetable_index)
        self.table_line.setModel(self.model)
        self.table_line.horizontalHeader().setStretchLastSection(True)
        self.table_line.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.num_1.setMinimum(1)
        self.num_2.setMinimum(1)
        self.lock=threading.Lock()
        self.work1=0
        self.work2=0
        self.timetable={"10001":[10001,"06:10",45,50],
	 "10002":[10002,"13:30",78,65],
	 "10003":[10003,"22:15",50,55],

	 "20001":[20001,"07:13",44,55],
	 "20002":[20002,"13:35",65,60],
	 "20003":[20003,"22:15",53,35],
	 
	 "30001":[30001,"08:25",56,40],
	 "30002":[30002,"11:45",98,50],
	 "30003":[30003,"21:45",34,60]}
        self.thread1 = threading.Thread(target=self.sale_tic1,args=())
        self.thread2 = threading.Thread(target=self.sale_tic2,args=())
        self.thread1.start()
        self.thread2.start()

    def change_table(self,i):
        roadname=roadlines[i]
        busnums=LinesInfo[roadname]
        self.select_1.clear()
        self.select_2.clear()
        for row in range(3):
            busnum_name=busnums[row]
            self.select_1.addItem(busnum_name)
            self.select_2.addItem(busnum_name)
            buscc=self.timetable[busnum_name]
            for column in range(4):
                Item=buscc[column]
                Item_info=QStandardItem(str(Item))
                self.model.setItem(row,column,Item_info)
        self.table_line.setModel(self.model)
        #self.showresult("Had been updated")
        

    def get_ticket1(self):
        self.numBus=self.getBusName(1)
        self.numTic=self.getTicNum(1)
        #global work1
        self.work1=1
        #self.showresult("get NUM tICK")
        time.sleep(1)
        if e[0]==1:
            self.showresult("you get ticket from 1")
        if e[0]==0:
            self.showresult("no enough tickit")
        self.change_table(self.choocie_line.currentIndex())

    def get_ticket2(self):
        self.numBus=self.getBusName(2)
        self.numTic=self.getTicNum(2)
        #global work2
        self.work2=1
        #self.showresult("get NUM tICK")
        time.sleep(1)
        if e[0]==2:
            self.showresult("you get ticket from 2")
        if e[0]==0:
            self.showresult("no enough tickit")
        self.change_table(self.choocie_line.currentIndex())

    def getBusNum(self,i):
        #self.showresult("you are selecting bus num ")
        pass

    def showresult(self,strr):
        self.show_result.setText(str(strr))

    def getBusName(self,i):
        #self.showresult("you are selecting bus num ")
        if i==1 :
            return self.select_1.currentText()
        else:
            return self.select_2.currentText()

    def getTicNum(self,i):
        if i==1:
            return self.num_1.value()
        if i==2:
            return self.num_2.value()

    def sale_tic1(self):
        #global work1
        print(str(self.work1))
        if self.work1==1:
            e[0]=1
            self.sale_tic()
            self.work1=0
            #self.showresult("you get ticket from 1")
        time.sleep(1)
        self.sale_tic1()

    def sale_tic2(self):
        #global work2
        print(str(self.work2))
        if self.work2==1:
            e[0]=2
            self.sale_tic()
            self.work2=0
            #self.showresult("you get ticket from 2")
        time.sleep(1)
        self.sale_tic2()

    def sale_tic(self):
        self.lock.acquire()
        print("sale_tic")
        lllinfo=self.timetable[self.numBus]
        if lllinfo[3]<self.numTic:
            #self.showresult("no enough tickit")
            e[0]=0
            e[1]=self.numTic
        else:
            lllinfo[3] -= self.numTic
            #intt=lllinfo[3]
            #imetable[self.numBus][3]=intt
            #timetable[self.numBus]=lllinfo[3]
            e[1]=self.numTic
            #self.showresult("you get ticket from 1")
            #self.change_table(self.table_line.currentIndex)
        self.lock.release()
            




if __name__=="__main__":
    work1=0
    work2=0
    e=[0,0]
    app = QApplication(sys.argv)
    myWin=MyMainWindow()
    #thread1 = threading.Thread(target=myWin.sale_tic1,args=())
    #thread2 = threading.Thread(target=myWin.sale_tic2,args=())
    #thread1.start()
    #thread2.start()
    myWin.show()
    sys.exit(app.exec_())
