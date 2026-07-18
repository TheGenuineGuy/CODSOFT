import customtkinter as ctk
import random
import string

ctk.set_appearance_mode("System")

app = ctk.CTk()

app.title("Password Generator")
app.geometry("500x400")
app.resizable(False, False)

#functions

def generate_password():

    try:
        length = int(length_entry.get())

        if length <= 0:
            return

    except ValueError:
        return

    characters = ""

    if letters_var.get():
        characters += string.ascii_letters

    if numbers_var.get():
        characters += string.digits

    if symbols_var.get():
        characters += string.punctuation

    if not characters:
        return

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    password_entry.delete(0, "end")
    password_entry.insert(0, password)
    


title = ctk.CTkLabel(
    app,
    text="Password Generator",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)

length_entry = ctk.CTkEntry(
    app,
    width=250,
    placeholder_text="Password Length"
)
length_entry.pack(pady=10)
letters_var = ctk.BooleanVar(value=True)
numbers_var = ctk.BooleanVar(value=True)
symbols_var = ctk.BooleanVar(value=True)

letters_check = ctk.CTkCheckBox(
    app,
    text="Letters",
    variable=letters_var
)
letters_check.pack(pady=(0, 15))

numbers_check = ctk.CTkCheckBox(
    app,
    text="Numbers",
    variable=numbers_var
)
numbers_check.pack(pady=(0, 15))

symbols_check = ctk.CTkCheckBox(
    app,
    text="Symbols",
    variable=symbols_var
)
symbols_check.pack(pady=(0, 15))



password_entry = ctk.CTkEntry(
    app,
    width=350,
    height=40
)
password_entry.pack(pady=20)

copy_button = ctk.CTkButton(
    app,
    text="Copy Password",
    command=lambda: app.clipboard_append(password_entry.get())
)
copy_button.pack()

generate_button = ctk.CTkButton(
    app,
    text="Generate Password",
    command=generate_password
)
generate_button.pack(pady=10)

app.mainloop()