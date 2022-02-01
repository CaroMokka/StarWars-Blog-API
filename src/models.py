from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#TABLA USER >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
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
            "user_id": self.user_id,
            "user_name": self.user_name,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
#TABLA CHARACTERS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
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


#TABLA PLANETS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class Planets(db.Model):  
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(30), nullable=False)
    diameter = db.Column(db.Integer, nullable=False)  
    climate = db.Column(db.String(80), nullable=False)
    terrain = db.Column(db.String(80), nullable=False)
    population = db.Column(db.Integer, nullable=False)

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

#TABLA STARSHIPS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class Starships(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, nullable=False)
    model = db.Column(db.String(80), nullable=False)
    manufacturer = db.Column(db.String(80), nullable=False)
    passengers = db.Column(db.Integer, nullable=False)

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
         

#TABLA FAVORITES >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, nullable=False)
    character_id = db.Column(db.Integer, nullable=False)
    planet_id = db.Column(db.Integer, nullable=False)
    starship_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer)

    def __repr__(self):
        return '<Favorites %r>' % self.user_id 

    def serialize(self):
        return {
            "id": self.id,
            "user_idr": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "starship_id": self.starship_id,
            "quantity": self.quantity,
 
            
        }







