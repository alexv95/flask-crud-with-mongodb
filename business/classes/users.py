from business.DbConnector.connector import BDConnector


class UserDocument(BDConnector):
    def __init__(self):
        BDConnector.__init__(self)
        self.collection = self.db.users

    def insertUser(self, params):
        try:
            self.collection.insert(params)
            return True
        except:
            return False

    def updateUser(self, find_param, params):
        try:

            self.collection.update_one(
                modify_param, {"$set": params}, upsert=False)
            return True
        except:
            return False

    def deleteUser(self, delete_param):
        try:

            self.collection.delete_one(
                delete_param)
            return True
        except:
            return False

    def findAllUsers(self):
        try:
            self.collection.find(
                delete_param)
            return True
        except:
            return False
