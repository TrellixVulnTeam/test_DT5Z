import os
from tkinter import *
from tkinter import filedialog


# class MyWindow:
#     def __init__(self, win):
#         self.lbl1=Label(win, text='First number')
#         self.lbl2=Label(win, text='Second number')
#         self.lbl3=Label(win, text='Result')
#         self.t1=Entry(bd=3)
#         self.t2=Entry()
#         self.t3=Entry()
#         self.btn1 = Button(win, text='Add')
#         self.btn2=Button(win, text='Subtract')
#         self.lbl1.grid(column=0, row=0, pady=2)
#         self.t1.grid(column=1, row=0, pady=2)
#         self.lbl2.grid(column=0, row=1, pady=2)
#         self.t2.grid(column=1, row=1, pady=2)
#         # self.b1=Button(win, text='Add', command=self.add)
#         # self.b2=Button(win, text='Subtract')
#         # self.b2.bind('<Button-1>', self.sub)
#         # self.b1.place(x=100, y=150)
#         # self.b2.place(x=200, y=150)
#         # self.lbl3.place(x=100, y=200)
#         # self.t3.place(x=200, y=200)
#     def add(self):
#         self.t3.delete(0, 'end')
#         num1=int(self.t1.get())
#         num2=int(self.t2.get())
#         result=num1+num2
#         self.t3.insert(END, str(result))
#     def sub(self, event):
#         self.t3.delete(0, 'end')
#         num1=int(self.t1.get())
#         num2=int(self.t2.get())
#         result=num1-num2
#         self.t3.insert(END, str(result))
#
# window=Tk()
# mywin=MyWindow(window)
# window.title('Hello Python')
# window.geometry("400x300+10+10")
# window.mainloop()


def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename)


# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("500x500")

# Set window background color
window.config(background="white")

# Create a File Explorer label
label_file_explorer = Label(window,
                            text="File Explorer using Tkinter",
                            width=100, height=4,
                            fg="blue")

button_explore = Button(window,
                        text="Browse Files",
                        command=browseFiles)

button_exit = Button(window,
                     text="Exit",
                     command=exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column=1, row=1)

button_explore.grid(column=1, row=2)

button_exit.grid(column=1, row=3)

# Let the window wait for any events
window.mainloop()