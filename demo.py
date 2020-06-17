import ujson
import time
import nltk
import os
import math
'''
a = "abcd"
b = ''.join(format(ord(x), 'b') for x in a)
print(b)
'''


class search():
    def __init__(self):
        urls_json_file = open("id_URL.json", "r")
        self.urls_json = ujson.load(urls_json_file)
        urls_json_file.close()
        urls_len_json = open("url_len.json", "r")
        self.urls_len = ujson.load(urls_len_json)
        urls_len_json.close()

        self.stemmer = nltk.stem.PorterStemmer()
        self.parent_dir = "/Users/jay/Desktop/CS121/HW3/output5.11/M3/M32.0/words_index6.0"

    def search_words(self, keywords):
        keywords_list = keywords.split()
        for i in range(len(keywords_list)):
            keywords_list[i] = self.stemmer.stem(keywords_list[i]).lower()

        # print(keywords_list)
        # avoid duplicated key words
        keywords_dict = {}
        for key in keywords_list:
            if key in keywords_dict:
                keywords_dict[key] += 1
            else:
                keywords_dict[key] = 1
        print(keywords_dict)
        #keywords_list = list(set(keywords_list))
        tftq_list = []
        word_dict_list = []  # get word_dict from json

        for word, freq in keywords_dict.items():
            if len(word) > 2:
                path = os.path.join(
                    self.parent_dir, str(word[0]), str(word) + ".json")

                # print(path)
                try:
                    file = open(path, "r")
                    tftq = 1 + math.log10(freq)
                    word_json = ujson.load(file)
                    word_dict_list.append(word_json)
                    tftq_list.append(tftq)

                except FileNotFoundError:
                    print("Sorry, word '" + str(word) +
                          "' is not in our database")
        if word_dict_list == []:
            raise KeyError
            return
        url_tfidf_dict = {}  # format:{"url_index":sum of tfidf score}

        for word_index in range(len(word_dict_list)):

            # print(word)
            for url, tfidf in word_dict_list[word_index].items():

                if str(url) in url_tfidf_dict:
                    url_tfidf_dict[str(url)] += tfidf[0] * \
                        (tftq_list[word_index] * tfidf[1])
                else:
                    url_tfidf_dict[str(url)] = tfidf[0] * \
                        (tftq_list[word_index] * tfidf[1])
        for index, score in url_tfidf_dict.items():
            score = score / (self.urls_len[index])
        count = 0  # get top 20 indexs
        twenty_urls_list = []
        scores = []
        for index, score in sorted(url_tfidf_dict.items(), key=lambda item: item[1], reverse=True):
            if score in scores:
                pass
            else:
                twenty_urls_list.append(index)
                scores.append(score)
                count += 1
            if count == 20:
                break
        print(scores)
        return twenty_urls_list

    def get_urls(self, twenty_urls_list):

        url_list = []
        # url_list = []

        for u in twenty_urls_list:
            url = self.urls_json[u]

            symbol_index = url.find("#")
            if symbol_index != -1:
                url = url[:symbol_index]
            # main_index = url.find("index.php")
            # if main_index != -1:
            #     url = url[:main_index]
            # main2_index = url.find("index.html")
            # if main_index != -1:
            #     url = url[:main2_index]
            # url = url.rstrip("/")
            if url in url_list:
                pass
            else:
                url_list.append(url)

            if len(url_list) == 20:
                break

        return url_list
