class Pet:

    def __init__(self, data):
        self.name = data["name"]
        self.tricks = []
        self.health = 100
        self.energy = 80


    def sleep (self):
        self.energy = self.energy + 25
        print(f"{self.name} took a nap. Their energy is now {self.energy}")
        return self

    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10
        print(f"{self.name} took ate. Their energy is now {self.energy} and health is now {self.health}")
        return self

    def play(self):
        self.health = self.health + 5
        print(f"{self.name} played. Their health is now {self.health}")
        return self

    def noise(self):
        print("noise")
        return self