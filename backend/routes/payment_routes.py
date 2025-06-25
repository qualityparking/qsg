from flask import Blueprint, request, jsonify
from midtrans_config import midtrans_auth_header
import requests
import uuid
from datetime import datetime

payment_bp = Blueprint('payment_bp', __name__)

@payment_bp.route('/payment/token', methods=['POST'])
def create_snap_token():
    data = request.json
    order_id = f"ORDER-{uuid.uuid4().hex[:10]}"
    amount = int(data['amount'])

    payload = {
        "transaction_details": {
            "order_id": order_id,
            "gross_amount": amount
        },
        "credit_card": {"secure": True},
        "customer_details": {
            "first_name": "Member",
            "email": "member@example.com"
        }
    }

    res = requests.post(
        'https://app.sandbox.midtrans.com/snap/v1/transactions',
        headers=midtrans_auth_header(),
        json=payload
    )

    return jsonify({"snap_url": res.json().get('redirect_url')}), res.status_code


@payment_bp.route('/payment/confirm', methods=['POST'])
def confirm_payment():
    data = request.json
    order_id = data.get('order_id')
    status = data.get('transaction_status')

    # TODO: Verifikasi signature_key jika perlu
    # TODO: Update membership status di database

    if status in ['settlement', 'capture']:
        # Logika: extend membership expiry date
        print(f"[✔] Order {order_id} berhasil dibayar.")
    else:
        print(f"[!] Pembayaran untuk {order_id} status: {status}")

    return jsonify({'status': 'ok'})
