from flask import Flask, request, jsonify
from flask_restful import Api
from pymongo import MongoClient
from resources.user import UserRegistry, User
from resources.message import MessageAdder
from database import user_db
from flask_jwt import JWT
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "mongo!2dsdv#R$@T4fewf#$#!"
api = Api(app)
jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegistry, "/register")
api.add_resource(User, "/user/<string:name>")
api.add_resource(MessageAdder, "/user/message")


if __name__ == "__main__":
    app.run(debug=True)
    
