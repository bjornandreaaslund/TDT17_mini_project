import os

path = "lidar_data/labels"

d = {}
counts = []

for filename in os.listdir(path):
    id = filename[:len(filename)-7]
    #print(filename)
    if id not in d.keys():
        d[id] = []
    if filename != ".DS_Store":
        with open(path + "/" + filename) as file:
            i = 0
            for line in file:
                line.split(" ")
                d[id].append(line[0])
                i += 1
            if i == 1:
                print(filename)
            if i == 53:
                print(filename)
            counts.append(i)
for key in d.keys():
    d[key] = set(d[key])
    #print(key, d[key])

print(max(counts))
print(min(counts))
