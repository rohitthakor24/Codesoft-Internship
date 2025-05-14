import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x300")

        tk.Label(root, text="Enter First Number:").pack(pady=5)
        self.num1_entry = tk.Entry(root)
        self.num1_entry.pack(pady=5)

        tk.Label(root, text="Enter Second Number:").pack(pady=5)
        self.num2_entry = tk.Entry(root)
        self.num2_entry.pack(pady=5)

        tk.Label(root, text="Choose Operation:").pack(pady=10)

        tk.Button(root, text="+ Add", command=self.add).pack(pady=2)
        tk.Button(root, text="- Subtract", command=self.subtract).pack(pady=2)
        tk.Button(root, text="× Multiply", command=self.multiply).pack(pady=2)
        tk.Button(root, text="÷ Divide", command=self.divide).pack(pady=2)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=20)

    def get_inputs(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return None, None

    def add(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            result = num1 + num2
            self.result_label.config(text=f"Result: {result}")

    def subtract(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            result = num1 - num2
            self.result_label.config(text=f"Result: {result}")

    def multiply(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            result = num1 * num2
            self.result_label.config(text=f"Result: {result}")

    def divide(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            if num2 == 0:
                messagebox.showerror("Math Error", "Cannot divide by zero.")
            else:
                result = num1 / num2
                self.result_label.config(text=f"Result: {result}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()
