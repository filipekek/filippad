import json

#d = []
z = []
n = 10

for i in range(n):
    x = {'name': 'fff' + str(i), 'physical':{}, 'financial':{}}
    x['physical'] = {'age' : i+42, 'height': i*3, 'weight': i+29}
    x['financial'] = {'wealth': i*1300, 'income': i*500}
    z.append(x)

#    temp = [ x["name"], str(x["age"]), str(x["height"]), str(x["weight"]), str(x["wealth"]) ]
#    temp = ",".join(temp)
#    d.append(temp)

#s = "\n".join(d)

#with open("testdata.csv", "w+") as f: f.write(s)
with open("testdata.json", "w") as outfile:
    json.dump(z, outfile, indent=4)
