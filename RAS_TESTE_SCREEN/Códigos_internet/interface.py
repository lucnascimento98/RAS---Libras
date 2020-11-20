import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel # QToolTop permite alterar as configurações do botao
from PyQt5 import QtCore # Permitir colocar o alinhamento de texto
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread # Rodar código cv2

import cv2
import numpy as np

class VideoThread(QThread): # Código para colocar o código cv2 e código Qt numa thread
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        while True:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100 # Distância da borda superior
        self.esquerda = 100 # Distância da borda esquerda
        self.largura = 800 # Tamanho da janela
        self.altura = 600 # Tamanho da janela
        self.principal = "Primeira janela"

        self.titulo = QLabel(self)
        self.titulo.setText('RAS - Libras')
        self.titulo.move(175,0)
        self.titulo.resize(400,20)
        self.titulo.setStyleSheet('QLabel {font:bold; font-size:20px; color="blue"}')
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)

        self.texto = QLabel(self)
        self.texto.setText('Ver texto')
        self.texto.move(123,200)
        self.texto.resize(400,20)
        self.texto.setStyleSheet('QLabel {font:bold; font-size:20px; color="blue"}')
        self.texto.setAlignment(QtCore.Qt.AlignCenter)
        
        sair = QPushButton('Sair',self) # Declarando o botão 1 para o o objeto
        sair.move(730, 570) # Posição do objeto dentro da janela
        sair.resize(70, 30) # Define o tamanho do botão (Largura, Altura)
        sair.setStyleSheet('QPushButton {background-color:#870EA5; font:bold; font-size:20px}') # Mudar o estilo do botão
        sair.clicked.connect(self.sair_click)

        botao2 = QPushButton('Não Aperte Aqui!',self)
        botao2.move(660, 570)
        botao2.resize(70, 30)
        botao2.setStyleSheet('QPushButton {background-color:#8B0000; font:italic; font-size:20px}')
        botao2.clicked.connect(self.botao2_click)

        # Colocando a janela do opencv

        self.CarregarJanela() # Colocar os Widgets antes de definir a janela

    def CarregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.principal)
        self.show()

    def sair_click(self): # Comando do botão
        sys.exit()

    def botao2_click(self): # Comando do botão
        self.texto.setText('Teste botao')

aplicacao = QApplication(sys.argv) # Parametro para fechar janela
j = Janela()
sys.exit(aplicacao.exec())
