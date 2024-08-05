import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import database

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("400x500")
        self.tasks = []

        self.create_widgets()
        self.load_tasks()

    def create_widgets(self):
        # Title Label
        title_label = ttk.Label(self.root, text="Task Manager", font=("Helvetica", 18))
        title_label.pack(pady=20)

        # Frame for Task List
        frame = ttk.Frame(self.root)
        frame.pack(pady=10)

        # Task Listbox
        self.task_listbox = tk.Listbox(frame, width=40, height=15, font=("Helvetica", 12))
        self.task_listbox.pack(side="left", fill="y")

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient="vertical")
        scrollbar.config(command=self.task_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.task_listbox.config(yscrollcommand=scrollbar.set)

        # Buttons Frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)

        # Add Task Button
        add_button = ttk.Button(button_frame, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=0, padx=10)

        # Edit Task Button
        edit_button = ttk.Button(button_frame, text="Edit Task", command=self.edit_task)
        edit_button.grid(row=0, column=1, padx=10)

        # Delete Task Button
        delete_button = ttk.Button(button_frame, text="Delete Task", command=self.delete_task)
        delete_button.grid(row=1, column=0, padx=10, pady=10)

        # Complete Task Button
        complete_button = ttk.Button(button_frame, text="Mark as Complete", command=self.toggle_task_completion)
        complete_button.grid(row=1, column=1, padx=10, pady=10)

    def load_tasks(self):
        self.tasks = database.get_all_tasks()
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_text = f"{'[x]' if task[3] else '[ ]'} {task[1]}: {task[2]}"
            self.task_listbox.insert(tk.END, task_text)

    def add_task(self):
        title = simpledialog.askstring("Add Task", "Enter task title:")
        if title:
            description = simpledialog.askstring("Add Task", "Enter task description:")
            database.add_task(title, description)
            self.load_tasks()

    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_id = self.tasks[selected_index[0]][0]
            new_title = simpledialog.askstring("Edit Task", "Enter new task title:", initialvalue=self.tasks[selected_index[0]][1])
            new_description = simpledialog.askstring("Edit Task", "Enter new task description:", initialvalue=self.tasks[selected_index[0]][2])
            if new_title:
                database.update_task(task_id, new_title, new_description, self.tasks[selected_index[0]][3])
                self.load_tasks()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_id = self.tasks[selected_index[0]][0]
            database.delete_task(task_id)
            self.load_tasks()

    def toggle_task_completion(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            database.update_task(task[0], task[1], task[2], not task[3])
            self.load_tasks()

if __name__ == "__main__":
    database.create_table()
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
