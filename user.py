# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL


# model the class after the friend table from our database
class Users:
    def __init__(self, data):
        self.id = data["idusers"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL("users_schema").query_db(query)
        # print("results :", results)
        # Create an empty list to append our instances of friends
        users_Arr = []
        # Iterate over the db results and create instances of friends with cls.
        for one_user in results:
            users_Arr.append(cls(one_user))
            print(cls(one_user))
        return users_Arr
    

    @classmethod
    def create_user(cls, datas):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(eml)s, NOW(), NOW());"

        # datas is a dictionary that will be passed into the save method from server.py
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL("users_schema").query_db(query, datas)

    # print("results :", results)
    # return results # results == id du users crée
