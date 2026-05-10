from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class FinalWin(QWidget):

    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.index_txt = QLabel(txt_index)
        self.workheart_txt = QLabel(txt_workheart)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.index_txt, alignment = Qt.AlignCenter)
        self.v_layout.addWidget(self.workheart_txt, alignment = Qt.AlignCenter)
        self.setLayout(self.v_layout)

app = QApplication([])
mw = FinalWin()
app.exec_()