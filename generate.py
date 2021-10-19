
d = []
n = 100

for i in range(n):
#    x = {"name": "fff"+str(i), "age": i*2, "height": i+100, "weight": 10*i, "wealth": 1000*i}
    x = "fff" + str(i) + "," + str(i*2) + "," + str(i+100) + "," + str(10*i) +  "," + str(1000*i)
    d.append(x)

s = ("\n").join(d)
print(s)

with open("testdata.csv", "w+") as f: f.write(s)


