from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QMessageBox
import api

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Operator")
        v = QVBoxLayout()
        v.addWidget(QLabel("Username"))
        self.u = QLineEdit(); v.addWidget(self.u)
        v.addWidget(QLabel("Password"))
        self.p = QLineEdit(); self.p.setEchoMode(QLineEdit.Password); v.addWidget(self.p)
        btn = QPushButton("Login"); btn.clicked.connect(self.submit); v.addWidget(btn)
        self.setLayout(v)

    def submit(self):
        ok = api.login(self.u.text(), self.p.text())
        if ok: 
            from main import MainWindow
            self.close()
            MainWindow().show()
        else:
            QMessageBox.warning(self, "Gagal", "Login gagal!")
