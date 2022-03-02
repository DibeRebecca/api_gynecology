class Medecin:
    def __init__(self, id, nom, prenom, contact) -> None:
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.contact = contact

    @property
    def nom(self, nom) -> str:
        return self.nom

    @nom.setter
    def nom(self,nomm) -> None:
        self.nom = nomm

    @property
    def prenom(self, prenom) -> str:
        return self.prenom

    @nom.setter
    def prenom(self,prenomm) -> None:
        self.prenom = prenomm

    @property
    def contact(self, contact) -> str:
        return self.contact

    @contact.setter
    def contact(self,contact) -> None:
        self.contact = contact

    