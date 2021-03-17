# the simplest flask application can fit in a single source file
from enum import unique
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)

def db_init():
    # if the database doesn't exist, create it an all associated entities
    db.drop_all()
    db.create_all()

    admin = User(username='admin', email='admin@awesome.xyz')
    guest = User(username='guest', email='guest@awesome.xyz')

    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()


@app.route("/")
def homepage():
    output = User.query.all()
    app.logger.debug(output)
    show = f"username 1: {output[0].username} | username 2: {output[1].username}"
    return str(show)


if __name__ == '__main__':
    db_init()
    app.run(debug=True)