from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/flask_sample'
    
    db.init_app(app)

    # 認証済みルートのBlueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # 未認証ルートのBlueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app