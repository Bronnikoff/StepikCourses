import json

class Pet:
    count = 0
    def __init__(self, name = None):
        print("Pet", "here!")
        self.name = name
        Pet.count += 1
    def __del__(self):
        Pet.count -= 1

class Dog(Pet):
    def __init__(self, name = None, breed = None):
        print("Dog here!")
        super().__init__(name)
        self.breed = breed

    def say(self):
        return "{0}: waw".format(self.name)

class ExportJSON:
    def to_json(self):
        return json.dumps({"name": self.name, "breed": self.breed})

class UpgradeDog(Dog, ExportJSON):
    def __hash__(self):
        return None

class WoolenDog(Dog, ExportJSON):
    def __init__(self, name = None):
        super(Dog, self).__init__()
        self.breed = "Woolen"


pesik = UpgradeDog("Richard III", "Доберман")
print(id(pesik))
pesik.name = "Lui II"
print(id(pesik))
dogger = pesik
print(id(dogger))
pesik.name = "Lui III"
print(dogger.name)
