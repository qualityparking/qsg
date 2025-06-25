from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QMessageBox, QComboBox
import api

class ParkirMasuk(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Parkir Masuk")
        v = QVBoxLayout()
        v.addWidget(QLabel("Plat Nomor"))
        self.plat = QLineEdit(); v.addWidget(self.plat)
        v.addWidget(QLabel("Jenis Kendaraan"))
        self.jenis = QComboBox(); self.jenis.addItems(["motor","mobil","truk"]); v.addWidget(self.jenis)
        btn = QPushButton("Submit"); btn.clicked.connect(self.submit); v.addWidget(btn)
        self.setLayout(v)

    def submit(self):
        data, code = api.park_in(self.plat.text(), self.jenis.currentText())
        if code == 201:
            QMessageBox.information(self, "Sukses", "Parkir masuk tercatat.")
            self.close()
        else:
            QMessageBox.warning(self, "Error", data.get('msg', 'Gagal'))
