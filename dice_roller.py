import random
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSvg import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    
    def testwurf(self,  layout):
        roll = random.randint(1,6)
        print(roll)
        rollstring = f"w{roll}s.svg"
        layout.addWidget(QSvgWidget(rollstring))        
        return rollstring
        
    def wuerfeln(self,  layout):
        roll = random.randint(1,6)
        print(roll)
        rollstring = f"w{roll}s.svg"
        wwidget = QSvgWidget(rollstring)
        layout.insertWidget(0, wwidget)  
        altwidget = layout.widget(1)
        layout.removeWidget(altwidget)
        altwidget.deleteLater()
#        layout.setCurrentIndex(0)
        return rollstring

    def farbe(self, s):
        if s:
            print('Yea, Farbe',  s)
        else:
            print('Hier könnte Ihre Farbe stehen',  s)
        return s

    def __init__ (self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Würfel')
        
        layout = QStackedLayout()
        margin = 15
        layout.setContentsMargins(margin, margin,margin,margin)
        
        toolbar = QToolBar('Menüleiste')
        self.addToolBar(toolbar)
    
        button_action = QAction(QIcon('w5.svg'), "Würfeln", self)
        button_action.setStatusTip("Klicken, um zu würfeln")
        button_action.triggered.connect(lambda: self.wuerfeln(layout))
        toolbar.addAction(button_action)
        
        erg = self.testwurf(layout)
        
        
        cwidget = QWidget()
        cwidget.setLayout(layout)
        self.setCentralWidget(cwidget)
        
        button_action2 = QAction(QIcon('farbe.svg'),  "bunt", self)
        button_action2.setStatusTip("Mach den Würfel bunt")
        button_action2.triggered.connect(self.farbe)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)
        
        button_action3 = QAction(QIcon('ende.svg'), "Beenden", self)
        button_action3.setStatusTip("Programm beenden")
        button_action3.triggered.connect(self.close)
        toolbar.addAction(button_action3)

        self.setStatusBar(QStatusBar(self))
  

app = QApplication(sys.argv)

fenster = MainWindow()
fenster.setGeometry(100, 100, 256, 310)

fenster.show()

sys.exit(app.exec_())