import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []
        self.selected_index = None

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, pady=10)
        self.populate_listbox()

        update_button = tk.Button(root, text="Update Your Task", command=self.update_task)
        update_button.grid(row=2, column=0, pady=10)

        delete_button = tk.Button(root, text="Delete Your Task", command=self.delete_task)
        delete_button.grid(row=2, column=1, pady=10)

        self.task_listbox.bind("<<ListboxSelect>>", self.on_task_select)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.populate_listbox()
            messagebox.showinfo("Task Added", f"Task '{task}' added to the to-do list.")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Please enter a task.")

    def update_task(self):
        selected_task_index = self.get_selected_index()
        if selected_task_index is not None:
            edited_task = self.task_entry.get()
            if edited_task:
                self.tasks[selected_task_index] = edited_task
                self.populate_listbox()
                messagebox.showinfo("Task Updated", f"Task updated to '{edited_task}'.")
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Please enter a task.")
        else:
            messagebox.showwarning("Please select a task to update.")

    def delete_task(self):
        selected_task_index = self.get_selected_index()
        if selected_task_index is not None:
            deleted_task = self.tasks.pop(selected_task_index)
            self.populate_listbox()
            messagebox.showinfo("Task Deleted", f"Task '{deleted_task}' deleted.")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Please select a task to delete.")

    def on_task_select(self, event):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.selected_index = selected_task_index[0]
            selected_task = self.tasks[self.selected_index]
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(tk.END, selected_task)

    def get_selected_index(self):
        return self.selected_index

    def populate_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()