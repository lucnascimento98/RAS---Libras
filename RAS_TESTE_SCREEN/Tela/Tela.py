import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QComboBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt

CATEGORIES = ["A","B","C","D","E","F","G","I","L","M","N","O","P","Q","R","T","U","V","W","Y"]

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.upper = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.name = "Praticar"

        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(800, 600))

        combo_text = QLabel(self)
        combo_text.move(20,60)
        combo_text.resize(200,20)
        combo_text.setText("Selecione uma letra")
        combo_text.setAlignment(QtCore.Qt.AlignCenter)
        combo_text.setStyleSheet('QLabel {font:bold; font-size:20px; color="black"}')

        self.combo = QComboBox(self)
        self.combo.addItems(CATEGORIES)
        self.combo.move(20,100)
        self.combo.resize(200,30)

        select = QPushButton("Aprender!",self) # ! Só para ser ousado
        select.move(20,140)
        select.resize(200,30)
        select.clicked.connect(self.select_click)

        image_text = QLabel(self)
        image_text.move(20,270)
        image_text.resize(200,20)
        image_text.setText("Imite a letra")
        image_text.setAlignment(QtCore.Qt.AlignCenter)
        image_text.setStyleSheet('QLabel {font:bold; font-size:20px; color="black"}')

        self.image_hand = QLabel(self)
        self.image_hand.move(20,300)
        self.image_hand.resize(200,200)
        self.image_hand.setStyleSheet("border: 3px solid black;") 
        self.image_hand.setAlignment(QtCore.Qt.AlignCenter)
        self.image_hand.setPixmap(QtGui.QPixmap('hands_images\none.png'))

        exit = QPushButton('Sair',self) # Declarando o botão 1 para o o objeto
        exit.move(700, 530) # Posição do objeto dentro da janela
        exit.resize(70, 30) # Define o tamanho do botão (Largura, Altura)
        exit.setStyleSheet('QPushButton {background-color:#BA0C2F; font-size:18px; color:white}') # Mudar o estilo do botão
        exit.clicked.connect(self.exit_click)

        back = QPushButton('Voltar',self) # Declarando o botão 1 para o o objeto
        back.move(630, 530) # Posição do objeto dentro da janela
        back.resize(70, 30) # Define o tamanho do botão (Largura, Altura)
        back.setStyleSheet('QPushButton {background-color:#772583; font-size:18px; color:white}') # Mudar o estilo do botão
        back.clicked.connect(self.exit_click)

        self.load_window()

    def load_window(self):
        self.setGeometry(self.left,self.upper,self.width,self.height)
        self.setWindowTitle(self.name)
        self.show()

    def select_click(self):
        pixmap = QtGui.QPixmap('hands_images\{}.png'.format(CATEGORIES[self.combo.currentIndex()]))
        smaller_pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.image_hand.setPixmap(smaller_pixmap)

    def exit_click(self): # Comando do botão
        sys.exit()

application = QApplication(sys.argv) # Parametro para fechar janela
j = window()
sys.exit(application.exec())
