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
from models import db, User, Characters, Planets, Starships, Favorites
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

#GET ALL USERS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users))

    return jsonify(all_users), 200

#GET A USER >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/user/<int:id>', methods=['GET'])
def get_a_user(id):
    user = User.query.get(id)
    print(id)
    if user is None:
       raise APIException('User not found', status_code=404)

    return jsonify(user.serialize()), 200



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
    db.session.add(character)
    db.session.commit() 
    return jsonify("Character successfully registered"), 200


#PUT CHARACTER >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/characters/<int:id>', methods=['PUT'])
def update_character(id):
    request_body_character = request.get_json()
    char = Characters.query.get(id)
    if char is None:
       raise APIException('Character not found', status_code=404)

    if "name" in request_body_character:
        char.name = request_body_character["name"]
    
    db.session.commit()
    
    return jsonify("Character updated successfully"), 200

#Delete CHARACTER >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
    character = Characters.query.get(id)
    if character is None:
       raise APIException('Character not found', status_code=404)
    db.session.delete(character)
    db.session.commit()
  
    
    return jsonify("Deleted character"), 200


#GET ALL STARSHIPS >>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/starships', methods=['GET'])
def get_starships():
    starships = Starships.query.all()
    all_starships = list(map(lambda x: x.serialize(), starships))
   
    return jsonify(all_starships), 200

#POST STARSHIPS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/starships', methods=['POST'])
def create_starship():
    request_body_starships = request.get_json() #recibes request
    starship = Starships(name=request_body_starships["name"], model=request_body_starships["model"], manufacturer=request_body_starships["manufacturer"], passengers=request_body_starships["passengers"]) #remplaza los datos de los campos
    db.session.add(starship)
    db.session.commit() 
    return jsonify("Starship successfully registered"), 200

#PUT STARSHIPS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/starships/<int:id>', methods=['PUT'])
def update_starship(id):
    request_body_starships = request.get_json() #Obtengo los datos nuevo en un json

    starship = Starships.query.get(id) #valor actual

    if starship is None:
       raise APIException('Starship not found', status_code=404)

    if "name" in request_body_starships:
        starship.name = request_body_starships["name"] #valor nuevo
        
    
    db.session.commit()
    
    return jsonify("Starship updated successfully"), 200


#DELETE STARSHIP >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/starships/<int:id>', methods=['DELETE'])
def delete_starship(id):
    starship = Starships.query.get(id)
    if starship is None:
       raise APIException('Starship not found', status_code=404)
    db.session.delete(starship)
    db.session.commit()
  
    
    return jsonify({"msg":"Deleted starship"}), 200

#Get FAVORITES >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/favorites', methods=['GET'])
def get_favorites():
    favorites = Favorites.query.all()
    all_favorites = list(map(lambda x: x.serialize(), favorites))
   
    return jsonify(all_favorites), 200

#POST FAVORITES opcion 1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/favorites', methods=['POST'])
def add_to_favorite():
    request_body_fav = request.get_json()
    print(request_body_fav)
    #user = request_body_fav["user_id"]
    #print(user)
    fav_user = Favorites(user_id=request_body_fav["user_id"])
  
    db.session.add(fav_user)
    db.session.commit()
    print(fav_user.user)
    
    

    return jsonify("ok"), 200

#POST FAVORITES >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
""" @app.route('/favorites', methods=['POST'])
def add_to_favorite():
    request_body_fav = request.get_json()
    favorite = Favorites(user_id=request_body_fav["user_id"], character_id=request_body_fav["character_id"], planet_id=request_body_fav["planet_id"], starship_id=request_body_fav["starship_id"])
    db.session.add(favorite)
    db.session.commit()
    return jsonify({"msg": "Favorite successfully created"}), 200 """

    
            
""" @app.route("/favorites", methods=["POST"])
def add_favorites():
    nfavorite = Favorites()
    nfavorite.planets_id = request.json['planet_id']
    nfavorite.characters_id = request.json['character_id']
    nfavorite.user_id  = request.json['user_id']
    db.session.add(nfavorite)
    db.session.commit()
    return jsonify({"msg": "Favorite successfully created"}), 200 """



















































# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
