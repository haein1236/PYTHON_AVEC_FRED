class Voiture:

    def __init__(self, marque, modele, annee, km):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.km = km

    def afficher(self):
        print(self.marque, self.modele, self.annee, self.km, "km")


class VoitureElectrique(Voiture):

    def __init__(self, marque, modele, annee, km, autonomie):
        super().__init__(marque, modele, annee, km)
        self.autonomie = autonomie

    def afficher(self):
        super().afficher()
        print("Autonomie :", self.autonomie, "km")
