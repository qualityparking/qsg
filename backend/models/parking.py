from app import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Parking(db.Model):
    __tablename__ = 'parkings'
    id = Column(Integer, primary_key=True)
    vehicle_plate = Column(String(20), nullable=False)
    vehicle_type = Column(String(20), nullable=True)
    masuk = Column(DateTime, nullable=False)
    keluar = Column(DateTime, nullable=True)
    duration = Column(Integer, nullable=True)
    fee = Column(Integer, nullable=True)
    payment_method = Column(String(20), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')
