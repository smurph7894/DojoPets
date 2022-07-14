import pet

class Cat(pet.Pet):
    
    def __init__(self, data):
        super().__init__(data)
        self.type = "Cat" 


    def noise(self):
        print("Meeeeooooooowwwwww, hiss")
        return self

