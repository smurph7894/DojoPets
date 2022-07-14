import pet

class Bird(pet.Pet):
    
    def __init__(self, data):
        super().__init__(data)
        self.type = "Bird" 

    def noise(self):
            print("Chirp, Chirp")
            return self