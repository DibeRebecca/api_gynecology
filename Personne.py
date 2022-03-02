class Personne:
    def __init__(self, id, nom, prenom, date_de_naissance, adresse, contact, age, sexe ) -> None:
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.contact = contact
        self.adresse = adresse
        self.age = age
        self.sexe = sexe

    @property
    def nom(self, nom) -> str:
        return self.nom

    @nom.setter
    def nom(self,nom) -> None:
        self.nom = nom

    @property
    def prenom(self, prenom) -> str:
        return self.prenom

    @prenom.setter
    def prenom(self, prenom) -> None:
        self.prenom = prenom

    @property
    def date_de_naissance(self, date_de_naissance) -> str:
        return self.date_de_naissance

    @date_de_naissance.setter
    def date_de_naissance(self, date_de_naissance) -> None:
        self.date_de_naissance = date_de_naissance

    @property
    def contact(self, contact) -> str:
        return self.contact

    @contact.setter
    def contact(self, contact) -> None:
        self.contact = contact
    
    @property
    def adresse(self) -> str:
        return self.adresse

    @adresse.setter
    def adresse(self,adresse ) -> None:
        self.adresse = adresse
    
        
        