import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style 
import password_generator
import argparse

# Root component
root = tk.Tk()
root.title("Fortify")
root.geometry("900x500")

# Set the style
style = Style(theme="vapor")

# Setting the frame
frame = ttk.LabelFrame(root, text="Password Generator", padding=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title label and entry
title_label = ttk.Label(frame, text="Enter title of the password:")
title_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
title_input= tk.StringVar()
title_input = ttk.Entry(frame, width=30,textvariable=title_input)
title_input.grid(row=0, column=1, padx=5, pady=5)

# Length label and entry
length_label = ttk.Label(frame, text="Enter the length (8-16):")
length_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
length_input = ttk.Entry(frame, width=10)
length_input.grid(row=1, column=1, padx=5, pady=5)

# Generate button
def on_generate():
    # Set the default title if empty
    if title_input.get().strip() == "":
        title_input.set("output")

    # Function to handle file writing
    def file_handler(title):
        filename = title.get().strip()
        # Append .txt if no extension is provided
        if "." not in filename:
            filename += ".txt"
        with open(filename, "w+") as file:
            file.write(f"{password}")

    try:
        length = int(length_input.get())
        if not 8 <= length <= 16:
            raise ValueError
        password = password_generator.generate(length=length)
        messagebox.showinfo(
            "Generated Password", f"Password: {password}\n(Copied to clipboard)"
        )
        file_handler(title_input)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid length (8-16).")


gen_button = ttk.Button(frame, text="Generate", command=on_generate)
gen_button.grid(row=2, column=0, columnspan=2, pady=15)

root.mainloop()
