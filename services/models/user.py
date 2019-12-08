from database import user_db
import bcrypt as encoder
from bson.objectid import ObjectId

class UserModel:
    def __init__(self, username, password, id=None, allowance=100, messages=[]):
        self.id = id
        self.username = username
        self.password = self.encoder(password)
        self.allowance = allowance
        self.messages = messages
        self.password = self.encoder(password)
        
    def encoder(self, password):
        return encoder.hashpw(str(password).encode("utf8"), encoder.gensalt())

    def json(self):
        return {
            "username":self.username,
            "password":self.password,
            "total_allowance":self.allowance,
            "messages":self.messages
        }
    def get(self):
        return {
            "username" :self.username,
            "total_allowance":self.allowance,
            "messages":self.messages
        }
        
    def save_to_db(self):
        user_db.insert(self.json())
        self._update_values()
        return True

    def update_to_db(self):
        user_db.update({"username":self.username},{"$set":self.json()})
        self._update_values()
        return True
        
    def _update_values(self):
        user = list(user_db.find({"username":self.username}))
        self.username = user[0]['username']
        self.id = user[0]['_id']
        self.password = user[0]['password']
        self.allowance = user[0]['total_allowance']
        return True
        
    def delete_from_db(self):
        user_db.remove({"username":self.username})
        return True

    def passwordCheck(self, password):
        if self.encoder(password) == self.password:
            return True
        return False

    def use_allowance(self):
        if self.allowance == 0:
            return False
        self.allowance-=1
        return True

    def add_message(self, message):
        self.messages.append(message)
        return True

    @classmethod
    def create_user(cls, payload):
        if "allowance" in payload and "messages" in payload:
            return cls(payload['username'], payload['password'], payload['allowance'], payload['messages'])
        return cls(payload['username'], payload['password'])
        
    @classmethod
    def find_by_username(cls, username):
        user = list(user_db.find({"username":username}))
        print(user)
        if user and len(user)>0:
            return cls(user[0]['username'], user[0]['password'], id=user[0]['_id'])
        return None

    @classmethod
    def find_by_id(cls, id):
        user = list(user_db.find({"_id" : ObjectId(self.id)}))
        if user and len(user)>0:
            return cls(user[0]['username'], user[0]['password'], user[0]['_id'])
        return None
