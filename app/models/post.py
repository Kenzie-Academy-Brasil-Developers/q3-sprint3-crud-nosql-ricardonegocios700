from decimal import InvalidContext
from xml.dom import InvalidCharacterErr
import pymongo
from datetime import date, datetime
#__name__ = "post"
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