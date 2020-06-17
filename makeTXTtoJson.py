import json
import os
from collections import defaultdict

for filename in os.listdir("/Users/xu_min/Desktop/Spring 2020/CS 121/Assignment3/outputs/"):
    if filename != ".DS_Store":
        word = defaultdict(lambda : defaultdict(int))
        with open("/Users/xu_min/Desktop/Spring 2020/CS 121/Assignment3/outputs/" + filename) as file:
            for i in file:
                i = i.rstrip().split()
                if len(i[0]) > 2:
                    word[i[0]][i[-1]] = int(i[1])
            for term, idFrq in word.items():
                # df = len(idFrq)
                for id, Freq in idFrq.items():
                    word[term.lower()][id] = Freq
            jsonName = filename.strip(".txt")
            if jsonName != "":
                print("{} done".format(jsonName.lower()))
                jsonfile = open("/Users/xu_min/Desktop/Spring 2020/CS 121/Assignment3/Output Json/{}.json".format(jsonName.lower()),'w')
                json.dump(word,jsonfile)
                jsonfile.close()
        file.close()
    
                