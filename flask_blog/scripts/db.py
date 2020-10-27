#flask_blog/scripts/db.py

from flask_script import Command
from flask_blog import db

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()
