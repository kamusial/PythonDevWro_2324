from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QWidget, QPushButton
import sys

app = QApplication(sys.argv)
# window = QDialog()

button = QPushButton('Nacisnij')
button.show()

# window.show()
app.exec()