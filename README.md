# Database as a service (python-mongo example)
This program allows user to create database as a service which in simpler means it exposes certain end points which enable user to store and maintain information inside the service
Do let me know if you need any more information or have any doubt

#### Contact detail
**email** : kmalik1122@gmail.com

#### Python libraries
1. Flask
2. Flask-restful
3. Flask-JWT
4. pymongo
5. bcrypt

## Instruction

first clone the repository to your local folder, then follow the gi>

```
docker-compose build
docker-compose up
```

If you want to test the service in the docker environment - please make the following change

1. In the database.py - change the name of the MongoClient from "mongodb://localhost:271017" to mongodb://db:271017". Also if you want to use a hosted mongoDb server, then simply change the url and the rest of the program will work fine. 




