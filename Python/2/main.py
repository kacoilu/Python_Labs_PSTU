import json
from my_class import  Person


def load_to_json(filename):
        return json.load(open(filename))


def write_to_json(data, filename):
        json.dump(data, open(filename, 'w'), indent=4)


data = {"Persons": []}

for i in range(10):
    data['Persons'].append(Person().__dict__)

write_to_json(data, 'data.json')
read = load_to_json('data.json')
print('Имя второго человека и возраст третьего')
print(read['Persons'][1]['name'], read['Persons'][2]['age'])