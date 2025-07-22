import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        value = float(entry_temp.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        if from_unit == to_unit:
            result = value
        elif from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (value * 9/5) + 32
            elif to_unit == "Kelvin":
                result = value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (value - 32) * 5/9
            elif to_unit == "Kelvin":
                result = (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = value - 273.15
            elif to_unit == "Fahrenheit":
                result = (value - 273.15) * 9/5 + 32

        label_result.config(text=f"Result: {result:.2f} {to_unit}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x250")
root.resizable(False, False)

tk.Label(root, text="Enter Temperature:").pack(pady=5)
entry_temp = tk.Entry(root)
entry_temp.pack()

tk.Label(root, text="From:").pack(pady=5)
combo_from = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
combo_from.pack()
combo_from.current(0)

tk.Label(root, text="To:").pack(pady=5)
combo_to = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
combo_to.pack()
combo_to.current(1)

tk.Button(root, text="Convert", command=convert_temperature).pack(pady=15)
label_result = tk.Label(root, text="Result: ", font=('Arial', 12))
label_result.pack()

root.mainloop()