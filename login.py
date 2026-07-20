from tkinter import *
from tkinter import ttk

# function for saving login info

# function for signing up

# Window for login information
window = Tk()
frame = ttk.Frame(window, padding = 5)
frame.grid()

#labels for username and password
ttk.Label(frame, text="Username").grid(column=0, row=0)
ttk.Label(frame, text="Password").grid(column=0, row=1)

#text fields for username and passwords
ttk.Entry(frame).grid(column=1, row=0)
ttk.Entry(frame).grid(column=1, row=1)

#exit button
ttk.Button(frame, text="quit",command=window.destroy).grid(column=1, row=2)
ttk.Button(frame, text="Sign Up").grid(column=2, row=2)
ttk.Button(frame, text="Log In",command=window.destroy).grid(column=0, row=2)

window.mainloop()
