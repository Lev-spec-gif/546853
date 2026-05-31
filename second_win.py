from instr import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit
from final_win import *
class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = int(age)
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3
class SecondWin(QWidget):

    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connect()
        self.show()

    def set_appear(self):
        self.setWindowTitle('zxc')
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    #ТАЙМЕР 1
    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 30, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    #2
    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 30, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    #3
    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 30, QFont.Bold))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def initUI(self):
        #тексты
        self.text_timer = QLabel('0')
        self.name_txt = QLabel(txt_name)
        self.age_txt = QLabel(txt_age)
        self.test1_txt = QLabel(txt_test1)
        self.test2_txt = QLabel(txt_test2)
        self.test3_txt = QLabel(txt_test3)
        #кнопки
        self.btn_test1 = QPushButton(txt_starttest1)
        self.btn_test2 = QPushButton(txt_starttest2)
        self.btn_test3 = QPushButton(txt_starttest3)
        self.sendresults_txt = QPushButton(txt_sendresults)
        # редактор линии писать
        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)
        #горизонтали вертикали
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        #линии
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignRight)
        self.l_line.addWidget(self.name_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.age_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        
        self.l_line.addWidget(self.test1_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.test2_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.test3_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.sendresults_txt, alignment = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connect(self):
        self.sendresults_txt.clicked.connect(self.next_wn)
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_sits)
        self.btn_test3.clicked.connect(self.timer_final)

    def next_wn(self):
        self.hide()
        self.exp = Experiment(self.line_age.text(), str(self.line_test1.text()), str(self.line_test2.text()), str(self.line_test3.text()))
        self.tw = FinalWin(self.exp)
