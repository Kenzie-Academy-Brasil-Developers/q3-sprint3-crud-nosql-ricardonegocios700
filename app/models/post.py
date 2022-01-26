from genericpath import exists
from turtle import title
import pymongo
from datetime import date, datetime


client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["atividade9"]

class Post():
    def __init__(self, **kwargs) -> None:
        self.id: int = self.new_id()
        self.title: str = kwargs["title"]
        self.author: str = kwargs["author"]
        self.tags: list[:str] = kwargs["tags"]
        self.content: str = kwargs["content"]

    def save_post(self):
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        db.post.insert_one(self.__dict__)
        return self

    @staticmethod
    def update_to(id, my_json):
        my_json["updated_at"] = datetime.today()
        db.post.update_one({"id": id}, {"$set": my_json})

    @staticmethod
    def delete_post(post):
        db.post.delete_one({"id": post["id"]})
        # db.post.delete_one(post) # funcionava e parou de funcinar...

    @staticmethod
    def find_post(id):
        result = db.post.find_one({"id": int(id)})
        return result

    @staticmethod
    def list_all():
        working = db.post.find()
        result = []
        for w in working:
            w.update({"_id": str(w["_id"])})
            result.append(w)
        return result

    def verify_title(self, title):
        if len(title) < 3:
            raise Exception("Tamanho inválido, título deve ter mais que 3 caracteres")
        return title

    @staticmethod
    def all_post() -> list:
        return db.post.find()

    @classmethod
    def new_id(cls) -> int:
        result = 0
        for t in cls.all_post():
            if result < t['id']:
                result = t['id']
        return(result+1)

    @staticmethod
    def serialize_id(data):
        if type(data) is dict:
            data.update({"_id": str(data["_id"])})
        if type(data) is Post:
            data._id = str(data._id)
        return data
    