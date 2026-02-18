import tkinter as tk

window = tk.Tk()
window.title("Test Window")
window.geometry("500x500")
window.resizable(True, True)
window.configure(bg="Gray")

img = tk.PhotoImage(file="logo.png")
image_label = tk.Label(window, image=img)
image_label.pack()

name_lbl=tk.Label(window,text="Name")
name_lbl.pack(pady=5,padx=10)

name_entry=tk.Entry(window)
name_entry.pack(pady=5,padx=10)

def show():
    name=name_entry.get()
    label ['text'] = f"Hello {name}"

button = tk.Button(window, text="Submit", font = ("Arial",12,"bold"), fg = "Black",bg= "Gray", width = 10, height = 1,anchor = 'center')
button.pack(side = "top", padx = 10,pady = 20,fill = "x",expand=False)
window.mainloop()
