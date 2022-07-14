from urllib.parse import non_hierarchical


class Ninja:

    def __init__ (self, data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.pet = None
        self.treats = []
        self.pet_food = "Dry Food"


    def add_pet (self, pet):
        self.pet= pet
        return self
    
    def walk (self):
        self.pet = self.pet.play()
        return self

    def feed(self):
        self.pet = self.pet.eat()
        return self

    def bathe(self):
        self.pet = self.pet.noise()