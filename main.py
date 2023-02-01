import tkinter as tk

padding = 30
mass_conversion_factor = 0.45359


def convert_kg_to_lbs():
    kilograms = try_parse_float(input_kg.get())
    pounds = round(kilograms / mass_conversion_factor, 2)
    label_converted_kgs.config(text=f"Is equal to {pounds} lbs")


def convert_lbs_to_kg():
    pounds = try_parse_float(input_lbs.get())
    kilograms = round(pounds * mass_conversion_factor, 2)
    label_converted_lbs.config(text=f"Is equal to {kilograms} kgs")


def try_parse_float(string):
    try:
        return float(string)
    except ValueError:
        return None


window = tk.Tk()
window.minsize(width=300, height=300)
window.config(padx=padding, pady=padding)
window.title("Kg to lbs converter")

# First form labels
label_tile_1 = tk.Label(text="Convert kg to lbs:", font="bold")
label_tile_1.grid(row=0, column=0)

label_kg = tk.Label(text="kg")
label_kg.grid(row=1, column=2)

label_converted_kgs = tk.Label(text="Is equal to 0 lbs")
label_converted_kgs.grid(row=2, column=1)

# Second form labels
label_tile_2 = tk.Label(text="Convert lbs to kg:", font="bold")
label_tile_2.grid(row=3, column=0)

label_lbs = tk.Label(text="lbs")
label_lbs.grid(row=4, column=2)

label_converted_lbs = tk.Label(text="Is equal to 0 kg")
label_converted_lbs.grid(row=6, column=1)

# Inputs
input_kg = tk.Entry()
input_kg.grid(row=1, column=1)

input_lbs = tk.Entry()
input_lbs.grid(row=4, column=1)


# Buttons
button_kg = tk.Button(text="Calculate", command=convert_kg_to_lbs)
button_kg.grid(row=1, column=3)

button_kg = tk.Button(text="Calculate", command=convert_lbs_to_kg)
button_kg.grid(row=4, column=3)


window.mainloop()
