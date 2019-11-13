from decouple import config
from flask import Flask, render_template, request
from .models import DB, User, Tweet

#now we make a app factory

def create_app():
    app = Flask(__name__)

    #add our config
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #now have the database know about the app
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)

    @app.route('/user/<name>')
    def user(name):
        tweets = Tweet.query.filter(User.name == name).tweets
        return render_template('tweets.html', title='tweets', tweets=tweets)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset', users=[])
    return app