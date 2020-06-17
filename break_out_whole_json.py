import ujson
import os
tfidf_file = open("wordURLtfidf_idf.json", "r")
tfidf_content = ujson.load(tfidf_file)
tfidf_file.close()
os.mkdir("/Users/jay/Desktop/CS121/HW3/output5.11/M3/M32.0/words_index6.0")
parent_dir = "/Users/jay/Desktop/CS121/HW3/output5.11/M3/M32.0/words_index6.0"
max_num = len(tfidf_content)
i = 1
for term, termfreqset in tfidf_content.items():
    print(str(i) + "/" + str(max_num))
    if len(term) <= 20:
        child1_dir = os.path.join(parent_dir, str(term[0]))
        try:
            os.mkdir(child1_dir)
        except FileExistsError:
            pass
        file_name = os.path.join(child1_dir, str(term) + ".json")

        word_json = open(file_name, "w")
        ujson.dump(termfreqset, word_json)
        word_json.close()
    i += 1
print("finished")


# os.mkdir("words_index")
