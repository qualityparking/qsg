from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from reportlab.lib.pagesizes import A6
from reportlab.pdfgen import canvas
import os
import sqlite3

os.makedirs('struk', exist_ok=True)

def generate_struk(plat, masuk, keluar, durasi, biaya, metode):
    filename = f"struk/STRUK_{plat}_{keluar.strftime('%Y%m%d%H%M%S')}.pdf"
    c = canvas.Canvas(filename, pagesize=A6)
    c.setFont("Helvetica", 10)
    c.drawString(20, 140, f"STRUK PARKIR")
    c.drawString(20, 125, f"Plat Nomor: {plat}")
    c.drawString(20, 110, f"Masuk: {masuk.strftime('%Y-%m-%d %H:%M')}")
    c.drawString(20, 95, f"Keluar: {keluar.strftime('%Y-%m-%d %H:%M')}")
    c.drawString(20, 80, f"Durasi: {durasi} jam")
    c.drawString(20, 65, f"Biaya: Rp {biaya:,}")
    c.drawString(20, 50, f"Metode: {metode}")
    c.save()
    return filename

app = Flask(__name__)
DB = 'database.db'
TARIF_PER_JAM = 2000

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS parkir (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plat TEXT,
            masuk DATETIME,
            keluar DATETIME,
            durasi_jam INTEGER,
            biaya INTEGER,
            metode_pembayaran TEXT
        )''')

@app.route('/')
def dashboard():
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM parkir WHERE keluar IS NULL")
        aktif = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM parkir WHERE keluar IS NOT NULL")
        selesai = cur.fetchone()[0]
    return render_template('dashboard.html', aktif=aktif, selesai=selesai)

@app.route('/masuk', methods=['GET', 'POST'])
def masuk():
    if request.method == 'POST':
        plat = request.form['plat'].upper()
        waktu = datetime.now()
        with sqlite3.connect(DB) as conn:
            conn.execute("INSERT INTO parkir (plat, masuk) VALUES (?, ?)", (plat, waktu))
        return redirect(url_for('dashboard'))
    return render_template('masuk.html')

@app.route('/keluar', methods=['GET', 'POST'])
def keluar():
    if request.method == 'POST':
        plat = request.form['plat'].upper()
        metode = request.form['metode']
        keluar = datetime.now()

        with sqlite3.connect(DB) as conn:
            cur = conn.cursor()
            cur.execute("SELECT id, masuk FROM parkir WHERE plat = ? AND keluar IS NULL", (plat,))
            row = cur.fetchone()
            if row:
    id_, masuk = row
    masuk = datetime.strptime(masuk, '%Y-%m-%d %H:%M:%S')
    durasi = max(1, int((keluar - masuk).total_seconds() // 3600))
    biaya = durasi * TARIF_PER_JAM
    cur.execute("UPDATE parkir SET keluar = ?, durasi_jam = ?, biaya = ?, metode_pembayaran = ? WHERE id = ?",
                (keluar, durasi, biaya, metode, id_))
    generate_struk(plat, masuk, keluar, durasi, biaya, metode)
    return redirect(url_for('dashboard'))
            else:
                return "Kendaraan tidak ditemukan.", 404
    return render_template('keluar.html')

@app.route('/riwayat')
def riwayat():
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM parkir WHERE keluar IS NOT NULL ORDER BY keluar DESC")
        data = cur.fetchall()
    return render_template('riwayat.html', data=data)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
