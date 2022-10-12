from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#                                        protocol + adapter,   user + pw chosen,   ip address/host : port (postgres default port is 5432),  databasee to connect to
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://trello_dev:password123@localhost:5432/trello"

db = SQLAlchemy(app)

class Card(db.Model):
    # define the table name for the db
    __tablename__= "cards"
    # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True)
    # Add the rest of the attributes.
    title = db.Column(db.String())
    description = db.Column(db.String())
    date = db.Column(db.Date())
    status = db.Column(db.String())
    priority = db.Column(db.String())

@app.route('/')
def index():
    return "hello"