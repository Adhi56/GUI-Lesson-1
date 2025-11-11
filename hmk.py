from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Replit Screen")
root.config(background = "dark blue")

templatelabel = Label(root, text= "Pick a Template")
templatelabel.place(x = 125, y = 25)
templateentry = Entry(root, width = 30)
templateentry.place(x = 125, y = 60)

namelabel = Label(root, text = "Name your project")
namelabel.place(x = 125, y = 100)
nameentry = Entry(root, width = 30)
nameentry.place(x= 125, y = 135)

createreplbutton = Button(root,text="Create Repl", bg = "white", fg = "grey", bd = 15, command = root.destroy)
createreplbutton.place(x= 125, y= 300)

root.mainloop()