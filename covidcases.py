import plotly.express as px

with open("usacovid1.csv", "r") as f:
    lines = f.readlines()
names = lines[0].split(',')
names_ready = []
dates = list()

for u in names:
    names_ready.append(u.replace('"','').replace('\n',''))

lines_dict = dict()
for x in names_ready:
    lines_dict[x] = list()


for i in lines:
    if i == lines[0]:
        continue
    i_list = i.replace("'", "").replace("\n", "").split(",")
    i_ready = list()
    for n in i_list:
        if n == i_list[0]:
            i_ready.append(None)
            dates.append(n.replace('"', ''))
            continue
        elif n == '':
            i_ready.append(0)
            continue
        else:
            i_ready.append(int(n))
    for u in i_ready:
        lines_dict[names_ready[i_ready.index(u)]].append(u)

for k in lines_dict:
    lines_dict[k].reverse()

px.line(x=dates, y=lines_dict['negative'])

