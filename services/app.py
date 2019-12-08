from flask import Flask, request, jsonify
from flask_restful import Api
from pymongo import MongoClient
from resources.user import UserRegistry
from database import user_db

app = Flask(__name__)
api = Api(app)


api.add_resource(UserRegistry, "/register")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
