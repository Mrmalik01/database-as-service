from models.user import UserModel
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and  user.passwordCheck(password):
        return user

def identity(payload):
    return UserModel.find_by_id(payload['identity'])


   

