import json

filename = 'json/test.json'
with open(filename) as f_obj:
    pop_data = json.load(f_obj)

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name    = pop_dict['Country Name']
        population      = pop_dict["Value"]
        print(country_name + ":" + population)