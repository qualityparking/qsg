from flask import Flask
from flask_cors import CORS
from database import init_db
from routes.payment_routes import payment_bp

app = Flask(__name__)
CORS(app)

# DB
init_db(app)

# Routes
app.register_blueprint(payment_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
