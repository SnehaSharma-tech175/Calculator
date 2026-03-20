import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("450x550")
root.resizable(False, False)

# Configure grid (IMPORTANT for proper layout)
for i in range(6):
    root.rowconfigure(i, weight=1)

for j in range(4):
    root.columnconfigure(j, weight=1)

# Display (Entry Widget)
expression = ""
input_text = tk.StringVar()

entry = tk.Entry(root, textvariable=input_text,
                 font=('Arial', 18), bd=8,
                 insertwidth=2, borderwidth=4,
                 justify='right')
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Functions
def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

def equalpress():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    input_text.set("")

def delete():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == '=':
        action = equalpress
    else:
        action = lambda x=text: press(x)

    tk.Button(root, text=text, font=('Arial', 14),
              command=action).grid(row=row, column=col,
                                   sticky="nsew", padx=5, pady=5)

# Clear and Delete buttons
tk.Button(root, text='C', font=('Arial', 14), command=clear)\
    .grid(row=5, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

tk.Button(root, text='DEL', font=('Arial', 14), command=delete)\
    .grid(row=5, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)

# Run the app
root.mainloop()