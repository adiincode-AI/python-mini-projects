class User:
    def __init__(self, name, phonenumber):
        self.name = name
        self.phonenumber = phonenumber

    def to_dict(self):
        return {
            "name": self.name,
            "phonenumber": self.phonenumber
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(
            data["name"],
            data["phonenumber"]
        )
        return user
    
class Book:
    def __init__(self, title, author,is_available = True):
        self.title = title.lower().strip()
        self.author = author.lower().strip()
        self.is_available = is_available

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "is_available": self.is_available 
        }

    @classmethod
    def from_dict(cls, data):
        book = cls(
            data["title"],
            data["author"],
            data["is_available"]
        )
        return book
