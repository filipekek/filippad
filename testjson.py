import json
import statistics

with open("testdata.json") as json_file:
    z = json.load(json_file)


a = {'name': 'average', 'physical': {'age':[],'height':[],'weight'}, 'financial':{'wealth':[],'income':[]}}

#all_ages = []
#all_heights = []
#all_weights = []
#all_wealth = []
#all_incomes = []

for u in z:
    a['physical']['age'].append(u['physical']['age'])
    all_heights.append(u['physical']['height'])
    all_weights.append(u['physical']['weight'])
    all_wealth.append(u['financial']['wealth'])
    all_incomes.append(u['financial']['income'])


#a = {'name' : 'average', 'physical': {'age': statistics.mean(all_ages), 'height': statistics.mean(all_heights), 'weight': statistics.mean(all_weights)}, 'financial': {'wealth': statistics.mean(all_wealth), 'income': statistics.mean(all_incomes)}}

with open("testaverage.json", "w") as outfile:
    json.dump(a, outfile, indent=4)
