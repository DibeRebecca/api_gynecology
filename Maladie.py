import json
import csv
class Maladie:
    def __init__(self, id, nom) -> None:
        self.id = id
        self.nom = nom
    
    @property
    def nom(self, nom) -> str:
        return self.nom

    @nom.setter
    def nom(self,nom) -> None:
        self.nom = nom

def insert():
    with open("maladie.csv","r") as f:
        reader=csv.reader(f)
        next(reader)
        maladies={"maladies":[]}
        for row in reader:
            print (row)
            maladies["maladies"].append({
                "nom":row[0],
                "symptomes":row[1],
                "traitements":row[2],
                "examen":row[3]
                })

    with open("maladies.json","w") as f:
        json.dump(maladies, f,indent=4) 
            
insert()