import json
import statistics as st
import plotly.express as px

with open("testdata.json") as json_file:
    z = json.load(json_file)

physical_categories = list( z[0]['physical'] )
financial_categories = list( z[0]['financial'] ) 

m = {'name': 'average', 'physical': {}, 'financial':{}}
a = {'name': 'all', 'physical': {}, 'financial':{}}

for l in physical_categories:
    a['physical'][l] = []

for h in financial_categories:
    a['financial'][h] = []

#all_ages = []
#all_heights = []
#all_weights = []
#all_wealth = []
#all_incomes = []

#for u in z:
#    for l in physical_categories:
#        a['physical'][l].append(u['physical'][l])
#    for l in financial_categories:
#        a['financial'][l].append(u['financial'][l])

for l in physical_categories:
    m['physical'][l] = st.mean([ p['physical'][l] for p in z])
for l in financial_categories:
    m['financial'][l] = st.mean([ p['financial'][l] for p in z])

for l in physical_categories:
    a['physical'][l] = [ p['physical'][l] for p in z]
for l in financial_categories:
    a['financial'][l] = [ p['financial'][l] for p in z]


x = [ p['name'] for p in z ]

px.bar(x=x, y=a['physical']['weight'], labels={'x': 'names', 'y': 'weight'}).show()
#for u in physical_categories:
#    a['physical'][u] = st.mean(a['physical'][u])

#for u in financial_categories:
#    a['financial'][u] = st.mean(a['financial'][u])

#a = {'name' : 'average', 'physical': {'age': st.mean(all_ages), 'height': st.mean(all_heights), 'weight': st.mean(all_weights)}, 'financial': {'wealth': st.mean(all_wealth), 'income': st.mean(all_incomes)}}

#with open("testaverage.json", "w") as outfile:
 #   json.dump(a, outfile, indent=4)
