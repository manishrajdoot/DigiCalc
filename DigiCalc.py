import tkinter as tk
from tkinter import PhotoImage

# Function to handle button click for numbers
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))

# Function to clear the display
def button_clear():
    display.delete(0, tk.END)

# Function to set the operation to addition
def button_add():
    first_number = display.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    display.delete(0, tk.END)

# Function to set the operation to subtraction
def button_subtract():
    first_number = display.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    display.delete(0, tk.END)

# Function to set the operation to multiplication
def button_multiply():
    first_number = display.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    display.delete(0, tk.END)

# Function to set the operation to division
def button_divide():
    first_number = display.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    display.delete(0, tk.END)

# Function to calculate the result
def button_equal():
    second_number = display.get()
    display.delete(0, tk.END)

    if math == "addition":
        display.insert(0, f_num + float(second_number))
    elif math == "subtraction":
        display.insert(0, f_num - float(second_number))
    elif math == "multiplication":
        display.insert(0, f_num * float(second_number))
    elif math == "division":
        if float(second_number) != 0:
            display.insert(0, f_num / float(second_number))
        else:
            display.insert(0, "Error")

# Create main window
window = tk.Tk()
window.title("DigiCalc")
window.configure(bg='lightblue')

# Set the icon for the window
icon_image = PhotoImage(file=r"C:\Users\MANISH RAJDOOT\Desktop\DigiCalc\icon\calculator.png")  # Make sure to use your icon's filename
window.iconphoto(False, icon_image)

# Configure the window to be resizable and flexible
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)

# Create display area
display = tk.Entry(window, width=25, borderwidth=5, font=('Arial', 20), justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

# Create buttons with unique colors and equal size
button_style = {'padx': 40, 'pady': 20, 'font': ('Arial', 16)}

button_1 = tk.Button(window, text="1", bg='lightgreen', command=lambda: button_click(1), **button_style)
button_2 = tk.Button(window, text="2", bg='lightgreen', command=lambda: button_click(2), **button_style)
button_3 = tk.Button(window, text="3", bg='lightgreen', command=lambda: button_click(3), **button_style)
button_4 = tk.Button(window, text="4", bg='lightgreen', command=lambda: button_click(4), **button_style)
button_5 = tk.Button(window, text="5", bg='lightgreen', command=lambda: button_click(5), **button_style)
button_6 = tk.Button(window, text="6", bg='lightgreen', command=lambda: button_click(6), **button_style)
button_7 = tk.Button(window, text="7", bg='lightgreen', command=lambda: button_click(7), **button_style)
button_8 = tk.Button(window, text="8", bg='lightgreen', command=lambda: button_click(8), **button_style)
button_9 = tk.Button(window, text="9", bg='lightgreen', command=lambda: button_click(9), **button_style)
button_0 = tk.Button(window, text="0", bg='lightgreen', command=lambda: button_click(0), **button_style)

button_add = tk.Button(window, text="+", bg='orange', command=button_add, **button_style)
button_subtract = tk.Button(window, text="-", bg='orange', command=button_subtract, **button_style)
button_multiply = tk.Button(window, text="*", bg='orange', command=button_multiply, **button_style)
button_divide = tk.Button(window, text="/", bg='orange', command=button_divide, **button_style)

button_clear = tk.Button(window, text="AC", bg='red', command=button_clear, **button_style)
button_equal = tk.Button(window, text="=", bg='blue', command=button_equal, **button_style)

# Arrange buttons in grid with sticky to ensure they expand equally
button_1.grid(row=3, column=0, sticky='nsew')
button_2.grid(row=3, column=1, sticky='nsew')
button_3.grid(row=3, column=2, sticky='nsew')

button_4.grid(row=2, column=0, sticky='nsew')
button_5.grid(row=2, column=1, sticky='nsew')
button_6.grid(row=2, column=2, sticky='nsew')

button_7.grid(row=1, column=0, sticky='nsew')
button_8.grid(row=1, column=1, sticky='nsew')
button_9.grid(row=1, column=2, sticky='nsew')

button_0.grid(row=4, column=0, sticky='nsew')

button_clear.grid(row=4, column=1, sticky='nsew')
button_equal.grid(row=4, column=2, sticky='nsew')

button_add.grid(row=1, column=3, sticky='nsew')
button_subtract.grid(row=2, column=3, sticky='nsew')
button_multiply.grid(row=3, column=3, sticky='nsew')
button_divide.grid(row=4, column=3, sticky='nsew')

# Start the main loop
window.mainloop()
