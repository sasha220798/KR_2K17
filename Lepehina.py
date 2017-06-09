from tkinter import*
from math import*
from tkinter.filedialog import *
import string
import fileinput

def task(x):
    z=1/(sqrt(1+sin(1/(sqrt(2+cos(1/3+sin(1/4)))))))
    textarea_task.delete(1.0, END)
    textarea_task.insert(END, "Написать программу для вычисления значения выражения: z=1/(sqrt(1+sin(1/(sqrt(2+cos(1/3+sin(1/4)))))))")
    textarea_solve.delete(1.0, END)
    textarea_solve.insert(END, z)

def task_1(task):
    N=int(input("Введите количество этажей в доме"))    # Этажей в доме
    K=int(input("Введите количество квартир на площадке"))    # Квартир на площадке
    M=int(input("Введите количество подъездов в доме"))    # Подъезов в доме
    F=int(input("Введите номер квартиры"))    # Номер хаты
    P=F/(N*K)+ 1 #Номер подъезда
    G=F/((N*K)/K)+1 #Номер этажа
    textarea_task.delete(1.0, END)
    textarea_task.insert(END, "В N-этажном доме M подъездов. На каждой лестничной площадке К квартир. Нумерация квартир в доме сквозная, на¬чиная с 1. Написать программу, которая по номеру квартиры определяет номер подъезда и этажа, на котором находится квартира.")
    textarea_solve.delete(1.0, END)
    textarea_solve.insert(END, P, G )

def task_2(task):
    textarea_task.delete(1.0,END)
    textarea_task.insert(END,"Заданы окружность радиуса R с центром в начале координат и прямая, проходящая через точки А (х; у) и В (х; - у). Написать программу, проверяющую, пересекаются ли окружность и прямая, или они касаются друг друга, или не пересекаются и не касаются.")
    r=int(input("Введите радиус круга "))
    x=int(input("Введите положительное значение x "))
    y=int(input("Введите положительное значение y "))
    if x<r:
        textarea_solve.delete(1.0,END)
        textarea_solve.insert(END,"окружность с центром в начале координат и радиусом", (r), " и прямая, проходящая через точки ", (x,y),(x,-y), ", пересекаются")
                                                                                                                                           
    elif x==r:
        textarea_solve.delete(1.0,END)
        textarea_solve.insert(END,"окружность с центром в начале координат и радиусом", (r), " и прямая, проходящая через точки ", (x,y),(x,-y), ", касаются")
    else:
        textarea_solve.delete(1.0,END)
        textarea_solve.insert(END,"окружность с центром в начале координат и радиусом", (r), " и прямая, проходящая через точки ", (x,y),(x,-y), ", не пересекаются и не касаются")

def task_3(task):
    r=int(input("Введите радиус круга "))
    x=int(input("Введите положительное значение x "))
    y=int(input("Введите положительное значение y "))
    if x<r:
        textarea_task.delete(1.0,END)
        textarea_solve.delete(1.0,END)
        textarea_task.insert(END,"окружность")
        textarea_solve.insert(END,"окружность с центром в начале координат и радиусом", r, "и прямая, проходящая через точки ", (x,y),(x,-y),",пересекаются")                   
    elif x==r:
        textarea_task.delete(1.0,END)
        textarea_solve.delete(1.0,END)
        textarea_task.insert(END,"окружность")
        textarea_solve.insert(END,"окружность с центром в начале координат и радиусом", r, "и прямая, проходящая через точки ", (x,y),(x,-y),",касаются")
    else:
        textarea_task.delete(1.0,END)
        textarea_solve.delete(1.0,END)
        textarea_task.insert(END,"окружность")
        textarea_solve.insert(END,"окружность с центром в начале координат и радиусом", r, "и прямая, проходящая через точки ", (x,y),(x,-y),",не пересекаются и не касаются")

def task_4(task):
    a=2**2;
    print (a)
    textarea_task.delete(1.0, END)
    textarea_task.insert(END, "Здесь находится текст задания №5")
    textarea_solve.delete(1.0, END)
    textarea_solve.insert(END, "А здесь - его решение_5")

def task_5(task):
    A=int(input("Введите число А: "))
    B=int(input("Введите число В: "))
    
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
