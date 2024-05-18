from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QPushButton
import sys

app = QApplication(sys.argv)

window1 = QDialog()     #proste okno, tylko z Xem do zamkniecia
window1.setWindowTitle('QDialog')
window1.show()

window2 = QWidget()     #proste okno, z Xem, minimalizacją i pełnym ekranem
window2.setWindowTitle('QWidget')
window2.show()

window3 = QMainWindow()   #zaawansowane okno z większą liczbą funkcji
window3.setWindowTitle('QMainWindow')
window3.statusBar().showMessage('Status to .......')
window3.menuBar().addMenu('Options')
window3.show()

app.exec()