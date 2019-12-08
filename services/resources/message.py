
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.user import UserModel


class MessageAdder(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("message", str, required=True, help="Message is required to call this API")
    parser.add_argument("username", str, required=True, help="Username is required to call this API")

    @jwt_required()
    def post(self):
        payload = MessageAdder.parser.parse_args()
        user = UserModel.find_by_username(payload['username'])
        if user:
            if user.use_allowance():
                user.add_message(payload['message'])
                user.update_to_db()
                return {"message" : "message is saved in the database successfully"}, 201
            else:
                return {"message" : "Limit of allowance reached"}, 405
        else:
            return {"message": "User does not exist"}, 404


        
