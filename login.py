from email import message
from tkinter import *
from tkinter import ttk, messagebox

class Login_window():
    def __init__(self,master):
        frame = ttk.Frame(master, padding = 10)
        frame.grid()
        #labels for username and password
        ttk.Label(frame, text="Username").grid(column=0, row=0)
        ttk.Label(frame, text="Password").grid(column=0, row=1)

        #buttons
        Q_button = ttk.Button(frame, text="quit",command=master.destroy).grid(column=1, row=2)
        S_button = ttk.Button(frame, text="Sign Up", command = sign_up).grid(column=2, row=2)
        L_button = ttk.Button(frame, text="Log In",command=sign_up).grid(column=0, row=2)

        #entry fields
        Username_text = Entry(frame).grid(column=1, row=0)
        password_text = Entry(frame).grid(column=1, row=1)

    #function for collecting user and pass word


# function for signing up
# def sign_up():
def sign_up():
    messagebox.showerror("OOPS!", "You thought!")







# Window for login information
root = Tk()
root.title("Log-In")
window = Login_window(root)
root.mainloop()






