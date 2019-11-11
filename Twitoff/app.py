from flask import Flask
from .models import DB

#App Factory
def create_app():
    app = Flask(__name__)

    #Add config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    #now have the database know about the app
    DB.init_app(app)

    @app.route('/')
    def root():
        return 'Welcome to Twitoff'
    return app