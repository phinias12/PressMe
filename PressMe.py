from PyQt4.QtCore import QTimer
from PyQt4.QtGui import *
from random import *

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.x1=120
        self.placementx1= 450
        self.placementy1= self.placementx1+120
        self.placementx2= 200
        self.placementy2= self.placementx2+120
        self.score=0
        #self.timer=0
        self.count=60

    def initUI(self):
        self.setGeometry(10, 25, 350, 100)
        self.setWindowTitle('Press Me!')
        self.resize(800,800)
        font= QFont("Times New Roman", 18)
        self.score = 0
        self.timer=QTimer(timeout=self.update)
        self.scorelabel=QLabel("Score: "+str(self.score), self)
        self.scorelabel.setFont(font)
        self.scorelabel.resize(100,50)
        self.scorelabel.move(10,0)
        self.timerlabel=QLabel(self)
        self.count=60
        self.timerlabel.setText("Time: "+str(self.count))
        self.timerlabel.move(320,0)
        self.timerlabel.resize(100,50)
        self.timerlabel.setFont(font)
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
        qp.drawRect(self.placementx1,self.placementx2,self.x1,self.x1)

    def mousePressEvent(self,event):
        pointerx=event.x()
        pointery=event.y()
        if self.placementx1<=pointerx<=self.placementx1+self.x1 \
           and self.placementx2<=pointery<=self.placementx2+self.x1:
            if self.x1 > 30:
                self.x1-=2
            else:
                pass
            print("HIT!")
            self.placementy1-=2
            self.placementy2-=2
            self.placementx1=(randint(0,400))
            self.placementx2=(randint(50,400))
            self.score += 1
            self.scorelabel.setText("Score: "+str(self.score))
            self.repaint()


        else:
            print("MISS!")
            self.score -=1
            self.scorelabel.setText("Score: "+str(self.score))

    def update(self):
        self.count-=1
        self.timerlabel.setText("Timer: "+str(self.count))
        self.placementx1=(randint(0,400))
        self.placementx2=(randint(20,400))
        self.repaint()

app = QApplication([])
ex = MainWindow()
ex.show()
app.exec()
