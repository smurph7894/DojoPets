import pet

class Dog(pet.Pet):
    
    def __init__(self, data):
        super().__init__(data)
        self.type = "Dog" 


    def noise(self):
        print("Woof")
        return self

