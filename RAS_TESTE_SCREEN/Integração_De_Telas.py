import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from interface import *
from interface2 import *

class janela2(QMainWindow):
    def __init__ (self):
        super() .__init__()
        self.ui = Ui_Janela2()
        self.ui.setupUi(self)
        self.ui.start_button.clicked.connect(self.voltaJanela)

    def voltaJanela(self):
        self.origem = tela()
        self.origem.show()
        self.close()


class tela(QMainWindow):
    def __init__ (self):
        super() .__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.janela2 = janela2()
        self.ui.start_button.clicked.connect(self.mudaJanela)


    def mudaJanela(self):
        self.janela2.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = tela()
    w.show()
    sys.exit(app.exec_())