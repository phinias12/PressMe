from PyQt5.QtCore import QTimer, QCoreApplication
from PyQt5.QtGui import QFont, QPainter, QColor
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QVBoxLayout,
                             QLabel, QPushButton)
from random import *
import time

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        # Initialize the splashPage
        self.splashPage()

    def newgame():
        self.hide()
        self.splashPage()

    def splashPage(self):
        # This is the intro name for the splashPage window
        # Initialize
        self.x1 = 0
        self.placementx1 = 0
        self.placementy1 = self.placementx1+120
        self.placementx2 = 0
        self.placementy2 = self.placementx2+120
        self.score = 0
        self.count = 60

        # Initialize the window
        self.move(15, 15)
        self.setWindowTitle('Press Me!')
        self.resize(1000,700)

        # Initialize all labels and buttons in the game everything in the game
        self.gameover = False
        self.timer_font = QFont("Times New Roman", 18)
        self.score = 0
        self.timer = QTimer(timeout=self.update)
        self.countdown_timer = QTimer(timeout=self.countdown)
        self.name = QLabel("Press Me!", self)
        self.intro_font = QFont("Helvetica", 65)
        self.btn_font = QFont("Helvetica", 40)
        self.name.setFont(self.intro_font)
        self.scorelabel=QLabel("Score: "+str(self.score), self)
        self.font= QFont("Times New Roman", 18)
        self.instr = QLabel("It's so simple. Just press the black square that ", self)
        self.instr1 = QLabel("randomly changes its position. But be careful,", self)
        self.instr2 = QLabel("everytime when you touch the wrong place, you ", self)
        self.instr3 = QLabel("get a point taken off. You have only 60 seconds", self)
        self.instr4 = QLabel(" to get as much points as possible.", self)
        self.countdown_label = QLabel('', self)
        self.timerlabel = QLabel('',self)
        self.count = 3
        self.timer_count = 30
        self.timerlabel.setText("Time: "+str(self.timer_count))
        self.instr.resize(0,0)
        self.instr1.resize(0,0)
        self.instr2.resize(0,0)
        self.instr3.resize(0,0)
        self.instr4.resize(0,0)
        self.timerlabel.resize(0,0)
        self.scorelabel.resize(0,0)
        self.scorelabel.resize(0,0)
        self.timerlabel.resize(0,0)
        self.countdown_label.resize(0,0)
        self.instr.resize(0,0)
        self.instr1.resize(0,0)
        self.instr2.resize(0,0)
        self.instr3.resize(0,0)
        self.instr4.resize(0,0)
        self.x1 = 0
        self.placementx1 = 0
        self.placementy1 = 0
        self.placementx2 = 0
        self.placementy2 = 0
        self.start_btn = QPushButton('', self)
        self.help_btn =  QPushButton('', self)
        self.gameover = False

        # The intro page name
        self.name.resize(400,150)
        self.name.move(300,200)

        #The start_btn
        self.start_btn.setFont(self.btn_font)
        self.start_btn.resize(175,50)
        self.start_btn.move(300,400)
        self.start_btn.setText('START')
        self.start_btn.clicked.connect(self.countdown)

        #The help_btn
        self.help_btn.setFont(self.btn_font)
        self.help_btn.resize(175, 50)
        self.help_btn.move(525, 400)
        self.help_btn.clicked.connect(self.help)
        self.help_btn.setText('HELP')

        self.show()

    def help(self):
        #Clear everything
        self.name.resize(0,0)

        #Make instructions
        intro_font = QFont("Helvetica", 32)
        self.instr.setFont(intro_font)
        self.instr1.setFont(intro_font)
        self.instr2.setFont(intro_font)
        self.instr3.setFont(intro_font)
        self.instr4.setFont(intro_font)
        self.instr.resize(950,50)
        self.instr.move(40,100)
        self.instr1.resize(950, 50)
        self.instr1.move(40,150)
        self.instr2.resize(950, 50)
        self.instr2.move(40,200)
        self.instr3.resize(950, 50)
        self.instr3.move(40,250)
        self.instr4.resize(950, 50)
        self.instr4.move(40,300)
        self.help_btn.resize(0,0)
        self.start_btn.move(400,400)

        self.start_btn.setText("PLAY")
        self.start_btn.clicked.connect(self.countdown)

        self.show()

    def countdown(self):
        #Clear everything
        self.countdown_timer.start(1000)
        self.scorelabel.resize(0,0)
        self.timerlabel.resize(0,0)
        self.countdown_label.resize(0,0)
        self.instr.resize(0,0)
        self.instr1.resize(0,0)
        self.instr2.resize(0,0)
        self.instr3.resize(0,0)
        self.instr4.resize(0,0)
        self.x1 = 0
        self.placementx1 = 0
        self.placementy1 = 0
        self.placementx2 = 0
        self.placementy2 = 0
        self.repaint()
        self.score = 0
        self.gameover = False
        self.name.resize(0,0)
        self.help_btn.resize(0,0)
        self.start_btn.resize(0,0)
        self.instr.resize(0,0)
        self.instr1.resize(0, 0)
        self.instr2.resize(0, 0)
        self.instr3.resize(0, 0)
        self.instr4.resize(0, 0)
        self.countdown_label.setText(str(self.count))

        #Initialize
        self.countdown_font = QFont('Helvetica',100)
        self.countdown_label.setFont(self.countdown_font)
        self.countdown_label.move(500,0)
        self.countdown_label.resize(950,650)

        if self.count == 0:
            self.game()

        self.count -= 1
        self.show()

    def game(self):
        self.countdown_label.resize(0, 0)
        self.countdown_timer.stop()
        self.x1 = 120
        self.placementx1 = 450
        self.placementy1 = self.placementx1+ 120
        self.placementx2 = 200
        self.placementy2 = self.placementx2+ 120
        self.score = 0
        self.scorelabel.setText("Score: "+str(self.score))
        self.timer_count = 30
        self.repaint()
        self.timerlabel.setText("Timer: "+str(self.timer_count))

        self.scorelabel.setFont(self.font)
        self.scorelabel.resize(200,50)
        self.scorelabel.move(10,0)
        self.timerlabel.move(320,0)
        self.timerlabel.resize(400,50)
        self.timerlabel.setFont(self.font)
        self.timer.start(1000)

        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):
        color = QColor(0, 0, 0)
        color.setNamedColor('#646464')
        qp.setPen(color)
        qp.setBrush(QColor('black'))
        qp.drawRect(self.placementx1,self.placementx2,
                    self.x1,self.x1)

    def mousePressEvent(self,event):
        if not self.gameover:
            pointerx = event.x()
            pointery = event.y()
            if self.placementx1<=pointerx<=self.placementx1+self.x1 \
               and self.placementx2<=pointery<=self.placementx2+self.x1:

                if self.x1 > 30:
                    self.x1-=2

                print("Location ({}, {})".format(
                pointerx, pointery))
                print("HIT!")
                self.placementy1-=2
                self.placementy2-=2
                self.placementx1=(randint(0,800))
                self.placementx2=(randint(50,500))
                self.score += 1
                self.scorelabel.setText("Score: "+str(self.score))
                self.repaint()

            else:
                print("MISS!")
                self.score -=1
                self.scorelabel.setText("Score: "+str(self.score))

    def update(self):
        if not self.gameover:
            self.timer_count -= 1
            if self.timer_count == 0:
                self.timer.stop()
                self.gameover = True
                self.endgame()
            if not self.gameover:
                self.timerlabel.setText("Timer: "+str(self.timer_count))
                self.placementx1=(randint(0,400))
                self.placementx2=(randint(50,400))
                self.repaint()

    def endgame(self):
        self.start_btn.resize(175,50)
        self.start_btn.move(300,400)
        self.count = 3
        self.start_btn.clicked.connect(self.newgame)
        self.start_btn.setText('PLAY')

        self.help_btn.resize(175, 50)
        self.help_btn.move(525, 400)
        self.help_btn.clicked.connect(QCoreApplication.instance().quit)
        self.help_btn.setText('LEAVE')

        self.timerlabel.setText("GAME OVER!")

app = QApplication([])
ex = MainWindow()
ex.show()
app.exec()
