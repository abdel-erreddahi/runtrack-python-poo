class voiture:
    def __init__(self, marque, modele, annee, kilometrage,) -> None:
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoire = 50
        
        pass
    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_kilometrage(self):
        return self.__kilometrage
    
    def get_en_marche(self):
        return self.__en_marche
        
    def en_marche(self):
        return self.__en_marche


    def set_modele(self, modele_modifie):
        self.__modele = modele_modifie
    
    def set_annee(self, annee_modifie):
        self.__annee = annee_modifie
    
    def set_kilometrage(self, kilometrage_modifie):
        self.__kilometrage = kilometrage_modifie
    
    def set_en_marche(self, en_marche_modifie):
        self.__en_marche = en_marche_modifie
    
    def demarrer(self):
        if self.get_verifier_plein() > 5:
            self.en_marche = True
            print("La voiture peut se demarer :")
            return True
        else:
            print("Le réservoir est trop bas, veuillez faire le plein :")
        return False


    def arreter(self):
        if self.en_marche:
            self.en_marche = False
            return False
        
    def get_verifier_plein(self):
        return self.__reservoire
    
    def set_verifier_plein(self, reserve):
        self.__reservoire = reserve

    
    def InfosVoiture(self):
        print("Informations sur la voiture :")
        print(f"Marque : {self.get_marque()}")
        print(f"Modèle : {self.get_modele()}")
        print(f"Année : {self.get_annee()}")
        print(f"Kilométrage : {self.get_kilometrage()} km")



    
Voiture = voiture('mustang', 'modele 2024', 2024, '250 km')

Voiture.set_verifier_plein(7)

# Afficher les informations de la voiture
Voiture.InfosVoiture()

# Démarrer la voiture
print(Voiture.demarrer())





        