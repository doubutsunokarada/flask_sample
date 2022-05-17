from flask import Flask, make_response, jsonify
from flask_cors import CORS
from .database import db

def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
        'user': 'user',
        'password': 'password',
        'host': '10.254.249.2',
        'db_name': 'flask_sample'
    })

    db.init_app(app)

    # 認証済みルートのBlueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # 未認証ルートのBlueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

app = create_app()