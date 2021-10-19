
d = []
n = 100

for i in range(n):
    x = {"name": "fff"+str(i), "age": i*2, "height": i+100, "weight": 10*i, "wealth": 1000*i}
    temp = [ x["name"], str(x["age"]), str(x["height"]), str(x["weight"]), str(x["wealth"]) ]
    temp = ",".join(temp)
    d.append(temp)

s = "\n".join(d)

with open("testdata.csv", "w+") as f: f.write(s)


