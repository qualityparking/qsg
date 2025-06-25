import os
from reportlab.lib.pagesizes import A6
from reportlab.pdfgen import canvas
from datetime import datetime

os.makedirs('struk', exist_ok=True)

def generate_struk(plat, duration, fee, metode):
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    fname = f"struk/STRUK_{plat}_{now}.pdf"
    c = canvas.Canvas(fname, pagesize=A6)
    c.setFont("Helvetica", 10)
    c.drawString(20, 140, "STRUK PARKIR")
    c.drawString(20, 125, f"Plat: {plat}")
    c.drawString(20, 110, f"Durasi: {duration} jam")
    c.drawString(20, 95, f"Biaya: Rp {fee:,}")
    c.drawString(20, 80, f"Metode: {metode}")
    c.drawString(20, 50, f"Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.save()
    return fname
