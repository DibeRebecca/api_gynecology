class Symptomes:
    def __init__(self, id, nom) -> None:
        self.id = id
        self.nom = nom

    @property
    def nom(self, nom) -> str:
        return self.nom

    @nom.setter
    def nom(self,nom) -> None:
        self.nom = nom