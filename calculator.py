import tkinter as tk 
from tkinter import Tk

calculate = "" 

def add_calculate(symbol):
    global calculate
    calculate += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,  calculate)

def evaluation_calculate():
    global calculate 
    try:
        result = str(eval(calculate))
        calculate = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
        
def clear_field():
    global calculate 
    calculate = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("300x275")

text_result = tk.Text(root, height = 2, width = 16, font = ("Arial", 24))
text_result.grid(columnspan = 5)

button_1 = tk.Button(root, text = "7", command =lambda: add_calculate(7), width = 5, font = ("Arial",14))
button_1.grid(row=2, column=1)
button_2 = tk.Button(root, text = "8", command =lambda: add_calculate(8), width = 5, font = ("Arial",14))
button_2.grid(row=2, column=2)
button_3 = tk.Button(root, text = "9", command =lambda: add_calculate(9), width = 5, font = ("Arial",14))
button_3.grid(row=2, column=3)
button_4 = tk.Button(root, text = "+", command =lambda: add_calculate('+'), width = 5, font = ("Arial",14))
button_4.grid(row=2, column=4)
button_5 = tk.Button(root, text = "4", command =lambda: add_calculate(4), width = 5, font = ("Arial",14))
button_5.grid(row=3, column=1)
button_6 = tk.Button(root, text = "5", command =lambda: add_calculate(5), width = 5, font = ("Arial",14))
button_6.grid(row=3, column=2)
button_7 = tk.Button(root, text = "6", command =lambda: add_calculate(6), width = 5, font = ("Arial",14))
button_7.grid(row=3, column=3)
button_8 = tk.Button(root, text = "-", command =lambda: add_calculate('-'), width = 5, font = ("Arial",14))
button_8.grid(row=3, column=4)
button_9 = tk.Button(root, text = "1", command =lambda: add_calculate(1), width = 5, font = ("Arial",14))
button_9.grid(row=4, column=1)
button_10 = tk.Button(root, text = "2", command =lambda: add_calculate(2), width = 5, font = ("Arial",14))
button_10.grid(row=4, column=2)
button_11 = tk.Button(root, text = "3", command =lambda: add_calculate(3), width = 5, font = ("Arial",14))
button_11.grid(row=4, column=3)
button_12 = tk.Button(root, text = "*", command =lambda: add_calculate('*'), width = 5, font = ("Arial",14))
button_12.grid(row=4, column=4)
button_13 = tk.Button(root, text = "(", command =lambda: add_calculate('('), width = 5, font = ("Arial",14))
button_13.grid(row=5, column=1)
button_14 = tk.Button(root, text = "0", command =lambda: add_calculate(0), width = 5, font = ("Arial",14))
button_14.grid(row=5, column=2)
button_15 = tk.Button(root, text = ")", command =lambda: add_calculate(')'), width = 5, font = ("Arial",14))
button_15.grid(row=5, column=3)
button_16 = tk.Button(root, text = "/", command =lambda: add_calculate('/'), width = 5, font = ("Arial",14))
button_16.grid(row=5, column=4)
button_clear = tk.Button(root, text = "CLR", command = clear_field, width = 11, font = ("Arial", 14))
button_clear.grid(row=6, column=1, columnspan=2)
button_equals = tk.Button(root, text = "=", command = evaluation_calculate, width = 11, font = ("Arial", 14))
button_equals.grid(row=6, column=3, columnspan=2)

root.mainloop()

