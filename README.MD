# Flask SQLAlchemy Tutorial

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) is a "micro" web application framework. [Flask Tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/) and [my repo](https://github.com/ahuimanu/flask-tutorial) covering it.
- [SQLAlchemy](https://docs.sqlalchemy.org/en/14/) is an O/RM for Python. [SQLAlchemy Tutorial](https://docs.sqlalchemy.org/en/14/tutorial/index.html#unified-tutorial)

[Here is a handy source for Python](https://github.com/github/gitignore/blob/master/Python.gitignore) `.gitignore` files.

## Quick Start

Assuming some understanding of Flask and SQLAlchemy, it is possible to get right down to it.

Primarily, the [Flask-SQLAlchemy extension](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) provides the opportunity to use the [SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.SQLAlchemy) class in our projects.

The minimal shell:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
```

As of March 2021, it is important to remain with SQLAlchemy version 1.3.x in order for flask_sqlalchemy to work.
