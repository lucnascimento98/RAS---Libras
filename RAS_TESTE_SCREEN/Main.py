import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel # QToolTop permite alterar as configurações do botao
from PyQt5 import QtCore, QtWidgets # Permitir colocar o alinhamento de texto
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread # Rodar código cv2

from ScreenOpenCV import App

from interface import Ui_MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())