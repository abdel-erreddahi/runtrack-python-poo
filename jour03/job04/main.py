class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        return f"{self.nom} (#{self.numero}) - Position: {self.position}\nButs: {self.buts_marques}\nPasses décisives: {self.passes_decisives}\nCartons jaunes: {self.cartons_jaunes}\nCartons rouges: {self.cartons_rouges}"


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        for joueur in self.joueurs:
            print(joueur.afficherStatistiques())
            print("\n")

    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe_decisive":
                    joueur.effectuerUnePasseDecisive()
                elif action == "carton_jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "carton_rouge":
                    joueur.recevoirUnCartonRouge()


# Création des joueurs
joueur1 = Joueur("Lionel Messi", 10, "Attaquant")
joueur2 = Joueur("Cristiano Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Neymar Jr", 11, "Milieu de terrain")

# Création des équipes
equipe1 = Equipe("Équipe A")
equipe2 = Equipe("Équipe B")

# Ajout des joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)

equipe2.ajouterJoueur(joueur3)

# Affichage des statistiques initiales des joueurs
print("Statistiques initiales des joueurs:")
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

# Simulation d'un match
print("\nSimulation d'un match:")
equipe1.mettreAJourStatistiquesJoueur("Lionel Messi", "but")
equipe1.mettreAJourStatistiquesJoueur("Cristiano Ronaldo", "passe_decisive")
equipe2.mettreAJourStatistiquesJoueur("Neymar Jr", "carton_jaune")

# Affichage des statistiques après le match
print("\nStatistiques après le match:")
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
