from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
import sys
from random import choice

window_titles = [
    'Moja apka',
    'Moja apka',
    'Dalej to samo',
    'Dalej to samo',
    'Ziemia',
    'Ziemia',
    'Tytul',
    'Tytul',
    'BLAD!'
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Moja aplikacja')
        self.setFixedSize(600, 400)
        button = QPushButton('przycisk')
        button.pressed.connect(self.button_clicked)




app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()