# todo_list_app.py

import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = self.load_tasks()

        # Create GUI components
        self.task_list_frame = tk.Frame(self.root)
        self.task_list_frame.pack(fill="both", expand=True)

        self.task_list = tk.Listbox(self.task_list_frame, width=40)
        self.task_list.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self.task_list_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.task_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_list.yview)

        self.add_task_frame = tk.Frame(self.root)
        self.add_task_frame.pack(fill="x")

        self.task_entry = tk.Entry(self.add_task_frame, width=30)
        self.task_entry.pack(side="left")

        self.add_button = tk.Button(self.add_task_frame, text="Add", command=lambda: self.add_task(self.task_entry.get()))
        self.add_button.pack(side="left")

        self.remove_button = tk.Button(self.add_task_frame, text="Remove", command=self.remove_task)
        self.remove_button.pack(side="left")

        self.complete_button = tk.Button(self.add_task_frame, text="Complete", command=self.complete_task)
        self.complete_button.pack(side="left")

        # Load tasks into the list
        for task in self.tasks:
            self.task_list.insert("end", task)

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for i in range(self.task_list.size()):
                f.write(self.task_list.get(i) + "\n")

    def add_task(self, task):
        if task:
            self.task_list.insert("end", task)
            self.task_entry.delete(0, "end")
            self.save_tasks()
        else:
            messagebox.showerror("Error", "Please enter a task")

    def remove_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            self.save_tasks()
        except IndexError:
            messagebox.showerror("Error", "Select a task to remove")

    def complete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            task = self.task_list.get(task_index)
            if not task.startswith("[x] "):
                self.task_list.delete(task_index)
                self.task_list.insert(task_index, "[x] " + task)
            self.save_tasks()
        except IndexError:
            messagebox.showerror("Error", "Select a task to complete")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    app.run()