from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from flask_jwt_extended import JWTManager

from controllers.user_controller import user_bp
from controllers.travel_controller import travel_bp
from infra.db.database import db


def get_db_password():
    """Lire le mot de passe depuis le secret du docker-compose."""
    with open('/run/secrets/db_password', 'r') as file:
        return file.read().strip()


app = Flask(__name__)
load_dotenv(".flaskenv")

api_key = os.getenv('API_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg://{os.getenv('DB_USER')}:{get_db_password()}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = api_key

jwt = JWTManager(app)
cors = CORS(app)

db.init_app(app)


app.register_blueprint(user_bp, url_prefix='/auth')
app.register_blueprint(travel_bp, url_prefix='/travel')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
