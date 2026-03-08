import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_URL = "http://localhost:5000"

# ---------------- API FUNCTIONS ---------------- #

def load_members():

    for row in table.get_children():
        table.delete(row)

    try:
        r = requests.get(f"{API_URL}/members")
        members = r.json()

        for m in members:
            table.insert(
                "",
                tk.END,
                values=(
                    m["_id"],
                    m["name"],
                    m["age"],
                    m["weight"],
                    m["height"],
                    m["membership"],
                    m["expiry"]
                )
            )

        status_var.set("Members loaded successfully")

    except:
        messagebox.showerror("Error", "Cannot fetch members")


def add_member():

    try:
        data = {
            "name": name_var.get(),
            "age": int(age_var.get()),
            "weight": float(weight_var.get()),
            "height": float(height_var.get()),
            "membership": membership_var.get()
        }

        requests.post(f"{API_URL}/members", json=data)

        messagebox.showinfo("Success", "Member Added")
        load_members()

    except:
        messagebox.showerror("Error", "Invalid input")


def delete_member():

    selected = table.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a member")
        return

    item = table.item(selected[0])
    member_id = item["values"][0]

    requests.delete(f"{API_URL}/members/{member_id}")

    messagebox.showinfo("Deleted", "Member removed")

    load_members()


def calculate_bmi():

    try:

        data = {
            "weight": float(weight_var.get()),
            "height": float(height_var.get())
        }

        r = requests.post(f"{API_URL}/bmi", json=data)

        bmi = r.json()["BMI"]

        messagebox.showinfo("BMI Result", f"Your BMI is {bmi}")

    except:
        messagebox.showerror("Error", "Invalid values")


def check_expired():

    r = requests.get(f"{API_URL}/membership/expired")

    expired = r.json()

    if not expired:
        messagebox.showinfo("Status", "No expired memberships")
        return

    names = "\n".join([m["name"] for m in expired])

    messagebox.showwarning("Expired Members", names)


# ---------------- UI ---------------- #

root = tk.Tk()
root.title("ACEest Gym Management System")
root.geometry("1100x600")
root.configure(bg="#eef1f5")


# Sidebar
sidebar = tk.Frame(root, bg="#2c3e50", width=200)
sidebar.pack(side="left", fill="y")

title = tk.Label(
    sidebar,
    text="ACEest\nGym",
    fg="white",
    bg="#2c3e50",
    font=("Arial", 18, "bold")
)
title.pack(pady=20)


def sidebar_button(text, command):

    btn = tk.Button(
        sidebar,
        text=text,
        command=command,
        width=20,
        bg="#34495e",
        fg="white",
        relief="flat",
        pady=8
    )
    btn.pack(pady=5)


sidebar_button("Refresh Members", load_members)
sidebar_button("Expired Membership", check_expired)


# Main Area
main = tk.Frame(root, bg="#eef1f5")
main.pack(side="right", fill="both", expand=True)


header = tk.Label(
    main,
    text="Gym Member Dashboard",
    font=("Arial", 20, "bold"),
    bg="#eef1f5"
)
header.pack(pady=10)


# Form Card
form_card = tk.Frame(main, bg="white", padx=20, pady=20)
form_card.pack(fill="x", padx=20, pady=10)


name_var = tk.StringVar()
age_var = tk.StringVar()
weight_var = tk.StringVar()
height_var = tk.StringVar()
membership_var = tk.StringVar()


def form_field(parent, label, var):

    row = tk.Frame(parent, bg="white")
    row.pack(fill="x", pady=5)

    tk.Label(row, text=label, width=15, bg="white").pack(side="left")

    tk.Entry(row, textvariable=var).pack(side="left", fill="x", expand=True)


form_field(form_card, "Name", name_var)
form_field(form_card, "Age", age_var)
form_field(form_card, "Weight", weight_var)
form_field(form_card, "Height", height_var)
form_field(form_card, "Membership", membership_var)


# Buttons
button_frame = tk.Frame(main, bg="#eef1f5")
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Add Member",
    bg="#27ae60",
    fg="white",
    width=15,
    command=add_member
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Delete Member",
    bg="#e74c3c",
    fg="white",
    width=15,
    command=delete_member
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Calculate BMI",
    bg="#f39c12",
    fg="white",
    width=15,
    command=calculate_bmi
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="Refresh",
    bg="#3498db",
    fg="white",
    width=15,
    command=load_members
).grid(row=0, column=3, padx=5)


# Table Card
table_card = tk.Frame(main, bg="white")
table_card.pack(fill="both", expand=True, padx=20, pady=10)


columns = ("ID", "Name", "Age", "Weight", "Height", "Membership", "Expiry")

table = ttk.Treeview(table_card, columns=columns, show="headings")

for col in columns:
    table.heading(col, text=col)

table.column("ID", width=0, stretch=False)

table.pack(fill="both", expand=True)


# Scrollbar
scroll = ttk.Scrollbar(table_card, command=table.yview)
table.configure(yscrollcommand=scroll.set)
scroll.pack(side="right", fill="y")


# Status bar
status_var = tk.StringVar()
status_var.set("Ready")

status = tk.Label(
    root,
    textvariable=status_var,
    bg="#bdc3c7",
    anchor="w"
)
status.pack(fill="x", side="bottom")


load_members()

root.mainloop()