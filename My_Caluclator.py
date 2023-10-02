import tkinter as tk
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)  
        entry.insert(tk.END, str(result))  
    except Exception as e:
        entry.delete(0, tk.END)  
        entry.insert(tk.END, "Error")
def clear():
    entry.delete(0, tk.END)
def backspace():
    current_text = entry.get()
    updated_text = current_text[:-1]
    entry.delete(0, tk.END)
    entry.insert(0, updated_text)
root = tk.Tk()
root.title("Calculator")
title_label = tk.Label(root, text="My Calculator", bg="green", fg="white", font=("Helvetica", 20, "bold"))
title_label.pack(fill="both")
entry = tk.Entry(root, font=("Arial", 16))
entry.pack(fill="both")
button_frame = tk.Frame(root)
button_frame.pack(fill="both")
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 0, 0
for button_text in buttons:
    if button_text == '=':
        tk.Button(button_frame, text=button_text, font=("Arial", 16), width=5, height=2, command=calculate).grid(row=row, column=col)
    else:
        tk.Button(button_frame, text=button_text, font=("Arial", 16), width=5, height=2, command=lambda text=button_text: entry.insert(tk.END, text)).grid(row=row, column=col)
    
    col += 1
    if col > 3:
        col = 0
        row += 1
tk.Button(button_frame, text="reset", font=("Arial", 16), width=5, height=2, command=clear).grid(row=row, column=col)
col += 1
tk.Button(button_frame, text="remove", font=("Arial", 16), width=5, height=2, command=backspace).grid(row=row, column=col)
result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack(fill="both")
root.mainloop()
