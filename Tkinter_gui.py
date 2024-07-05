# Создание окна приветствия
import tkinter as tk

def say_hello():
    user_input = entry.get()
    if user_input:
        print(f"Привет, {user_input}!")
    else:
        print(f"Введите свое имя в поле")

root = tk.Tk()
root.title("Login form")

label = tk.Label(root, text="Введите ваше имя")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Продолжить", command=say_hello)
button.pack()

root.mainloop()
