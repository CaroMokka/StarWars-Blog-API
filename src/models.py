from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#TABLA USER
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True, default=True)

    def __repr__(self):
        return '<User %r>' % self.user_name

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(30), nullable=False)
    homeworld = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "gender": self.gender,
            "homeworld": self.homeworld,
            # do not serialize the password, its a security breach
        }    


#TABLA PLANETAS
class Planets(db.Model):  
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(30), nullable=False)
    diameter = db.Column(db.Integer)  
    climate = db.Column(db.String(80))
    terrain = db.Column(db.String(80))
    population = db.Column(db.Integer)

    def __repr__(self):
        return '<Planets %r>' % self.name  

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population
            
        }  

#TABLA NAVES
class Starships(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(80))
    manufacturer = db.Column(db.String(80))
    passengers = db.Column(db.Integer)

    def __repr__(self):
        return '<Starships %r>' % self.name 

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "passangers": self.passangers,
 
            
        }    
         