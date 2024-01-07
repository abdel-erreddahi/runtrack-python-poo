class Personne:
    def __init__(self, age=14) -> None:
        self.age = age

    def afficherAge(self):
        print(f"J'ai {self.age} ans")
        return self.age

    def bonjour(self):
        return 'Bonjour'

    def Modifier_age(self, age_modifie) -> int:
        self.age = age_modifie
        return age_modifie

class Eleve(Personne):
    def allerEnCours(self):
        return "Je vais en cours"

    def afficherAge(self):
        super().afficherAge() 

class Professeur(Eleve):
    def __init__(self, matiereEnseignee) -> None:
        self.__cours = matiereEnseignee

    def enseigner(self):
        return "Le cours va commencer"

# Utilisation
print("ELEVE :")
eleve = Eleve()
eleve.Modifier_age(15)
eleve.afficherAge()

print("\nPROFESSEUR :")
professeur = Professeur("Maths")
print(professeur.bonjour())
print(professeur.allerEnCours())
professeur.Modifier_age(40)
professeur.afficherAge()