class Personne:


    def __init__(self, age = 14) -> None:
        self.age = age
        pass

    def Age(self):
        return self.age

    def afficherAge(self):
        print(self.age)
        return self.age

    def bonjour(self):
        return 'Hello'
    
    def Modifier_age(self, age_modifie) -> int:
        self.age = age_modifie


class Eleve(Personne):

    def allerEnCours(self):
        return "Je vais en cours"
    
    def afficherAge(self):
        print(f"J'ai {self.age} ans")
    
class Professeur:

    def __init__(self, matiereEnseignée,) -> None:
        self.__cours = matiereEnseignée
        pass

    def enseigner(self):
        return "Le cours va commencer"


personne = Personne()
personne.afficherAge()
print(personne.bonjour())

eleve = Eleve()
eleve.afficherAge()