# Hacer una tabla de la "familia general"

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Current(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    parents= db.Column(db.Integer, db.ForeignKey('parent.id'),
        nullable=False)
    def __repr__(self):
        return '<Current %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    children = db.relationship('Current',backref='parent', lazy=True) 

    def __repr__(self):
        return '<Parent %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }
         