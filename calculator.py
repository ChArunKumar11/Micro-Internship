import tkinter as tk
from tkinter import messagebox

# Function to update the expression in the entry
def click(event):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(event.widget["text"]))

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed")
        entry.delete(0, tk.END)
    except Exception:
        messagebox.showerror("Error", "Invalid Input")
        entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry widget to display expressions and results
entry = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="solid", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Button text layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

# Create and place buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for char in row:
        btn = tk.Button(frame, text=char, font=("Arial", 18), relief="ridge", borderwidth=1)
        btn.pack(side="left", expand=True, fill="both", padx=1, pady=1)

        if char == "=":
            btn.config(bg="lightgreen", command=evaluate)
        elif char == "C":
            btn.config(bg="lightcoral", command=clear)
        else:
            btn.bind("<Button-1>", click)

# Run the application
root.mainloop()
