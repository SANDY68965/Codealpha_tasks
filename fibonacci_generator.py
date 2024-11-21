import tkinter as tk
from tkinter import ttk

def fibonacci_count(n):
    """Generate the first n Fibonacci numbers."""
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def fibonacci_up_to(max_value):
    """Generate Fibonacci numbers up to a maximum value."""
    fib_sequence = []
    a, b = 0, 1
    while a <= max_value:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def fibonacci_memoization(n, memo={}):
    """Generate the nth Fibonacci number using memoization."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

def calculate_fibonacci():
    try:
        if option.get() == 1:
            n = int(entry.get())
            result = fibonacci_count(n)
            result_label.config(text=f"The first {n} Fibonacci numbers are: {result}")
        elif option.get() == 2:
            max_value = int(entry.get())
            result = fibonacci_up_to(max_value)
            result_label.config(text=f"Fibonacci numbers up to {max_value} are: {result}")
        elif option.get() == 3:
            n = int(entry.get())
            result = fibonacci_memoization(n)
            result_label.config(text=f"The {n}th Fibonacci number is: {result}")
    except ValueError:
        result_label.config(text="Please enter a valid integer.")

# Setting up the main window
root = tk.Tk()
root.title("Fibonacci Generator")

# Adding options to select type of Fibonacci generation
option = tk.IntVar(value=1)

frame_options = tk.Frame(root)
frame_options.pack(pady=10)

tk.Radiobutton(frame_options, text="Generate first n Fibonacci numbers", variable=option, value=1).pack(anchor='w')
tk.Radiobutton(frame_options, text="Generate Fibonacci numbers up to a maximum value", variable=option, value=2).pack(anchor='w')
tk.Radiobutton(frame_options, text="Get nth Fibonacci number using memoization", variable=option, value=3).pack(anchor='w')

# Adding input field
entry_label = tk.Label(root, text="Enter the number or maximum value:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

# Adding a button to trigger Fibonacci calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate_fibonacci)
calculate_button.pack(pady=10)

# Adding a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Running the application
root.mainloop()

