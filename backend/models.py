from database import db
from datetime import datetime, timedelta

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(20))  # member, petugas, admin
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plat = db.Column(db.String(20), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Membership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    berlaku_sampai = db.Column(db.DateTime)
    last_paid = db.Column(db.DateTime)

    def extend_membership(self, bulan: int = 1):
        today = datetime.utcnow()
        if self.berlaku_sampai and self.berlaku_sampai > today:
            self.berlaku_sampai += timedelta(days=30 * bulan)
        else:
            self.berlaku_sampai = today + timedelta(days=30 * bulan)
        self.last_paid = today
