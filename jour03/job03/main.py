class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} - {self.description} - Statut: {self.statut}"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        self.taches = [t for t in self.taches if t.titre != titre]

    def marquerCommeFinie(self, titre):
        for t in self.taches:
            if t.titre == titre:
                t.statut = "Terminée"
                break

    def afficherListe(self):
        return [str(tache) for tache in self.taches]

    def filterListe(self, statut):
        return [str(tache) for tache in self.taches if tache.statut == statut]


# Test du code
tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Réviser pour l'examen", "Relire les notes de cours")
tache3 = Tache("Faire du sport", "30 minutes de jogging")

liste_taches = ListeDeTaches()

liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

print("Liste initiale:")
print(liste_taches.afficherListe())

liste_taches.supprimerTache("Réviser pour l'examen")

print("\nListe après suppression d'une tâche:")
print(liste_taches.afficherListe())

liste_taches.marquerCommeFinie("Faire les courses")

print("\nListe après avoir marqué une tâche comme terminée:")
print(liste_taches.afficherListe())

taches_a_faire = liste_taches.filterListe("À faire")
print("\nTâches à faire:")
print(taches_a_faire)

