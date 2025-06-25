import base64

# Midtrans sandbox credentials
SERVER_KEY = 'YOUR_SERVER_KEY'
CLIENT_KEY = 'YOUR_CLIENT_KEY'

def midtrans_auth_header():
    return {
        'Authorization': 'Basic ' + base64.b64encode((SERVER_KEY + ':').encode()).decode(),
        'Content-Type': 'application/json'
    }
