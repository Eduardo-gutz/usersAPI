from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/eduardo-gutz/Escritorio/python/src/db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    additionalName = db.Column(db.String(20))
    lastName = db.Column(db.String(20))
    secondLastName = db.Column(db.String(20))
    age = db.Column(db.Integer)
    birthDate = db.Column(db.String(10))

    def __init__(self, name, additionalName, lastName, secondLastName, age, birthDate):
        self.name = name
        self.additionalName = additionalName
        self.lastName = lastName
        self.secondLastName = secondLastName
        self.age = age
        self.birthDate = birthDate

db.create_all()

class UserSchema(ma.Schema): 
    class Meta:
        fields = ('id', 'name', 'additionalName', 'lastName', 'secondLastName', 'age', 'birthDate')

user_schema = UserSchema()
users_schema = UserSchema(many = True)

@app.route('/user', methods=['POST'])
def create_user():
    name = request.json['name']
    additionalName = request.json['additionalName']
    lastName = request.json['lastName']
    secondLastName = request.json['secondLastName']
    age = request.json['age']
    birhtDate = request.json['birthDate']

    new_user = User(name, additionalName, lastName, secondLastName, age, birhtDate)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

@app.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)

    return jsonify(result)

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)

    return user_schema.jsonify(user)

@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)

    user.name = request.json['name']
    user.additionalName = request.json['additionalName']
    user.lastName = request.json['lastName']
    user.secondLastName = request.json['secondLastName']
    user.age = request.json['age']
    user.birthDate = request.json['birthDate']

    db.session.commit()

    return user_schema.jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
