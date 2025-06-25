from flask import Flask
from flask_cors import CORS
from routes.payment_routes import payment_bp

app = Flask(__name__)
CORS(app)

# Register route
app.register_blueprint(payment_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
