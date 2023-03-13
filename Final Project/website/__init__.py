from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

DB_NAME = "database.db" 
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "yoyoyo"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from .views import views
    from .models import User, Post, Comment, Like
    from .auth import auth

    app.register_blueprint(views, url_prefix= "/")
    app.register_blueprint(auth, url_prefix= "/")

    
    # create_database(app)

    login_manager = LoginManager()
    login_manager.login_view= "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    with app.app_context():
        db.create_all()

    return app