import json
from collections import defaultdict

file = open("/Users/xu_min/Desktop/Spring 2020/CS 121/Assignment3/id.json",'r')
idFile = json.load(file)
print("Loading Complete")

idWURL = defaultdict(str)
for id, fname in idFile.items():
    currentFile = open("/Users/xu_min/Desktop/Spring 2020/CS 121/Assignment3/{}".format(fname), 'r')
    currentData = json.load(currentFile)
    idWURL[id] = currentData['url']

print("New dict completed")
newfile = open("/Users/xu_min/Desktop/Spring 2020/CS 121/Assignment3/idURL.json",'w')
json.dump(idWURL,newfile)
print("Done")