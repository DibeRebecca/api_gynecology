import csv

import json

class Consultation:
    def __init__(self, id, date, lieu) -> None:
        self.id = id
        self.date = date
        self.lieu = lieu

    @property
    def date(self) -> str:
        return self.date

    @date.setter
    def date(self, date) -> None:
        self.date = date

    @property
    def lieu(self, lieu) -> str:
        return self.lieu

    @lieu.setter
    def lieu(self, lieu) -> None:
        self.lieu = lieu

def insert():
    with open("consultation.csv","r") as f:
        reader=csv.reader(f)
        next(reader)
        consultation={"details":[],"patient":[],"constantes":[],"maladies":[]}

        for row in reader:
            print (row)
            consultation={"details":[],"patient":[],"constantes":[],"maladies":[]}

            consultation["details"].append({
                "date":row[0],
                "lieu":row[1],
                })
            
            patient_informations = row[2].split("|")
            consultation["patient"].append({
                "nom":patient_informations[0],
                "prenom":patient_informations[1],
                "age":patient_informations[2],
                "sexe":patient_informations[3],
                "groupe_sanguin":patient_informations[4],
                "telephone":patient_informations[5],
                })
            
            constante_informations = row[3].split("|")
            consultation["constantes"].append({
                "poids":constante_informations[0],
                "pression_arterielle":constante_informations[1],
                "temperature":constante_informations[2],
                "poul":constante_informations[3],
                "glycemie":constante_informations[4],
                })
            
            consultation["maladies"].append({
                "nom":row[4],
                "symptomes":row[5],
                "traitements":row[6],
                "examen":row[7]
                })

    with open("consultation.json","w") as f:
        json.dump(consultation, f,indent=4) 
insert()
