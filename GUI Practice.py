import tkinter as tk

num_click = 0

def say_hi():
    label.config(text="You Clicked the button ")

def undo():
    label.config(text="My First TKinter Project!")

def click_much():
    global num_click
    num_click+=1
    num_click_label.config(text=str(num_click))
    


#create main window
root = tk.Tk()
root.title("My First TKinter Project!")
root.geometry("400x300")

label = tk.Label(root, text="Hello, TKinter")

label.pack()

button = tk.Button(root, text="click me", command = say_hi)
button.pack()

undo_button = tk.Button(root, text="UNDO!", command = undo)
undo_button.pack()

num_click_label = tk.Label(root, text=str(num_click))
num_click_label.pack()

click_button = tk.Button(root, text="Click", font=("Arial", 28), command = click_much)
click_button.pack()
#runs the above program
root.mainloop()

