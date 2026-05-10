from instr import *
from final_win import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit

class SecondWin(QWidget):

    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connect()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        #тексты
        self.hintname_txt = QLabel(txt_hintname)
        self.hintage_txt = QLabel(txt_hintage)
        self.test1_txt = QLabel(txt_test1)
        self.test2_txt = QLabel(txt_test2)
        self.test3_txt = QLabel(txt_test3)
        self.timer_txt = QLabel('00:00:00')
        #кнопки
        self.starttest1_txt = QPushButton(txt_starttest1)
        self.starttest2_txt = QPushButton(txt_starttest2)
        self.starttest3_txt = QPushButton(txt_starttest3)
        self.sendresults_txt = QPushButton(txt_sendresults)
        # редактор линии писать
        self.line_FIO = QLineEdit('Ф.И.О.')
        self.line_age = QLineEdit('0')
        self.line_test1 = QLineEdit('0')
        self.line_test2_1 = QLineEdit('0')
        self.line_test2_2 = QLineEdit('0')
        #горизонтали вертикали
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        #линии
        self.r_line.addWidget(self.timer_txt, alignment = Qt.AlignRight)
        self.l_line.addWidget(self.hintname_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_FIO, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.hintage_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        
        self.l_line.addWidget(self.test1_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.starttest1_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.test2_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.starttest2_txt, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.test3_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.starttest3_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2_1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2_2, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.sendresults_txt, alignment = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connect(self):
        self.sendresults_txt.clicked.connect(self.next_wn)
    def next_wn(self):
        self.hide()
        FinalWin()

app = QApplication([])
mw = SecondWin()
app.exec_()