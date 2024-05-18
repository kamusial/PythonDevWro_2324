from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
import sys
from random import choice

window_titles = [
    'Jan',
    'Alicja',
    'Ania',
    'Kamil',
    'Jakub',
    'Agnieszka',
    'Tomasz',
    'Ada',
    'BLAD!'
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()