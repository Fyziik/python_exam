import json

people = [
    {
        'name': 'Andreas',
        'age': 25
    },
    {
        'name': 'Findus',
        'age': 2
    }
]

# Write JSON object to file with dump
# dump just directly formats and inserts into the assigned file, skipping the return part. This is actually twice as fast as .dumps()
with open('testfiles/people.json', 'w') as f:
    json.dump(people, f)
    f.close()



# Write JSON object to file with dumps
# dumps returns a formatted string, which we can use .write() with to insert it into a .json file in the right format
with open('testfiles/people2.json', 'w') as f:
    formatted_json = json.dumps(people)
    f.write(formatted_json)
    f.close()



# Reading from JSON file via .load()
with open('testfiles/people.json', 'r') as f:
    output = json.load(f)
    print(output)
    print( [ i['name'] for i in output ] )



# Reading from JSON file via .loads()
with open('testfiles/people2.json', 'r') as f:
    txt = f.read()
    output = json.loads(txt)
    print(output)
    print( [ i['age'] for i in output ] )