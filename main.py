from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.geometry("500x300") 
root.configure(bg="#2c3e50")

def time():
    current_time = strftime('%H:%M:%S %p')
    time_label.config(text=current_time)
    time_label.after(1000, time)

def date():
    current_date = strftime('%A, %d %B %Y')
    date_label.config(text=current_date)

date_label = Label(root, font=("Helvetica", 18, "bold"),
                   background="#2c3e50",
                   foreground="#f1c40f")
date_label.pack(pady=20)

time_label = Label(root, font=('Helvetica', 48, 'bold'), 
              background='#2c3e50', 
              foreground='#ecf0f1')
time_label.pack()

time()
date()

mainloop()