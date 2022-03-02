import json
import csv

with open ("names.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data={"names":[]}
    for row in reader:
        print (row)
        data["names"].append({"firstname":row[0 ],"age":row[1]})
        
with open ("names.json","w") as f:
    json.dump(data, f, indent=4)
    
    