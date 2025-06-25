from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import sqlite3

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
