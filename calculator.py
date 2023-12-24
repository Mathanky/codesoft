import tkinter as tk

def calculate(a, b, operation):
    try:
        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == '/':
            result = a / b
        elif operation == '^':
            result = a ** b
        else:
            result = 'Invalid Operator'
    except ZeroDivisionError:
        result = 'Error: Division by zero'
    return result

def calculate_button_click():
    number1 = float(entry_number1.get())
    number2 = float(entry_number2.get())
    operation = entry_operator.get()

    result = calculate(number1, number2, operation)

    label_result.config(text=f"Result: {result}")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create input fields and labels
label_number1 = tk.Label(window, text="Enter Number 1:")
entry_number1 = tk.Entry(window)

label_number2 = tk.Label(window, text="Enter Number 2:")
entry_number2 = tk.Entry(window)

label_operator = tk.Label(window, text="Enter Operator (+, -, *, /, ^):")
entry_operator = tk.Entry(window)

# Create a button to trigger the calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate_button_click)

# Create a label to display the result
label_result = tk.Label(window, text="Result:")

# Place widgets in the window using grid layout
label_number1.grid(row=0, column=0)
entry_number1.grid(row=0, column=1)

label_number2.grid(row=1, column=0)
entry_number2.grid(row=1, column=1)

label_operator.grid(row=2, column=0)
entry_operator.grid(row=2, column=1)

calculate_button.grid(row=3, column=0, columnspan=2)

label_result.grid(row=4, column=0, columnspan=2)

# Start the GUI main loop
window.mainloop()