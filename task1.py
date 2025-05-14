import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack()

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        done_button = tk.Button(root, text="Mark as Done", command=self.mark_done)
        done_button.pack(pady=5)

        update_button = tk.Button(root, text="Update Task", command=self.update_task)
        update_button.pack(pady=5)

        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.refresh_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index] = self.tasks[index] + " ✔"
            self.refresh_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task.")

    def update_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            new_task = simpledialog.askstring("Update Task", "Enter new task:")
            if new_task:
                self.tasks[index] = new_task
                self.refresh_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.refresh_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task.")

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
