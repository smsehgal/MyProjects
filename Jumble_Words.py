import tkinter
from tkinter import *
import random
from tkinter import messagebox

answers=[
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
    "delhi",
    "germany",
    "bhutan",
    "russia",
    "australia",
    "brazil",
    "beijing",
    "mexico",
    "mumbai",
    "tokyo",
    "cairo",
    "japan",
    "france",
    "singapore",
    "iran",
    "indonesia",
    "italy",
    "sweden",
]

words=[
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
    "dlhei",
    "graeynm",
    "buahtn",
    "irsaus",
    "asuaairlt",
    "bzairl",
    "binegij",
    "xcmoie",
    "mmauib",
    "tokoy",
    "cioar",
    "ajnpa",
    "nfcar",
    "segonpari",
    "anir",
    "iedsanino",
    "iaytl",
    "dseewn",
]

num=random.randrange(0,25,1)

def default():
    global words,answers,num
    lbl.config(text=words[num])


def checkans():
    global words,answers,num
    var=ans1.get()
    if var== answers[num]:
        messagebox.showinfo("Success","This is a correct answer")
        res()
    else:
        messagebox.showerror("Error","This is not correct")
        e1.delete(0,END)

def res():
    global words,answers,num
    num=random.randrange(0,25,1)
    lbl.config(text=words[num])
    e1.delete(0,END)


root=tkinter.Tk()
root.geometry("350x400+400+300")
root.title("Jumbled")
root.configure(background="#000000")
lbl=Label(
    root,
    text="You are here",
    font=("Verdana",18),
    bg= '#000000',
    fg= '#ffffff'
)
lbl.pack(pady=30,ipadx=10,ipady=10)

ans1=StringVar()
e1=Entry(root,font=("Verdana",16),textvariable=ans1)
e1.pack(ipadx=5,ipady=5)

btncheck=Button(root,text="Check",command=checkans,font=("Comic sans ms",16),width="16",bg="#4C4B4B",fg="#6ab04c",relief=GROOVE)
btncheck.pack(pady=40)
btncheck=Button(root,text="Reset",command=res,font=("Comic sans ms",16),width="16",bg="#4C4B4B",fg="#6ab04c",relief=GROOVE)
btncheck.pack()

default()
root.mainloop()