class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

# Instanciation de la classe Animal
mon_animal = Animal()

# Affichage de l'âge initial
print(f"l'age de l'animal  {mon_animal.age} ans")

# Faire vieillir l'animal
mon_animal.vieillir()

# Affichage de l'âge après avoir vieilli
print(f"L'age de l'animal  {mon_animal.age} ans")
class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

# Instanciation de la classe Animal
mon_animal = Animal()

# Utilisation de la méthode nommer pour donner un nom à l'animal
mon_animal.nommer("Luna")

# Affichage du nom de l'animal
print(f" L'animal se nomme {mon_animal.prenom}")

