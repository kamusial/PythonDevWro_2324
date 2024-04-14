from dataclasses import dataclass
from pydantic import BaseModel


class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


@dataclass
class HumanData:
    name: str
    surname: str
    age: int
    [("name", str), ("surname", str), ("age", int)]

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __repr__(self):
        return str(self)


class Humantic(BaseModel):
    name: str
    surname: str
    age: int


ania = Human("Anna", "B", 23)
ania2 = HumanData("Anna", "B", 23)
ania3 = Humantic(name="Anna", surname="B", age="23")
print([ania, ania2, ania3])
print(type(ania3.age))
