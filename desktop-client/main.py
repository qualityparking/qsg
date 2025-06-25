import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from login import LoginWindow
from parkir_masuk import ParkirMasuk
from parkir_keluar import ParkirKeluar

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operator Parkir")
        v = QVBoxLayout()
        btn1 = QPushButton("Parkir Masuk"); btn1.clicked.connect(self.masuk); v.addWidget(btn1)
        btn2 = QPushButton("Parkir Keluar"); btn2.clicked.connect(self.keluar); v.addWidget(btn2)
        self.setLayout(v)

    def masuk(self): ParkirMasuk().show()
    def keluar(self): ParkirKeluar().show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    LoginWindow().show()
    sys.exit(app.exec())
