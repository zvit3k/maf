from tkinter import *
import os

def start():
    value = choice.get()
    frames = e1.get()
    interval = e2.get()
    if value==1:
        os.system('gphoto2 -I '+interval+' -F '+frames+' --capture-image')
    elif value==2:
        os.system('gphoto2 -I '+interval+' -F '+frames+' --capture-image-and-download')

        
master = Tk()

choice=IntVar()
choice.set(1)

Label(master, text="Liczba klatek: ", font=('Courier', 15)).grid(row=0)
Label(master, text="Interwal [s]: ", font=('Courier', 15)).grid(row=1)
Radiobutton(master, text="Zapis w aparacie", variable=choice, value=1).grid(row=2, column=0)
Radiobutton(master, text="Zapis na Raspberry", variable=choice, value=2).grid(row=2, column=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Label(master, text="Aby przerwac w trakcie zdjec, nacisnij Ctrl+C").grid(row=4, column=0)
Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Start', command=start).grid(row=3, column=1, sticky=W, pady=4)
master.title("MAF - Mirkowy Automator Fotograficzny")
master.geometry("450x130")
mainloop()
