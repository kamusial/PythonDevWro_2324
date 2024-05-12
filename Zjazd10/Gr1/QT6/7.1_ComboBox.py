import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QComboBox

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Combo box')
        widget = QComboBox()
        widget.addItems(['Zero', 'raz', 'dwa', 'trzy'])
        widget.currentTextChanged.connect(self.text_change)
        widget.currentIndexChanged.connect(self.index_changed)

        self.setCentralWidget(widget)

    def text_change(self, s):
        print(s)

    def index_changed(self, i):
        print(i)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
