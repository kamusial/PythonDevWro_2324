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
        self.button = QPushButton('przycisk')
        self.button.pressed.connect(self.button_clicked)
        self.windowTitleChanged.connect(self.wrong_title)
        self.setCentralWidget(self.button)

    def button_clicked(self):
        print('kliknięty')
        current_title = choice(window_titles)
        print('nowy tytul to: ', current_title)
        self.setWindowTitle(current_title)

    def wrong_title(self, window_title):
        print('Tytul zmieniono na', window_title)
        if window_title == 'BLAD!':
            self.button.setDisabled(True)
            self.button.setText('Nieaktywny')
            
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()