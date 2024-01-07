import random

class Carte:
    def __init__(self, valeur, couleur) -> None:
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self) -> None:
        self.paquet = self.creer_paquet()
    
    def creer_paquet(self):
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        return paquet
    
    def melanger_paquet(self):
        random.shuffle(self.paquet)
    
    def tirer_carte(self):
        if len(self.paquet) == 0:
            print("Le paquet est vide.")
            return None
        return self.paquet.pop()
    
    def valeur_main(self, main):
        valeur = 0
        as_present = False

        for carte in main:
            if carte.valeur.isdigit() or carte.valeur in ['10', 'Valet', 'Dame', 'Roi']:
                valeur += 10
            elif carte.valeur == 'As':
                as_present = True
                valeur += 1 
            else:
                valeur += int(carte.valeur)

        if as_present and valeur + 10 <= 21:
            valeur += 10 

        return valeur


jeu_blackjack = Jeu()
jeu_blackjack.melanger_paquet()

main_joueur = [jeu_blackjack.tirer_carte(), jeu_blackjack.tirer_carte()]
main_croupier = [jeu_blackjack.tirer_carte(), jeu_blackjack.tirer_carte()]

print("Main du joueur :", [carte.valeur for carte in main_joueur])
print("Main du croupier :", [carte.valeur for carte in main_croupier])

# On peut continuer à developper le jeu si on veut ...