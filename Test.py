class FizzBuzz:

    #def __init__(self, nom) -> None:
        #self.nom = nom
    
    #def factorielle(self):
        #return (120)


    def __init__(self, start=1, end=100):
        self.start = start
        self.end = end

    def affiche(self):
        for i in range(self.start, self.end + 1):
            if i % 15 == 0:
                print("Frisbee")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)