import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1 facile, 2 moyen, 3 difficile) : "))

    def lancerJeu(self):
        self.choisirNiveau()

        if self.niveau == 1:
            vie_joueur = 100
            vie_ennemi = 50
        elif self.niveau == 2:
            vie_joueur = 80
            vie_ennemi = 70
        elif self.niveau == 3:
            vie_joueur = 60
            vie_ennemi = 90

        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        self.deroulementPartie(joueur, ennemi)

    def verifierSante(self, personnage):
        if personnage.vie <= 0:
            print(f"{personnage.nom} a perdu!")
            return True
        return False

    def verifierGagnant(self, joueur, ennemi):
        if joueur.vie > ennemi.vie:
            print(f"{joueur.nom} a gagné!")
        elif joueur.vie < ennemi.vie:
            print("L'ennemi a gagné!")
        else:
            print("Match nul!")

    def deroulementPartie(self, joueur, ennemi):
        while True:
            joueur.attaquer(ennemi)
            if self.verifierSante(ennemi):
                break

            ennemi.attaquer(joueur)
            if self.verifierSante(joueur):
                break

        self.verifierGagnant(joueur, ennemi)


# Test du jeu
jeu = Jeu()
jeu.lancerJeu()
