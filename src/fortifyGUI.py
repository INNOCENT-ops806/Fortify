import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
import password_generator


def launch_gui():
    root = tk.Tk()
    root.title("Fortify")
    root.geometry("900x500")
    style = Style(theme="vapor")  # noqa: F841
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    frame = ttk.LabelFrame(root, text="Password Generator", padding=20)
    frame.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")

    title_label = ttk.Label(frame, text="Enter title of the password:")
    title_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    title_input_var = tk.StringVar()
    title_input = ttk.Entry(frame, width=30, textvariable=title_input_var)
    title_input.grid(row=0, column=1, padx=5, pady=5)

    length_label = ttk.Label(frame, text="Enter the length (8-16):")
    length_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    length_input = ttk.Entry(frame, width=10)
    length_input.grid(row=1, column=1, padx=5, pady=5)

    def on_generate():
        def file_handler(title):
            filename = title.get().strip() or "output.txt"
            if "." not in filename:
                filename += ".txt"
            # Increment filename if exists
            base, ext = filename.rsplit(".", 1)
            ext = "." + ext
            counter = 1
            new_filename = filename
            import os

            while os.path.exists(new_filename):
                new_filename = f"{base}{counter}{ext}"
                counter += 1
            with open(new_filename, "w+") as file:
                file.write(password)

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


if __name__ == "__main__":
    launch_gui()
