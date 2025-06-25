import requests
from config import BASE_URL

TOKEN = None

def login(username, password):
    global TOKEN
    r = requests.post(f"{BASE_URL}/login", json={'username': username, 'password': password})
    if r.status_code == 200:
        TOKEN = r.json()['token']
        return True
    return False

def park_in(plat, jenis):
    r = requests.post(f"{BASE_URL}/parking/in", json={'plat': plat, 'jenis': jenis}, headers=get_hdr())
    return r.json(), r.status_code

def park_out(plat, metode):
    r = requests.post(f"{BASE_URL}/parking/out", json={'plat': plat, 'metode': metode}, headers=get_hdr())
    return r.json(), r.status_code

def get_hdr():
    return {'Authorization': f'Bearer {TOKEN}'} if TOKEN else {}
