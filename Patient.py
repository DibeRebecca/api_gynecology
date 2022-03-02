from Personne import Personne

class Patient(Personne):
    def __init__(self, id, nom, prenom, date_de_naissance, adresse, contact, age, sexe, poids, pression_arterielle,groupe_sanguin, temperature, poul) -> None:
        super().__init__(id, nom, prenom, date_de_naissance, adresse, contact, age, sexe)
        self.id = id
        self.pression_arterielle = pression_arterielle
        self.temperature = temperature
        self.groupe_sanguin = groupe_sanguin
        self.poul = poul

    @property
    def pression_arterielle(self, pression_arterielle) -> str:
        return self.pression_arterielle

    @pression_arterielle.setter
    def pression_arterielle(self, pression_arterielle ) -> None:
        self.pression_arterielle = pression_arterielle

    @property
    def temperature(self, temperature) -> str:
        return self.contact

    @temperature.setter
    def temperature(self, temperature) -> None:
        self.temperature = temperature

    @property
    def groupe_sanguin(self, groupe_sanguin) -> str:
        return self.groupe_sanguin

    @groupe_sanguin.setter
    def groupe_sanguin(self,groupe_sanguin) -> None:
        self.groupe_sanguin = groupe_sanguin

    @property
    def poul(self, contact) -> str:
        return self.poul

    @poul.setter
    def poul(self,poul) -> None:
        self.poul = poul
        