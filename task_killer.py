import os
import psutil
import tkinter as tk
from tkinter import messagebox, ttk

class TaskKillerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TaskKiller")
        self.root.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=("PID", "Name", "Status"), show="headings")
        self.tree.heading("PID", text="PID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Status", text="Status")
        self.tree.pack(expand=True, fill=tk.BOTH)

        refresh_button = tk.Button(self.root, text="Refresh", command=self.refresh_processes)
        refresh_button.pack(side=tk.LEFT, padx=10, pady=10)

        kill_button = tk.Button(self.root, text="Kill Process", command=self.kill_process)
        kill_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.refresh_processes()

    def refresh_processes(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for process in psutil.process_iter(['pid', 'name', 'status']):
            self.tree.insert("", "end", values=(process.info['pid'], process.info['name'], process.info['status']))

    def kill_process(self):
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning("Select Process", "Please select a process to terminate.")
            return

        pid = int(self.tree.item(selected_item, 'values')[0])

        try:
            os.kill(pid, 9)
            messagebox.showinfo("Success", f"Process {pid} terminated.")
            self.refresh_processes()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to terminate process {pid}. Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskKillerApp(root)
    root.mainloop()