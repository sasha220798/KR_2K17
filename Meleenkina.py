from tkinter import*
from tkinter.filedialog import *
import string
import fileinput

def task(x):
    x=(2.468/(3.69/(10**3)**1/3)**1/5)
    y=25/125/(6.99/(300000)**2)**1/9
    z=(x**2+y**2)/(1-(x**2-y**2)/2)
    textarea_task.delete(1.0, END)
    textarea_task.insert(END, "Здесь находится текст задания №1")
    textarea_solve.delete(1.0, END)
    textarea_solve.insert(END,z, "А здесь - его решение")
    print("Success")

def task_1(task):
    p=5*5;
    print (p)
    textarea_task.delete(1.0, END)
    textarea_task.insert(END, "Здесь находится текст задания №2")
    textarea_solve.delete(1.0, END)
    textarea_solve.insert(END, "А здесь - его решение_2")

def task_2(task):
    a=2**2;
    print (a)
    textarea_task.delete(1.0, END)
    textarea_task.insert(END, "Здесь находится текст задания №3")
    textarea_solve.delete(1.0, END)
    textarea_solve.insert(END, "А здесь - его решение_3")

def task_3(task):
    a=2**2;
    print (a)
    textarea_task.delete(1.0, END)
    textarea_task.insert(END, "Здесь находится текст задания №4")
    textarea_solve.delete(1.0, END)
    textarea_solve.insert(END, "А здесь - его решение_4")

def task_4(task):
    a=2**2;
    print (a)
    textarea_task.delete(1.0, END)
    textarea_task.insert(END, "Здесь находится текст задания №5")
    textarea_solve.delete(1.0, END)
    textarea_solve.insert(END, "А здесь - его решение_5")

def task_5(task):
    a=2**2;
    print (a)
    textarea_task.delete(1.0, END)
    textarea_task.insert(END, "Здесь находится текст задания №6")
    textarea_solve.delete(1.0, END)
    textarea_solve.insert(END, "А здесь - его решение_6")

def task_6(task):
    a=2**2;
    print (a)
    textarea_task.delete(1.0, END)
    textarea_task.insert(END, "Здесь находится текст задания №7")
    textarea_solve.delete(1.0, END)
    textarea_solve.insert(END, "А здесь - его решение_7")

def task_7(task):
    a=2**2;
    print (a)
    textarea_task.delete(1.0, END)
    textarea_task.insert(END, "Здесь находится текст задания №8")
    textarea_solve.delete(1.0, END)
    textarea_solve.insert(END, "А здесь - его решение_8")

def task_8(task):
    a=2**2;
    print (a)
    textarea_task.delete(1.0, END)
    textarea_task.insert(END, "Здесь находится текст задания №9")
    textarea_solve.delete(1.0, END)
    textarea_solve.insert(END, "А здесь - его решение_9")

def task_9(task):
    a=2**2;
    print (a)
    textarea_task.delete(1.0, END)
    textarea_task.insert(END, "Здесь находится текст задания №10")
    textarea_solve.delete(1.0, END)
    textarea_solve.insert(END, "А здесь - его решение_10")

def task_10(task):
    a=2**2;
    print (a)



    
test=Tk()
test.title("Контрольная работа. Малахов Д.А. Вариант № 9")
textarea_task=Text(test, width=50, height=15,font="12",wrap=WORD)
textarea_solve=Text(test, width=50, height=15,font="12",wrap=WORD)
Labe_task=Label(test, text="Задача")
Labe_solve=Label(test, text="Решение")

#Кнопка отладки
but_debug = but_debug = Button(test,
          text="Задание 1", #надпись на кнопке
          width=30,height=2, #ширина и высота
          bg="white",fg="blue") #цвет фона и надписи
but_debug.bind("<Button-1>",task)

#Кнопка задания №2
but_1 = but_1 = Button(test,
          text="Задание 2", #надпись на кнопке
          width=30,height=2, #ширина и высота
          bg="white",fg="blue") #цвет фона и надписи
but_1.bind("<Button-1>",task_1)

#Кнопка задания №3
but_2 = but_2 = Button(test,
          text="Задание 3", #надпись на кнопке
          width=30,height=2, #ширина и высота
          bg="white",fg="blue") #цвет фона и надписи
but_2.bind("<Button-1>",task_2)
#Кнопка задания №4
but_3 = but_3 = Button(test,
          text="Задание 4", #надпись на кнопке
          width=30,height=2, #ширина и высота
          bg="white",fg="blue") #цвет фона и надписи
but_3.bind("<Button-1>",task_3)
#Кнопка задания №5
but_4 = but_4 = Button(test,
          text="Задание 5", #надпись на кнопке
          width=30,height=2, #ширина и высота
          bg="white",fg="blue") #цвет фона и надписи
but_4.bind("<Button-1>",task_4)
#Кнопка задания №6
but_5 = but_5 = Button(test,
          text="Задание 6", #надпись на кнопке
          width=30,height=2, #ширина и высота
          bg="white",fg="blue") #цвет фона и надписи
but_5.bind("<Button-1>",task_5)
#Кнопка задания №7
but_6 = but_6 = Button(test,
          text="Задание 7", #надпись на кнопке
          width=30,height=2, #ширина и высота
          bg="white",fg="blue") #цвет фона и надписи
but_6.bind("<Button-1>",task_6)
#Кнопка задания №8
but_7 = but_7 = Button(test,
          text="Задание 8", #надпись на кнопке
          width=30,height=2, #ширина и высота
          bg="white",fg="blue") #цвет фона и надписи
but_7.bind("<Button-1>",task_7)
#Кнопка задания №9/
but_8 = but_8 = Button(test,
          text="Задание 9", #надпись на кнопке
          width=30,height=2, #ширина и высота
          bg="white",fg="blue") #цвет фона и надписи
but_8.bind("<Button-1>",task_8)
#Кнопка задания №10
but_9 = but_9 = Button(test,
          text="Задание 10", #надпись на кнопке
          width=30,height=2, #ширина и высота
          bg="white",fg="blue") #цвет фона и надписи
but_9.bind("<Button-1>",task_9)

def new_win():
    win=Toplevel(test)
def close_win():
    test.destroy()
def _save():
    sa=asksavefilename()
    letter=txt.get(1.0,END)
    f=open(sa,"w")
    f.write(letter)
    f.close()

men=Menu(test)
test.config(menu=men)
fmen=Menu(men)
men.add_cascade(label="File", menu=fmen)
fmen.add_command(label="New", command=new_win)
fmen.add_command(label="Save", command=_save)
fmen.add_command(label="Exit", command=close_win)


but_debug.grid(column=0, row=2)
but_1.grid(column=0, row=3)
but_2.grid(column=0, row=4)
but_3.grid(column=0, row=5)
but_4.grid(column=0, row=6)
but_5.grid(column=0, row=7)
but_6.grid(column=0, row=8)
but_7.grid(column=0, row=9)
but_8.grid(column=0, row=10)
but_9.grid(column=0, row=11)
Labe_task.grid(column=1, row=2, columnspan=4, rowspan=1, padx=20, pady=10)
Labe_solve.grid(column=6, row=2, columnspan=4, rowspan=1, padx=20, pady=10)
textarea_task.grid(column=1, row=3,columnspan=4,rowspan=8, padx=20, pady=10)
textarea_solve.grid(column=6, row=3,columnspan=4,rowspan=8, padx=20, pady=10)
test.mainloop() 
