"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Starships
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#GET ALL USERS
@app.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users))

    return jsonify(all_users), 200

#POST USER
@app.route('/user', methods=['POST'])
def create_user():
    request_body_user = request.get_json()
    user = User(user_name=request_body_user["user_name"], first_name=request_body_user["first_name"], last_name=request_body_user["last_name"], email=request_body_user["email"], password=request_body_user["password"])
    db.session.add(user)
    db.session.commit() 
    return jsonify("successfully registered"), 200 

#PUT USER 
@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    request_body_user = request.get_json()
    user = User.query.get(id)
    if user is None:
       raise APIException('User not found', status_code=404)

    if "user_name" in request_body_user:
        user.user_name = request_body_user["user_name"]
    if "email" in request_body_user:
        user.email = request_body_user["email"]
    db.session.commit()
    
    return jsonify("user updated successfully"), 200 

#DELETE USER
@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user is None:
       raise APIException('User not found', status_code=404)
    db.session.delete(user)
    db.session.commit()
  
    
    return jsonify("Deleted user"), 200         


#GET ALL PLANETS >>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    all_planets = list(map(lambda x: x.serialize(), planets))
   
    return jsonify(all_planets), 200


#POST PLANET >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/planets', methods=['POST'])
def create_planet():
    request_body_planets = request.get_json()
    planet = Planets(name=request_body_planets["name"], diameter=request_body_planets["diameter"], climate=request_body_planets["climate"], terrain=request_body_planets["terrain"], population=request_body_planets["population"])
    db.session.add(planet)
    db.session.commit() 
    return jsonify("Planet successfully registered"), 200    


#PUT PLANET >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/planets/<int:id>', methods=['PUT'])
def update_planet(id):
    request_body_planet = request.get_json()
    planet = Planets.query.get(id)
    if planet is None:
       raise APIException('Planet not found', status_code=404)

    if "name" in request_body_planet:
        planet.name = request_body_planet["name"]
    
    db.session.commit()
    
    return jsonify("user updated successfully"), 200



#DELETE PLANET >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/planets/<int:id>', methods=['DELETE'])
def delete_planet(id):
    planet = Planets.query.get(id)
    if planet is None:
       raise APIException('Planet not found', status_code=404)
    db.session.delete(planet)
    db.session.commit()
  
    
    return jsonify("Deleted planet"), 200 


#GET ALL CHARACTERS >>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/characters', methods=['GET'])
def get_characters():
    characters = Characters.query.all()
    all_characters = list(map(lambda x: x.serialize(), characters))
   
    return jsonify(all_characters), 200    


#POST CHARACTER >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/characters', methods=['POST'])
def create_character():
    request_body_characters = request.get_json()
    character = Characters(name=request_body_characters["name"], height=request_body_characters["height"], gender=request_body_characters["gender"], homeworld=request_body_characters["homeworld"])
    db.session.add(planet)
    db.session.commit() 
    return jsonify("Planet successfully registered"), 200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
