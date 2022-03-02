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


def insert(csvFilePath, jsonFilePath):
    jsonArr = []

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.reader(csvf)
        next(csvReader)
        for row in csvReader:
            print (row)
            consultation={"ID":"","details":[],"patient":[],"constantes":[],"maladies":[]}
            consultation["ID"]=row[0]
            consultation["details"].append({
                "date":row[1],
                "lieu":row[2],
                })
            patient_informations = row[3].split("|")
            print(row[2])

            consultation["patient"].append({
                "nom":patient_informations[0],
                #"prenom":patient_informations[1],
                "age":patient_informations[2],
                "sexe":patient_informations[3],
                "groupe_sanguin":patient_informations[4],
                "telephone":patient_informations[5],
                })
            constante_informations = row[4].split("|")
            consultation["constantes"].append({
                "poids":constante_informations[0],
                "pression_arterielle":constante_informations[1],
                "temperature":constante_informations[2],
                "poul":constante_informations[3],
                "glycemie":constante_informations[4],
                })
            
            consultation["maladies"].append({
                "nom":row[5],
                "symptomes":row[6],
                "traitements":row[7],
                "examen":row[8]
                })
            jsonArr.append(consultation)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArr, indent=4)
        jsonf.write(jsonString)


csvFilePath = r'consul.csv'
jsonFilePath = r'consul.json'


insert(csvFilePath, jsonFilePath) 
