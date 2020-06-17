import os
import json
from collections import defaultdict

word = defaultdict(lambda : defaultdict(int))
for filename in os.listdir("/Users/xu_min/Desktop/Spring 2020/CS 121/Assignment3/outputs/"):
    if filename != ".DS_Store":
        with open("/Users/xu_min/Desktop/Spring 2020/CS 121/Assignment3/outputs/" + filename) as file:
            for i in file:
                i = i.rstrip().split()
                if len(i[0]) > 2:
                    word[i[0]][i[-1]] = int(i[1])

print("Unique Token {}".format(len(word)))
file = open("/Users/xu_min/Desktop/Spring 2020/CS 121/Assignment3/wordURLandFreq.json",'w')
json.dump(word,file)
# for c,v in word.items():
    # file = open("/Users/xu_min/Desktop/Spring 2020/CS 121/Assignment3/wordURLandFreq.json",'w')
    # json.dump(word,file)
    # file.write(f"{c}\n")
    # for i,j in v.items():
    #     file.write("    {} => {} times\n".format(i,j))
    # file.write("===========================================\n") 
file.close()
print("Done")