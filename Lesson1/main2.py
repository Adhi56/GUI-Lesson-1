from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Password")
root.config(background= "light blue")

usernamelabel = Label(root, text= "Username: ")
usernamelabel.place(x= 50,y =50)
usernameentry = Entry(root, width= 30)
usernameentry.place(x= 150, y = 48)

passwordlabel = Label(root, text= "Password: ")
passwordlabel.place(x=50, y =100)
passswordentry = Entry(root, show='*', width= 30)
passswordentry.place(x= 150, y= 98)

submit = Button(root, text= "Submit", bg= "blue", fg= "grey", bd = 15, command= root.destroy)
submit.place(x=50, y= 300)
root.mainloop()