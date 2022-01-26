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
        #TODO verificar com calma as datas
        # self.created_at: date = kwargs["created_at"] or datetime.now()
        # self.updated_at: date = kwargs["updated_at"] or datetime.now()

    def save_post(self):
        db.post.insert_one(self.__dict__)
        return self

    def update_to(self, params):
        print("================================", self.__dict__)
        if params['title'] != self.title:
            self.title = params['title']
        if params['author'] != self.author:
            self.author = params['author']
        if params['tags'] != self.tags:
            self.tags = params['tags']
        if params['content'] != self.content:
            self.content = params['content']
        db.post.update_one(self.__dict__)
        #return self

    @staticmethod
    def delete_post(post):
        db.post.delete_one({"id": post["id"]})
    # def delete_post(post):
    #     db.post.delete_one(post)

    @staticmethod
    def find_post(id):
        result = db.post.find_one({"id": int(id)})
        return result

    @staticmethod
    def list_all():
        working = db.post.find()
        #TODO não consegui usar o serialize_id() no controller
        #TODO mantinha como um objeto do mongo e não interava no controller
        #TODO https://github.com/Kenzie-Academy-Brasil-Developers/q3-demos-turma7/blob/master/sprint3/demo7/app/models/dev_model.py
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
    

# p = Post(
#     **{
#         "id": 1,
#         "title": "Titulo",
#         "author": "Ricardo Silva",
#         "tags": ["python", "mongoDB", "postgreSQL"],
#         "content": "Aqui vai um texto, com o conteudo da postagem"
#     }
# )
# print(type(p))
# print(p)
# print(p.__dict__)
# print(p.save_post())

# dict_object = {
#         "id": 1,
#         "title": "Titulo",
#         "author": "Ricardo Silva",
#         "tags": ["python", "mongoDB", "postgreSQL"],
#         "content": "Aqui vai um texto, com o conteudo da postagem"
#     }
#p = Post(**dict_object)