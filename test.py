
with open("testdata.csv", "r") as f: s = f.read()

lines = s.split()

line0 = lines[0]
line1 = lines[1]
line2 = lines[2]

data = []

for y in lines:
	x = y.split(",")
	d = {'name': x[0], 'age': int(x[1]), 'height': int(x[2]), 'weight': int(x[3]), 'wealth': int(x[4])}
	data.append(d)

