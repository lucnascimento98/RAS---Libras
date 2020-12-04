import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from Menu import *
from Aprender import *
from Testar import *
from Informações import *


class Aprender(QMainWindow):
    def __init__ (self):
        super() .__init__()
        self.ui = Ui_Janela2()
        self.ui.setupUi(self)
        self.ui.start_button.clicked.connect(self.voltaJanela)

    def voltaJanela(self):
        self.origem = Menu()
        self.origem.show()
        self.close()


class Testar(QMainWindow):
    def __init__ (self):
        super() .__init__()
        self.ui = Ui_Testar()
        self.ui.setupUi(self)
        self.ui.start_button_2.clicked.connect(self.voltaJanela)

    def voltaJanela(self):
        self.origem = Menu()
        self.origem.show()
        self.close()


class Informacoes(QMainWindow):
    def __init__ (self):
        super() .__init__()
        self.ui = Ui_Informacoes()
        self.ui.setupUi(self)
        self.ui.config_button.clicked.connect(self.voltaJanela)

    def voltaJanela(self):
        self.origem = Menu()
        self.origem.show()
        self.close()


class Menu(QMainWindow):
    def __init__ (self):
        super() .__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Aprender = Aprender()
        self.ui.start_button.clicked.connect(self.mudaJanela)
        self.Testar = Testar()
        self.ui.start_button_2.clicked.connect(self.mudaJanela2)
        self.Informacoes = Informacoes()
        self.ui.config_button.clicked.connect(self.mudaJanela3)


    def mudaJanela(self):
        self.Aprender.show()
        self.hide()

    def mudaJanela2(self):
        self.Testar.show()
        self.hide()

    def mudaJanela3(self):
        self.Informacoes.show()
        self.hide()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Menu()
    w.show()
    sys.exit(app.exec_())