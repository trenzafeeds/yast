
"""
window.py

Functions for Qt window
creation.

Sources:
[1] https://stackoverflow.com/questions/33982167/pyqt5-create-semi-transparent-window-with-non-transparent-children
[2] https://stackoverflow.com/questions/49971584/updating-pyqt5-gui-with-live-data
"""

from lib.timer import *
from config import *

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pynput import keyboard

def display_time(time_in_s):
    return "{:0>2.0f}:{:0>2.0f}:{:0>2.2f}".format(time_in_s // 3600, time_in_s // 60, time_in_s % 60)

# Following class from [2]
class MainWindow(QMainWindow):

    def __init__(self, timer_label):
        QMainWindow.__init__(self)
        self.timer_label = timer_label
        
        self.setMinimumWidth(350)
        self.setMinimumHeight(100)

        # Styling
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        
        # Timer display
        self.label = QLabel('0.0')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Monospace', 20))
        self.label.setStyleSheet("background-color: pink; color: white; border: 1px solid aqua;")
        self.timer_name = QLabel('Untitled')
        self.timer_name.setFont(QFont('Monospace', 12))
        self.timer_name.setAlignment(Qt.AlignCenter)
        self.timer_name.setStyleSheet("background-color: pink; color: white; border: 1px solid aqua;")
        self.last_split = QLabel('No Split Yet')
        self.last_split.setFont(QFont('Monospace', 12))
        self.last_split.setAlignment(Qt.AlignCenter)
        self.last_split.setStyleSheet("background-color: pink; color: white; border: 1px solid aqua;")
        self.split_val = QLabel('No Split Yet')
        self.split_val.setFont(QFont('Monospace', 12))
        self.split_val.setAlignment(Qt.AlignCenter)
        self.split_val.setStyleSheet("background-color: pink; color: white; border: 1px solid aqua;")

        self.timer_w = QWidget()
        self.w_layout = QGridLayout(self.timer_w)
        self.w_layout.addWidget(self.timer_name, 0, 0)
        self.w_layout.addWidget(self.last_split, 1, 1)
        self.w_layout.addWidget(self.label, 0, 1)
        self.w_layout.addWidget(self.split_val, 1, 0)
        self.setCentralWidget(self.timer_w)

        self.qtimer = QTimer()
        self.qtimer.setInterval(50)
        self.qtimer.timeout.connect(self.updatetime)

        self.hk_startpause = keyboard.GlobalHotKeys({'{}'.format(STARTPAUSEKEY):self.startpause})
        self.hk_split = keyboard.GlobalHotKeys({'{}'.format(SPLITKEY):self.split})
        self.hk_unsplit = keyboard.GlobalHotKeys({'{}'.format(UNSPLITKEY):self.unsplit})
        self.hk_save = keyboard.GlobalHotKeys({'{}'.format(SAVEKEY):self.save})
        self.hk_quit = keyboard.GlobalHotKeys({'{}'.format(QUITKEY):self.finish})
        self.hk_startpause.start()
        self.hk_split.start()
        self.hk_unsplit.start()
        self.hk_save.start()
        self.hk_quit.start()
        
        self.event_loop()

    def event_loop(self):
        self.rtimer = Timer(self.timer_label)
        self.updatesplit()
        self.checksplitval()
        self.qtimer.start()
        self.timer_name.setText(self.rtimer.label)

    def updatetime(self):
        ctime = self.rtimer.get_time()
        self.label.setText(display_time(ctime))
        self.updatesplit()

    def updatesplit(self):
        lsplit = self.rtimer.since_split()
        self.last_split.setText(display_time(lsplit))

    def startpause(self):
        if not self.rtimer.started: self.rtimer.start()
        else:
            if self.rtimer.active: self.rtimer.pause()
            else: self.rtimer.resume()

    def split(self):
        last = self.rtimer.split()
        self.split_val.setText(display_time(last))

    def unsplit(self):
        last = self.rtimer.unsplit()
        self.split_val.setText(display_time(last))

    def checksplitval(self):
        last = self.rtimer.last_split()
        self.split_val.setText(display_time(last))

    def save(self):
        self.rtimer.save()

    def finish(self):
        if not self.rtimer.active:
            self.close()
        else: pass
        
        
def main_window(timer_label=None):
    qapp = QApplication(sys.argv)
    qapp.setStyle('Fusion')
    qwin = MainWindow(timer_label)
    qwin.show()
    sys.exit(qapp.exec_())
    
if __name__=='__main__':
    main_window(None)
            
