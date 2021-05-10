# Hacer una tabla de la "familia general"

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Current(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.String(120), unique=True, nullable=False)
    reference = db.Column(db.String(120), unique=True, nullable=False)
    parents= db.Column(db.Integer, db.ForeignKey('parent.id'),
        nullable=False)
    def __repr__(self):
        return '<Current %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "age": self.age,
            "reference": self.reference,
        }

class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.String(120), unique=True, nullable=False)
    reference = db.Column(db.String(120), unique=True, nullable=False)
    children = db.relationship('Current',backref='parent', lazy=True) 

    def __repr__(self):
        return '<Parent %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "age": self.age,
            "reference": self.reference,     
        }


class Grandparent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.String(120), unique=True, nullable=False)
    reference = db.Column(db.String(120), unique=True, nullable=False)
    # parents= db.Column(db.Integer, db.ForeignKey('parent.id'),
    # children = db.relationship('Parent',backref='grandparent', lazy=True) 

    def __repr__(self):
        return '<Grandparent %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "age": self.age,
            "reference": self.reference,    
        }        


         