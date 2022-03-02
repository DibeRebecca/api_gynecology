class Traitement:
    def __init__(self, nom, date) -> None:
        self.nom = nom
        self.date = date

    @property
    def nom(self, nom) -> str:
        return self.nom

    @nom.setter
    def nom(self,nom) -> None:
        self.nom = nom

    @property
    def date(self, date) -> str:
        return self.date

    @date.setter
    def date(self,date) -> None:
        self.date = date