class FizzBuzz:

    


    def __init__(self, nom):
        self.nom = nom

    def affiche(self):
        result=""
        for i in range(1, 101):
            if i % 15 == 0:
                result+="FrisBee"
            elif i % 5 == 0:
                result+="Buzz"
            elif i % 3 == 0:
                result+="Fizz"
            else:
                result+=str(i)
        
        print(result)
        return result