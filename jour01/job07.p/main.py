class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def bas(self):
        self.y += 1

    def haut(self):
        self.y -= 1

    def position(self):
        return (self.x, self.y)

# Exemple d'utilisation de la classe Personnage
personnage = Personnage()

# Déplacer le personnage et afficher la position
personnage.droite()
personnage.bas()
print("Position du personnage:", personnage.position())
