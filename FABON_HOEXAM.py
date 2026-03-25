import tkinter as tk

window = tk.Tk()
window.title("Menu")
window.configure(bg="gray")

def register_window():
    register_window = tk.Toplevel()
    register_window.title("Menu")
    register_window.configure(bg="gray")
    
    register_label = tk.Label(register_window, text="Register Your Credentials Here", bg="gray", font= ("Arial", 12, "bold"))
    register_label.pack(padx=10,pady=5)

    register_frame = tk.Frame(register_window, bg = "darkgray")
    register_frame.pack(padx=10,pady=5)

    register_name = tk.Label(register_frame, text = "Username:", bg = "darkgray", font= ("Arial", 12, "bold"))
    register_pass = tk.Label(register_frame, text = "Password:", bg = "darkgray", font= ("Arial", 12, "bold"))

    register_nameentry = tk.Entry(register_frame)
    register_passentry = tk.Entry(register_frame,show="*")

    def showpassword():
        if showpassvar.get() == 1:
            register_passentry.config(show="")
        elif showpassvar.get() == 0:
            register_passentry.config(show="*")


    showpassvar = tk.IntVar()
    showpass = tk.Checkbutton(register_frame, text = "Show Password",command=showpassword,offvalue=0,onvalue=1)

    submit = tk.Button(register_frame,text = "Submit", bg = "darkgray", font= ("Arial", 12, "bold"))

    register_name.grid(row=1,column=0,padx=5,pady=5)
    register_pass.grid(row=2,column=0,padx=5,pady=5)
    register_nameentry.grid(row=1,column=1,padx=5,pady=5)
    register_passentry.grid(row=2,column=1,padx=5,pady=5)
    showpass.grid(row=3,column=1,padx=5,pady=5)
    submit.grid(row=4,column=1,padx=5,pady=5)

    register_window.mainloop()

welcome = tk.Label(window, text="Welcome",bg="gray", font= ("Aerial", 12, "bold"))
welcome.pack(padx=20,pady=10)

register = tk.Button(window, text="Register", bg="blue",activebackground="darkblue", font=("Arial", 12, "bold"), width=40, command=register_window)
register.pack(padx=20,pady=5)

login = tk.Button(window, text="Log in", bg="green",activebackground="darkgreen", font=("Arial", 12, "bold"), width=40)
login.pack(padx=20,pady=5)

window.mainloop()
