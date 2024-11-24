from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from flask_jwt_extended import JWTManager

from controllers.user_controller import user_bp

app = Flask(__name__)
load_dotenv(".flaskenv")

api_key = os.getenv('API_KEY')

app.config['JWT_SECRET_KEY'] = api_key
jwt = JWTManager(app)

cors = CORS(app)

app.register_blueprint(user_bp, url_prefix='/auth')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
