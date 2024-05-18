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
]

window_titles *= 2
window_titles.append('BLAD!')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aplikacja')
        self.setFixedSize(600, 400)
        self.button = QPushButton('Kliknij')
        self.button.clicked.connect(self.button_clicked)
        self.windowTitleChanged.connect(self.wrong_title)
        self.setCentralWidget(self.button)

    def button_clicked(self):
        print('klikniety')
        new_title = choice(window_titles)
        print(f'nowy tytul: {new_title}')
        self.setWindowTitle(new_title)

    def wrong_title(self, window_title):
        print('Tytul zmieniono na ',window_title)
        if window_title == 'BLAD!':
            self.button.setDisabled(True)
            self.button.setText('Nieaktywny')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()