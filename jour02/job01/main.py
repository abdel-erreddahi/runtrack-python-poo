class rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur= longueur
        self.__largeur= largeur

    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, longueur_modifie):
        self.__longueur = longueur_modifie    
    def set_largeur(self, largeur_modifie):
        self.__largeur = largeur_modifie 
        
Rectangle = rectangle(10,5)

print("longueur initiale", Rectangle.get_longueur())
print("largeur initiale", Rectangle.get_largeur())

Rectangle.set_longueur(15)
Rectangle.set_largeur(7)

print("longueur modifie",Rectangle.get_longueur())
print("largeur modifie",Rectangle.get_largeur())
    
    
  

