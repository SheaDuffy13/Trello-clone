from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

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
    title = db.Column(db.String(100))   #Can pass number in () to set max num characters
    description = db.Column(db.Text())
    date = db.Column(db.Date())
    status = db.Column(db.String())
    priority = db.Column(db.String())

# Define a custom CLI (terminal) command. Run with "flask create" in terminal.
@app.cli.command('create')
def create_all():
    db.create_all()
    print("Tables created")

@app.cli.command("seed")
def seed_db():
    card = Card(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        title = "Start the project",
        description = "Stage 1, creating the database",
        status = "To Do",
        priority = "High",
        date = date.today()
    )
    # Add the object as a new row to the table
    db.session.add(card)
    # commit the changes
    db.session.commit()
    print("Table seeded")

@app.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")

@app.route('/')
def index():
    return "hello"