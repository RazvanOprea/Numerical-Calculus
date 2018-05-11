import tkinter


def machine_precision():
    #precizia masina se noteaza u sau epsilon
    epsilon = 1
    m = 0
    while 1.0 + epsilon != 1.0:
        epsilon = pow(10, m)
        m = m - 1
    return epsilon

def Call():
    label = tkinter.Label(master, text="\nPrecizia masina este u = " + str(machine_precision()))
    label.pack()
    button['bg'] = 'black'
    button['fg'] = 'white'
    button.configure(state='disabled')

if __name__ == "__main__":
    master = tkinter.Tk()
    master.geometry("300x300")
    master.title("Ex1")
    button = tkinter.Button(master, text='\nCalculeaza precizia masina\n', command=Call)
    button.pack()
    master.mainloop()
