from bs4 import BeautifulSoup
import json
import nltk
from collections import defaultdict
import re
import os
from itertools import groupby


def tokenize(content_list):
    token_list = []
    for i in content_list:
        i = re.sub("[^a-zA-Z0-9]+", ' ', i)
        i = i.strip().split()
        for token in i:
            if len(token) > 1:
                token_list.append(token)
    return token_list


def get_allFilePath():
    folder_path = "/Users/jay/Desktop/CS121/HW3/DEV"
    domain_list = os.listdir(folder_path)
    json_list = []

    for domain in domain_list:
        if "uci_edu" in domain:
            page_list = os.listdir(os.path.join(folder_path, domain))
            for json in page_list:
                json_list.append(os.path.join(folder_path, domain, json))

    return json_list


def record_id(path, web_id):
    id_file = open("id.txt", "a")
    id_file.write(str(web_id) + " " + path + "\n")
    id_file.close()


def get_tokenList(path):
    with open(path) as f:
        tempdata = json.load(f)
        soup = BeautifulSoup(tempdata["content"], "html.parser")
        content = soup.get_text()
        content_list = content.strip().split()
        token_list = tokenize(content_list)

    return token_list


def porterStem(words):
    stemmer = nltk.stem.PorterStemmer()
    return stemmer.stem(words)


def get_wordDict(token_list):
    wordcount_dict = defaultdict(int)
    # port_stemmer = nltk.PorterStemmer()

    for token in token_list:
        ss = [''.join(list(g))
              for k, g in groupby(token, key=lambda x: x.isdigit())]
        for i in ss:
            if re.match("^[a-zA-Z]+$", i):
                i = porterStem(i)
            wordcount_dict[i] += 1
# worddict[a][url]+=1
            # wordcount_dict[port_stemmer.stem(token)] += 1

    return wordcount_dict


def main():
    web_id = 0
    json_list = get_allFilePath()

    for json in json_list:
        path = json
        web_id += 1
        print(web_id)

        record_id(path, web_id)
        token_list = get_tokenList(path)
        wordcount_dict = get_wordDict(token_list)

        for word, count in wordcount_dict.items():
            file = open("/Users/jay/Desktop/CS121/HW3/output/" +
                        word[0] + ".txt", "a")
            file.write(word + "\t" + str(count) + "\t" + str(web_id) + "\n")
            file.close()


if __name__ == "__main__":
    main()
