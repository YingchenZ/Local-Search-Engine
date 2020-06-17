from tkinter import *
import time
import ujson
from demo import *
import webbrowser


class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.title('Search Engine')
        self.root.geometry('900x600')
        self.words = StringVar()
        self.ans = []
        self.process()
        # self.ans = []
        # self.ans = []

    def callback(self, url):
        webbrowser.open_new(url)

    def print_result(self):
        #initial_time = time.time_ns()
        for i in range(30, 600, 10):
            places = Label(self.root, text=" " * 400)
            places.place(x=0, y=i)
        initial_time = time.time_ns()
        ################################################################
        try:
            url_index_list = self.A.search_words(self.words.get())
            self.ans = self.A.get_urls(url_index_list)
        except Exception as x:
            print(x)
            self.ans = ["We don't have this(these) key word(s)."]

        # except KeyError:
        #     ans = ["We don't have this(these) key word(s)."]

        #ans = [1, 2, 3, 4, 5]  # 在这里加东西############################
        ################################################################
        print("Searching...")
        for i in range(len(self.ans)):
            print(self.ans[i])
            self.display(i)
            # places = Label(self.root, text="%-5s%s" %
            #                (str(i + 1) + ".", ans[i]), fg="blue", cursor="hand2")
            # #places.bind("<Button-1>", lambda e: self.callback(ans[i]))
            # places.pack()
            # places.bind("<Button-1>", lambda e: self.callback(ans[i]))
            # #places.bind("<Button-1>", lambda e: self.callback(ans[i]))
            # places.place(x=0, y=80 + 25 * i)
        print("Finished!")
        finish_time = time.time_ns()
        time_text = "Run time: " + \
            str((finish_time - initial_time) / (10**6)) + " ms"
        time_duration = Label(self.root, text=time_text)
        time_duration.place(x=0, y=55)
        test = Label(self.root, text="Key Word(s): " + str(self.words.get()))
        test.place(x=0, y=30)

    def display(self, i):
        places = Label(self.root, text="%-5s%s" %
                       (str(i + 1) + ".", self.ans[i]), fg="blue", cursor="hand2")
        places.pack()
        places.bind("<Button-1>", lambda e: self.callback(self.ans[i]))
        places.place(x=0, y=80 + 25 * i)

    def process(self):

        location_name = Entry(self.root, textvariable=self.words)
        location_name.place(x=130, y=0)
        labell = Label(self.root, text='Enter key word(s): ')
        labell.place(x=0, y=0)

        button = Button(self.root, text="Get Url!",
                        command=self.print_result)
        button.place(x=325, y=0)
        # words_json_file = open("wordURLandFreq.json", "r")
        # self.words_json = json.load(words_json_file)
        # print("loaded")
        initial_time = time.time_ns()
        self.A = search()
        finish_time = time.time_ns()
        time_text = "Json Loaded Run time: " + \
            str((finish_time - initial_time) / (10**6)) + " ms"
        print(time_text)
        print("Json Loaded")
        self.finish()

    def finish(self):
        self.root.mainloop()


if __name__ == "__main__":
    Gui()
