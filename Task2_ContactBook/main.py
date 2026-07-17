import customtkinter as ctk
import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "contacts.json")
contacts = []

ctk.set_appearance_mode("System")

app = ctk.CTk()

app.title("Contact Book")
app.geometry("500x600")


title = ctk.CTkLabel(
    app,
    text="Contact Book",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)

name_label = ctk.CTkLabel(app, text="Name")
name_label.pack()

name_entry = ctk.CTkEntry(app, width=300)
name_entry.pack(pady=5)

phone_label = ctk.CTkLabel(app, text="Phone")
phone_label.pack()

phone_entry = ctk.CTkEntry(app, width=300)
phone_entry.pack(pady=5)

email_label = ctk.CTkLabel(app, text="Email")
email_label.pack()

email_entry = ctk.CTkEntry(app, width=300)
email_entry.pack(pady=5)
#funtions

def load_contacts():
    global contacts

    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                contacts = json.load(file)
        except json.JSONDecodeError:
            contacts = []


def delete_contact(contact):
    contacts.remove(contact)

    save_contacts()
    display_contacts()


def update_contact(contact):
    name_entry.delete(0, "end")
    phone_entry.delete(0, "end")
    email_entry.delete(0, "end")

    name_entry.insert(0, contact["name"])
    phone_entry.insert(0, contact["phone"])
    email_entry.insert(0, contact["email"])

    contacts.remove(contact)

    save_contacts()
    display_contacts()


def display_contacts():
    for widget in contacts_frame.winfo_children():
        widget.destroy()

    for contact in contacts:
        card = ctk.CTkFrame(contacts_frame)
        card.pack(fill="x", padx=10, pady=5)

        name_label = ctk.CTkLabel(
            card,
            text=f"Name : {contact['name']}",
            font=("Arial", 16, "bold")
        )
        name_label.pack(anchor="w", padx=10, pady=(8, 2))

        phone_label = ctk.CTkLabel(
            card,
            text=f"Phone : {contact['phone']}"
        )
        phone_label.pack(anchor="w", padx=10)

        email_label = ctk.CTkLabel(
            card,
            text=f"Email : {contact['email']}"
        )
        email_label.pack(anchor="w", padx=10, pady=(0, 8))

        button_frame = ctk.CTkFrame(card, fg_color="transparent")
        button_frame.pack(pady=5)

        update_button = ctk.CTkButton(
        button_frame,
        text="Update",
        width=90,
        command=lambda c=contact: update_contact(c)
        )
        update_button.pack(side="left", padx=5)

        delete_button = ctk.CTkButton(
        button_frame,
        text="Delete",
        width=90,
        command=lambda c=contact: delete_contact(c)
        )
        delete_button.pack(side="left", padx=5)


def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()

    if not name or not phone or not email:
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts()
    display_contacts()

    print(contacts)

    name_entry.delete(0, "end")
    phone_entry.delete(0, "end")
    email_entry.delete(0, "end")






add_button = ctk.CTkButton(
    app,
    text="Add Contact",
    command=add_contact
)
add_button.pack(pady=20)

contacts_frame = ctk.CTkScrollableFrame(app, width=420, height=250)
contacts_frame.pack(pady=10, fill="both", expand=True)

load_contacts()
display_contacts()
app.mainloop()