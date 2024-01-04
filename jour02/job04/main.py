class Student:

    
    def __init__(self, nom, prenom, numéro_detudiant, nb_de_credits) -> None:
        self.__name = nom
        self.__prenom = prenom
        self.__numero = numéro_detudiant
        self.__credits = nb_de_credits
        self.__level = self.studentEval()

    def get_credits(self):
        return self.__credits

    def add_credits(self, nb_de_credits_ajoute):
        self.__credits += nb_de_credits_ajoute
        self.__level = self.studentEval()

    def studentEval(self):
        appreciation = self.__credits
        if appreciation >= 90:
            return "Excellent"
        elif appreciation >= 80:
            return "Très bien"
        elif appreciation >= 70:
            return "Bien"
        elif appreciation >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def get_appreciation(self):
        return self.__level
    
    def studentInfo(self):
        print(f"Nom: {self.__name}")
        print(f"Prénom: {self.__prenom}")
        print(f"Id: {self.__numero}")
        print(f"Niveau: {self.__level}")

# Utilisation de la classe Student
etudiant = Student("John", "Doe", 145, 0)

# Ajout des crédits à l'étudiant
etudiant.add_credits(60)
etudiant.add_credits(10)
etudiant.add_credits(10)

# Afficher le nombre de crédits et l'appréciation
print("Le nombre de crédits de John Doe est de :", etudiant.get_credits())
etudiant.studentInfo()