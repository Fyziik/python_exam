import json
import requests
import os

# 1. From this api https://api.github.com/orgs/python-elective-fall-2019/repos get all names of the repos and write them to a text file.
response = requests.get('https://api.github.com/orgs/python-elective-fall-2019/repos').json()

with open('exercises/results.txt', 'w') as f:
    to_insert = [ (x['name'], x['owner']['repos_url']) for x in response ]
    formatted_json = json.dump(to_insert, f)
    f.close()