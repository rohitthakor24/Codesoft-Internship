import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("350x350")

        tk.Label(root, text="Enter Password Length:").pack(pady=5)
        self.length_entry = tk.Entry(root)
        self.length_entry.pack(pady=5)

        self.use_upper = tk.IntVar()
        self.use_digits = tk.IntVar()
        self.use_special = tk.IntVar()

        tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.use_upper).pack()
        tk.Checkbutton(root, text="Include Numbers", variable=self.use_digits).pack()
        tk.Checkbutton(root, text="Include Special Characters", variable=self.use_special).pack()

        tk.Button(root, text="Generate Password", command=self.generate_password).pack(pady=15)
        self.result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=300)
        self.result_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 4:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Enter a valid length (minimum 4).")
            return

        characters = list(string.ascii_lowercase)
        if self.use_upper.get():
            characters += list(string.ascii_uppercase)
        if self.use_digits.get():
            characters += list(string.digits)
        if self.use_special.get():
            characters += list("!@#$%^&*()-_=+[]{};:,.<>?/")

        if not characters:
            messagebox.showerror("Selection Error", "Please select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.result_label.config(text=f"Generated Password: {password}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
