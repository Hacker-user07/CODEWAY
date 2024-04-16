import tkinter
from tkinter import *

ui=Tk()
ui.title("To-Do-List")
ui.geometry("500x750+500+150")
ui.resizable(False,False)
ui['background']='lightblue'

List=[]

def add():
    task=text_entry.get()
    text_entry.delete(0,END)

    if task:
        with open("todolist.txt",'a') as todofile:
            todofile.write(f"\n{task}")
        List.append(task)
        taskBox.insert(END,task)

def delete():
    global List
    task=str(taskBox.get(ANCHOR))
    if task in List:
        List.remove(task)
        with open("todolist.txt",'w') as todofile:
            for task in List:
                todofile.write(task+"\n")
        taskBox.delete(ANCHOR)

def openTodoFile():
    try:
        global List
        with open("todolist.txt",'r') as todofile:
            tasks=todofile.readlines()
        for task in tasks:
            if task!='\n':
                List.append(task)
                taskBox.insert(END,task)
    except:
        file=open('todolist.txt','w')
        file.close()

iconImage=PhotoImage(file="4782.png_860.png")
ui.iconphoto(False,iconImage)

bar=PhotoImage(file="2273785-200.png")
Label(ui,image=bar,bg="orange").pack()
header=Label(ui,text="Task List",font="forte 30",fg="white",bg="black")
header.place(x=170,y=20)
taskicon=PhotoImage(file="747095.png")
Label(ui,image=taskicon,bg="black").place(x=400,y=20)

frame=Frame(ui,width=500,height=65,bg="black")
frame.place(x=0,y=200)

task=StringVar()
text_entry=Entry(frame,width=38,font="arial",bd=0)
text_entry.place(x=10,y=18)

buttonimg=PhotoImage(file="images.png")

button=Button(frame,image=buttonimg,width=90,bg="black",bd=0,command=add,cursor="hand2")
button.place(x=400,y=0)

box=Frame(ui,width=700,height=100,bg="#32405b")
box.pack(pady=(180,0))

taskBox=Listbox(box,font=('arial',12),width=40,height=20,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
taskBox.pack(side=LEFT,fill=BOTH,padx=20)
scrollbar=Scrollbar(box)
scrollbar.pack(side=RIGHT,fill=BOTH)

taskBox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=taskBox.yview)

openTodoFile()

delframe=Frame(ui,width=500,height=70,bg="lightblue")
delframe.place(x=0,y=670)
Deleteicon=PhotoImage(file="images (1).png")
delbutton=Button(delframe,image=Deleteicon,width=60,bg="black",bd=0,command=delete,cursor="hand2")
delbutton.place(x=215,y=0)
ui.mainloop()
