import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = var_operation.get()
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Cannot divide by zero!"
            else:
                result = num1 / num2
        entry_result.delete(0, tk.END)
        entry_result.insert(0, result)
    except ValueError:
        entry_result.delete(0, tk.END)
        entry_result.insert(0, "Invalid input")

root = tk.Tk()
root.title("Calculator")

label_num1 = tk.Label(root, text="Number 1:")
label_num1.grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

label_operation = tk.Label(root, text="Operation:")
label_operation.grid(row=1, column=0)
var_operation = tk.StringVar(root)
var_operation.set("+")
option_menu_operation = tk.OptionMenu(root, var_operation, "+", "-", "*", "/")
option_menu_operation.grid(row=1, column=1)

label_num2 = tk.Label(root, text="Number 2:")
label_num2.grid(row=2, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=2, column=1)

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=3, column=0, columnspan=2)

entry_result = tk.Entry(root)
entry_result.grid(row=4, column=0, columnspan=2)

root.mainloop()
