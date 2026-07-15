import customtkinter as ctk
import json
import os

FILE_NAME = "todo.json"
tasks = []

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("My To-Do List")
app.geometry("500x600")
app.resizable(False, False)

title = ctk.CTkLabel(
    app,
    text="TO-DO LIST",
    font=("Arial", 28, "bold")
)
title.pack(pady=(20, 15))

entry = ctk.CTkEntry(
    app,
    width=320,
    height=40,
    placeholder_text="Enter a task..."
)

entry.bind("<Return>", lambda event: add_task())
entry.pack(pady=5)

#fucntions

def create_task(task_text, completed=False):

    row = ctk.CTkFrame(task_frame)
    row.pack(fill="x", padx=5, pady=5)

    checkbox = ctk.CTkCheckBox(
        row,
        text=task_text
    )

    checkbox.pack(side="left", padx=10)

    if completed:
        checkbox.select()

    def delete_task():
        row.destroy()
        tasks.remove(task)
        save_tasks()

    delete_btn = ctk.CTkButton(
        row,
        text="Delete",
        width=70,
        fg_color="#c0392b",
        hover_color="#96281B",
        command=delete_task
    )

    delete_btn.pack(side="right", padx=10)

    checkbox.configure(command=save_tasks)

    task = {
        "frame": row,
        "checkbox": checkbox
    }

    tasks.append(task)
    save_tasks()


def add_task():

    task = entry.get().strip()

    if not task:
        return

    create_task(task)

    

    entry.delete(0, "end")


def save_tasks():

    data = []

    for task in tasks:

        data.append({
            "task": task["checkbox"].cget("text"),
            "completed": bool(task["checkbox"].get())
        })

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def load_tasks():

    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []

    for task in data:
        create_task(
            task["task"],
            task["completed"]
        )
add_button = ctk.CTkButton(
    app,
    text="Add Task",
    width=120,
    height=40,
    command=add_task
)
add_button.pack(pady=15)

task_frame = ctk.CTkScrollableFrame(
    app,
    width=430,
    height=330
)
task_frame.pack(padx=20, pady=10, fill="both", expand=True)



load_tasks()
app.mainloop()

