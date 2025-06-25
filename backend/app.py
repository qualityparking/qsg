from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from routes.auth_routes import auth_bp
from routes.parking_routes import parking_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
jwt = JWTManager(app)

import models.user
import models.parking

app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(parking_bp, url_prefix='/api/parking')

if __name__ == '__main__':
    app.run(debug=True)
