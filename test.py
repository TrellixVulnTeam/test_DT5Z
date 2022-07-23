import os
import time
import threading
from tkinter import *
from tkinter import Button, Tk, HORIZONTAL
from tkinter.ttk import Progressbar
from tkinter import messagebox
import tqdm

# def percentageCalculator(x, y, case=1):
#     """Calculate percentages
#        Case1: What is x% of y?
#        Case2: x is what percent of y?
#        Case3: What is the percentage increase/decrease from x to y?
#     """
#     if case == 1:
#         # Case1: What is x% of y?
#         r = x / 100 * y
#         return r
#     elif case == 2:
#         # Case2: x is what percent of y?
#         r = x / y * 100
#         return r
#     elif case == 3:
#         # Case3: What is the percentage increase/decrease from x to y?
#         r = (y - x) / x * 100
#         return r
#     else:
#         raise Exception("Only case 1,2 and 3 are available!")
#
#
# def makeform(root, fields):
#     entries = []
#     for field in fields:
#         row = Frame(root)
#         lab = Label(row, width=20, text=field, anchor='w')
#         ent = Entry(row)
#         row.pack(side=TOP, fill=X, padx=5, pady=5)
#         lab.pack(side=LEFT)
#         ent.pack(side=RIGHT, expand=YES, fill=X)
#         entries.append((field, ent))
#     return entries
#
#
# def rand_func():
#     for i in range(10):
#         print(i)
#         time.sleep(1)
#
#
# def processEntry(entries):
#     infoDict = {}
#     for entry in entries:
#         field = entry[0]
#         text = entry[1].get()
#         infoDict[field] = text
#
#     return infoDict
#
#
# def runActions(progress, status):
#     alist = range(10)
#
#     log = open("log.txt", "a")
#
#     try:
#
#         p = 0
#         for i in alist:
#             p += 1
#             # Case2: x is what percent of y?
#             unit = percentageCalculator(p, len(alist), case=2)
#
#             # TODO make a decorator!
#             rand_func()  # some func
#
#             step = "Working on {}".format(i)
#             log.write(str('\n[OK]'))
#             progress['value'] = unit
#             percent['text'] = "{}%".format(int(unit))
#             status['text'] = "{}".format(step)
#
#             root.update()
#
#         messagebox.showinfo('Info', "Process completed!")
#         sys.exit()
#
#
#     except Exception as e:
#         messagebox.showinfo('Info', "ERROR: {}".format(e))
#         sys.exit()
#
#     log.close()
#
#
# root = Tk()
# root.title("App v0.1")
# root.geometry("600x320")
#
# # root.iconbitmap(os.path.join(os.getcwd(), 'favicon.ico'))
#
# fields = 'input1', 'input2', 'input4', 'input5', 'input6'
#
# ents = makeform(root, fields)
#
# runButton = Button(root, text='Start downloading', command=(lambda e=ents: runActions(progress, status)))
# percent = Label(root, text="", anchor=S)
# progress = Progressbar(root, length=500, mode='determinate')
# status = Label(root, text="Click button to start process..", relief=SUNKEN, anchor=W, bd=2)
#
# runButton.pack(pady=15)
# percent.pack()
# progress.pack()
# status.pack(side=BOTTOM, fill=X)
#
# root.mainloop()


def add1(board, pos):
    test_list = list(board)
    if board[pos] == '9':
        test_list[pos] = '0'
        board = "".join(test_list)
    else:
        # print(test_list)
        for i in range(0, len(test_list)):
            test_list[i] = int(test_list[i])
        test_list[pos] += 1
        for i in range(0, len(test_list)):
            test_list[i] = str(test_list[i])
        board = "".join(test_list)
    return board


# print(add1('999999', 3))


def sow(board, pos, num):
    position = pos
    number = 0
    while number < num:
        board = add1(board, position)
        position += 1
        number += 1
    return board

print(sow('012340', 1, 3))









