from tkinter import *
#Создано окно
window =  Tk()
window.title("Это окно")
window.geometry("500x600")

l1= Label()
l1.config(text="Поле 1")
l1.pack()

window,mainloop()