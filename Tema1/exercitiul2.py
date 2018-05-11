from random import random, randint
from exercitiul1 import machine_precision
from tkinter import *


# Verificam daca (x + y) + z = x + (y + z) , unde y = u si z = u
def checkAdditionIsAssociative():
    x = 1.0
    y = machine_precision()
    z = machine_precision()
    return (x + y) + z == x + (y + z)


def checkMultiplicationIsAssociative():
    my_dict = dict()
    my_dict['check'] = True
    x = random()
    y = random()
    z = random()
    while (x * y) * z == x * (y * z):
        x = random()
        y = random()
        z = random()
    my_dict['check'] = False
    my_dict['x'] = x
    my_dict['y'] = y
    my_dict['z'] = z
    return my_dict
    

if __name__ == "__main__":
    check_addition = checkAdditionIsAssociative()
    check_m = checkMultiplicationIsAssociative()
    master = Tk()
    master.title('Ex2')
    master.geometry("300x300")
    Label(master, text='Adunarea este asociativa: ' + str(check_addition)).pack()
    Label(master, text='\nInmultirea este asociativa: '
                       + str(check_m['check']) + '\n'
                       + 'x = ' + str(check_m['x']) + '\n'
                       + 'y = ' + str(check_m['y']) + '\n'
                       + 'z = ' + str(check_m['z'])).pack()
    master.mainloop()
