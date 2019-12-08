from flask_restful import Resource, reqparse
from flask import request
from werkzeug.security import safe_str_cmp
from database import user_db
import bcrypt as encoder
from models.user import UserModel
from flask_jwt import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('username', str, required=True, help="Username is required to login")
parser.add_argument('password', str, required=True, help="Password is required to login")

class UserRegistry(Resource):
    def post(self):
        payload = dict(parser.parse_args())
        username = payload['username']
        password = payload['password']
        if UserModel.find_by_username(username):
            return {"message" :"username is taken"}, 400
        user = UserModel.create_user(payload)
        user.save_to_db()
        user = user.get()
        return user, 201


class User(Resource):
    def get(self, name):
        user = UserModel.find_by_username(name)
        if user :
            return user.get(), 200
        return {"message": "User with given username does not exist"}, 404
     
    
#    def post(self):
        #payload = User.parser.parse_args()
        #user = UserModel.find_by_username(payload['username'])
        #if user and payload.get('password'):
        #    user.password = payload.get('password')
        #    user.update_to_db()
        #return {"message": "User does not exist in the database"}, 404
        
    
