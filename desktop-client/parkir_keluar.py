from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QMessageBox, QComboBox
import api, utils

class ParkirKeluar(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Parkir Keluar")
        v = QVBoxLayout()
        v.addWidget(QLabel("Plat Nomor"))
        self.plat = QLineEdit(); v.addWidget(self.plat)
        v.addWidget(QLabel("Metode Pembayaran"))
        self.metode = QComboBox(); self.metode.addItems(["Tunai","QRIS","E-Wallet"]); v.addWidget(self.metode)
        btn = QPushButton("Proses Keluar"); btn.clicked.connect(self.submit); v.addWidget(btn)
        self.setLayout(v)

    def submit(self):
        data, code = api.park_out(self.plat.text(), self.metode.currentText())
        if code == 200:
            utils.generate_struk(self.plat.text(), data['duration'], data['fee'], data['metode'])
            QMessageBox.information(self, "Berhasil", f"Durasi: {data['duration']} jam\nBiaya: Rp {data['fee']:,}\nStruk disimpan.")
            self.close()
        else:
            QMessageBox.warning(self, "Error", data.get('msg', 'Gagal'))
