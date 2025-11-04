from tkinter import *

root = Tk()
root.geometry("250x300")
root.title("App 1")

btn1 = Button(root, text= "Don't press me", background= "blue", foreground= "dark blue", border= 10, command= root.destroy)
btn1.pack(side='bottom')

btn2 = Button(root, text= "Click me", background= "red", foreground= "pink", bd = 15, command= root.destroy)
btn2.pack(side='left')

btn3 = Button(root, text= "Destroy", background= "orange", foreground= "brown", bd = 10, command= root.destroy)
btn3.pack(side='top')

btn4 = Button(root, text= "Do not click", background= "black", foreground= "grey", bd = 10, command= root.destroy)
btn4.pack(side= 'right')
root.mainloop()