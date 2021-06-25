import csv
import json

with open('exercises/employee_file.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter=";")
    with open('exercises/frida.json', 'w') as j:
        j.write(json.dumps(list(reader)))