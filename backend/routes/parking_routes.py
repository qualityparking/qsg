from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models.parking import Parking
from datetime import datetime

parking_bp = Blueprint('parking', __name__)

@parking_bp.route('/in', methods=['POST'])
@jwt_required()
def park_in():
    data = request.get_json()
    current = get_jwt_identity()
    p = Parking(
        vehicle_plate = data['plat'],
        vehicle_type = data.get('jenis'),
        masuk = datetime.utcnow(),
        user_id = current['id']
    )
    db.session.add(p)
    db.session.commit()
    return jsonify(msg='Parkir masuk dicatat', id=p.id), 201

@parking_bp.route('/out', methods=['POST'])
@jwt_required()
def park_out():
    data = request.get_json()
    p = Parking.query.filter_by(vehicle_plate=data['plat'], keluar=None).first()
    if not p:
        return jsonify(msg='Tidak ditemukan'), 404

    keluar = datetime.utcnow()
    duration = int((keluar - p.masuk).total_seconds() // 3600) + 1
    rate = 2000
    fee = duration * rate

    p.keluar = keluar
    p.duration = duration
    p.fee = fee
    p.payment_method = data.get('metode')
    db.session.commit()

    return jsonify(
        plat=p.vehicle_plate,
        duration=duration,
        fee=fee,
        metode=p.payment_method
    )

