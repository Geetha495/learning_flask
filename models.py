from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class User(db.Model):
        __tablename__ = 'users'
        uid = db.Column(db.Integer,primary_key = True)
        firstname = db.Column(db.String(100))
        lastname = db.Column(db.String(100))
        email = db.Column(db.String(120),unique=True)
        pwdhash = db.Column(db.String(100))
        
        def __init__(self,firstname,lastname,email,pwd):
                self.firstname = firstname.title()
                self.lastname = lastname.title()
                self.email = email.lower()
                self.set_password(pwd)
        
        def set_password(self,pwd):
                self.pwdhash = generate_password_hash(pwd)
                
        def check_password(self,hshpwd):
                return check_password_hash(self.pwdhash,hshpwd)
        
                
        
        
        
        
        
        
        