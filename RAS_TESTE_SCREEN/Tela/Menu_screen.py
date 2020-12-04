import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QComboBox, QWidget, QVBoxLayout
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread


class windowMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.upper = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.name = "Menu"

        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(800, 600))

        title = QLabel(self)
        title.move(250,40)
        title.resize(300,90)
        title.setText("LibRAS")
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setStyleSheet('QLabel {font:bold; font-size:35px; color:#BA0C2F}')

        image_logo_LibRAS = QLabel(self)
        image_logo_LibRAS.

        learn = QPushButton("Aprender",self) # ! Só para ser ousado
        learn.move(100,160)
        learn.resize(160,80)
        learn.setStyleSheet('QPushButton {background-color:#772583; font-size:18px; color:white}')
        # learn.clicked.connect(self.select_click)

        test = QPushButton("Testar",self) # ! Só para ser ousado
        test.move(100,250)
        test.resize(160,80)
        test.setStyleSheet('QPushButton {background-color:#772583; font-size:18px; color:white}')
        # test.clicked.connect(self.select_click)

        info = QPushButton("Informações",self) # ! Só para ser ousado
        info.move(100,340)
        info.resize(160,80)
        info.setStyleSheet('QPushButton {background-color:#772583; font-size:18px; color:white}')
        # info.clicked.connect(self.select_click)

        exit = QPushButton('Sair',self) # Declarando o botão 1 para o o objeto
        exit.move(100, 430) # Posição do objeto dentro da janela
        exit.resize(160,80) # Define o tamanho do botão (Largura, Altura)
        exit.setStyleSheet('QPushButton {background-color:#BA0C2F; font-size:18px; color:white}') # Mudar o estilo do botão
        exit.clicked.connect(self.exit_click)


        self.load_window()

    def load_window(self):
        self.setGeometry(self.left,self.upper,self.width,self.height)
        self.setWindowTitle(self.name)
        self.show()

    def exit_click(self): # Comando do botão
        sys.exit()


application = QApplication(sys.argv) # Parametro para fechar janela
j = windowMenu()
sys.exit(application.exec())