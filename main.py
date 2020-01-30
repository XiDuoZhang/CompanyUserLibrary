import tkinter as tk
from tkinter import *
from tkinter import ttk
import connectionToSql as connection
from ShowAllUsers import getAllUsers

conn = connection.connection()
allUsers = getAllUsers(conn)
def showAllUsers():
    print(getAllUsers(conn))

window = Tk()
frame = Frame(window)
frame.pack(side=tk.LEFT, padx=20)
tv = ttk.Treeview(frame, columns=(1,2,3,4), show='headings', height='5')
tv.pack()

tv.heading(1, text="Id")
tv.heading(2, text="Last Name")
tv.heading(3, text="First Name")
tv.heading(4, text="User Code")
for user in allUsers:
    print(user)
    tv.insert('','end', values = user)

window.title('Company User System')
window.configure(background='gray')
# window.geometry("650x500")
window.minsize(500, 500)
window.resizable(False, False)

but = Button(window, text="Get all Company ", width=6, command=showAllUsers)
but.pack()
window.mainloop()