![12121](https://github.com/user-attachments/assets/f5bcc48a-92ef-4d1b-8bb4-b714e80c9411)



# Project Name: DigiCalc [Project_Link](https://github.com/manishrajdoot/DigiCalc)   [Download DigiCalc]()


**Step 1: Setting Up the Environment**
We began by importing the necessary libraries, particularly tkinter, which is a built-in Python library used for creating graphical user interfaces (GUIs). We also imported PhotoImage from tkinter to handle the calculator's icon image.

  ![111](https://github.com/user-attachments/assets/b9927fc6-5f90-4884-9401-c593da638048)




**Step 2: Creating Functions for Button Actions**
Several functions were developed to handle the logic behind button clicks and mathematical operations:

1. Number Button Click: When a number button is pressed, this function appends the corresponding number to the display.

   ![1222](https://github.com/user-attachments/assets/51a17983-73b8-476b-b8da-177ba1c232f2)


2. Clear Button: This function clears the calculator's display.
   
   ![2121](https://github.com/user-attachments/assets/9c62e5d8-9bb8-4ed5-a042-1648f0687969)

3. Operations (Add, Subtract, Multiply, Divide): These functions set the current operation (addition, subtraction, multiplication, or division) and store the first number.

    ![3232](https://github.com/user-attachments/assets/6619fba7-1ffe-4591-86f5-0ceb02f54060)

4. Equal Button: This function calculates the result based on the selected operation and the second number.

   `def button_equal():
    second_number = display.get()
    display.delete(0, tk.END)
    if math == "addition":
        display.insert(0, f_num + float(second_number))
`
   **#Similar conditions for subtraction, multiplication, and division**
   

**Step 3: Building the Main Window**
The main window for the calculator was created using the Tk() function. We gave it a title ("DigiCalc"), set a background color, and configured it to be resizable so that the buttons and display could expand.

`window = tk.Tk()
window.title("DigiCalc")
window.configure(bg='lightblue')
`

**Step 4: Setting the Icon Image**
We used PhotoImage to load an icon image for the calculator window. The image path was specified to match the local directory structure.

`icon_image = PhotoImage(file=r"C:\Users\MANISH RAJDOOT\Desktop\DigiCalc\icon\calculator.png")
window.iconphoto(False, icon_image)
`

**Step 5: Creating the Calculator Display**
The display area was implemented using tk.Entry(), which allows users to input numbers. We used font settings to make the text large and easy to read, with numbers aligned to the right.

`display = tk.Entry(window, width=25, borderwidth=5, font=('Arial', 20), justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
`


**Step 6: Creating the Buttons**
We defined each button on the calculator, assigning labels for numbers and operations, and binding them to their respective functions. Buttons were styled to ensure a consistent size and look.


`button_style = {'padx': 40, 'pady': 20, 'font': ('Arial', 16)}

button_1 = tk.Button(window, text="1", bg='lightgreen', command=lambda: button_click(1), **button_style)
button_add = tk.Button(window, text="+", bg='orange', command=button_add, **button_style)
button_equal = tk.Button(window, text="=", bg='blue', command=button_equal, **button_style)
`


**Step 7: Arranging Buttons in a Grid**
The buttons were arranged in a grid layout to form a standard calculator structure, with numeric buttons in rows and operational buttons in the rightmost column. The sticky='nsew' attribute ensured that each button expanded equally across the window.

`button_1.grid(row=3, column=0, sticky='nsew')
button_2.grid(row=3, column=1, sticky='nsew')
button_add.grid(row=1, column=3, sticky='nsew')
`

**Step 8: Running the Main Loop**
Finally, the mainloop() function was called to keep the window running and responsive to user interaction.

`window.mainloop()
`


**Summary**

In summary, this project involved creating a fully functional digital calculator using Python's tkinter library. The steps included designing the UI layout, implementing buttons for numeric input and basic arithmetic operations, and providing logic for calculations. The GUI was made flexible and responsive to enhance the user experience.



