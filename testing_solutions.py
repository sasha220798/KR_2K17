from math import*
from random import*
def task_24():
    floor_num=int(input("Введите количество этажей в доме: ")) #Количество этажей
    home=int(input("Введите номер квартиры: ")) #Номер квартиры
    porch_num=int(input("Введите количество подъездов: ")) #Количество подъездов
    home_count=int(input("Введите количество квартир на площадке: ")) #Квартир на площадке
    # home_in_porch - квартир в подъезде
    # porch - номер подъезда
    # floor - номер этажа
    home_in_porch = home_count * floor_num
    porch = home / home_in_porch
    porch = ceil(porch)
    floor = (home - (porch-1) * home_in_porch) / home_count
    floor_solution = ceil(floor)
    print("Квартира на ", floor_solution, " этаже, в подъезде ", porch)

#task_24()


def task_44():
    n = int(input("Задайте n: "))
    i = 0
    while i < n:
        i = 1 + (3*n-2)
    print(i)

#task_44()


def task_64():
    N=int(randrange(1,100))
    res = [x for x in range(1,N)]
    print (res)
    K=int(randrange(1,100))
    res_1 = [x for x in range(1, K)]
    print (res_1)
    res_res=list(set(res)-set(res_1))
    print(res_res)

#task_64()


def task_15():
    A=int(input("Введите число А: "))
    B=int(input("Введите число В: "))
    V=(A+B)/2
    print(V)

#task_15()


def task_25():
    k=int(input("Введите к-тую секунду: "))
    M=k//60
    H=k//3600
    D=H//24
    print(M, " minutes ", H, " hours ", D, " days")

task_25()    
