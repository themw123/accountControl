import pymongo


class Mongodb:

    def __init__(self):
        try:
            self.client = pymongo.MongoClient(
                "mongodb+srv://marv:***REMOVED***@cluster0.4ejve.mongodb.net/?retryWrites=true&w=majority")
            self.db = self.client["account"]
        except:
            print("!!!connection to database failed!!!")
            exit()

    def set_collection(self, collection):
        self.collection = self.db[collection]

    def insert(self, data):
        self.collection.insert_one(data)

    def find(self, query):
        cursor = self.collection.find(query)
        return cursor

    def find_one(self, query):
        return self.collection.find_one(query)

    def update(self, query, update):
        """ query = {"name": "John Doe"}
        update = {"$set": {"age": 43}}
        result = self.collection.update_one(query, update)
        print(result.modified_count) """
        pass

    def delete(self, query):
        """ query = {"name": "John Doe"}
        result = self.collection.delete_one(query)
        print(result.deleted_count) """
        pass
