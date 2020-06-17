import json
from collections import defaultdict

idURL = defaultdict(str)
with open("/Users/xu_min/Desktop/Spring 2020/CS 121/Assignment3/id.txt",'r') as id:
    for i in id:
        i = i.strip().split()
        idURL[i[0]] = i[1]
    id.close()

print("Start")
IdStore = open("/Users/xu_min/Desktop/Spring 2020/CS 121/Assignment3/id.json",'w')
json.dump(idURL, IdStore)
IdStore.close()
print("Done")