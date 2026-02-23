import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

# Konfigurasi Warna & Font 
BG_COLOR = "#f4f7f6"        # Abu-abu sangat muda (Background)
PRIMARY_COLOR = "#2c3e50"   # Biru tua (Header/Teks Utama)
ACCENT_COLOR = "#3498db"    # Biru cerah (Button Add)
DANGER_COLOR = "#e74c3c"    # Merah (Button Delete/Exit)
SECONDARY_COLOR = "#95a5a6" # Abu-abu (Button Clear)
TEXT_COLOR = "#2c3e50"

# File for storing expenses
EXPENSE_FILE = "expenses.csv"

# Create Main Application Window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("600x650")
root.configure(bg=BG_COLOR)

# Expense Data List
expenses = []

# Load Existing Expenses from CSV
def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        try:
            with open(EXPENSE_FILE, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row: # Pastikan baris tidak kosong
                        expenses.append(row)
                        expense_listbox.insert(tk.END, f"{row[0]} | Rp {row[1]} | {row[2]}")
        except Exception as e:
            print(f"Error loading file: {e}")

# Save Expenses to CSV
def save_expenses():
    with open(EXPENSE_FILE, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for expense in expenses:
            writer.writerow(expense)

# Add Expense
def add_expense():
    category = category_var.get()
    amount = amount_entry.get()
    description = description_entry.get()
    
    if not amount.isdigit() or category == "Pilih Kategori" or not description:
        messagebox.showerror("Input Tidak Valid", "Mohon masukkan detail pengeluaran dengan benar.")
        return
    
    expenses.append([category, amount, description])
    expense_listbox.insert(tk.END, f"{category} | Rp {amount} | {description}")
    calculate_total()
    clear_inputs()
    save_expenses()

# Delete Selected Expense
def delete_expense():
    selected = expense_listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Pilih pengeluaran yang ingin dihapus.")
        return
    
    index = selected[0]
    del expenses[index]
    expense_listbox.delete(index)
    calculate_total()
    save_expenses()

# Clear All Inputs
def clear_inputs():
    category_var.set("Pilih Kategori")
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

# Calculate Total Expenses
def calculate_total():
    total = sum(float(expense[1]) for expense in expenses)
    # Menggunakan format ribuan agar lebih mudah dibaca (e.g. 1.000.000)
    total_label.config(text=f"Total Pengeluaran: Rp {total:,.0f}".replace(",", "."))

# Clear All Expenses
def clear_all():
    if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus semua data?"):
        expenses.clear()
        expense_listbox.delete(0, tk.END)
        calculate_total()
        save_expenses()

# --- GUI Layout ---

# Title
title_label = tk.Label(root, text="💸 Expense Tracker", font=("Helvetica", 24, "bold"), bg=BG_COLOR, fg=PRIMARY_COLOR)
title_label.pack(pady=20)

# Input Frame
input_frame = tk.Frame(root, bg=BG_COLOR)
input_frame.pack(pady=10, padx=20)

# Category
tk.Label(input_frame, text="Kategori:", font=("Helvetica", 11), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, sticky="w", pady=5)
category_var = tk.StringVar(value="Pilih Kategori")
category_dropdown = ttk.Combobox(input_frame, textvariable=category_var, values=["Makanan", "Transportasi", "Sewa", "Utilitas", "Hiburan", "Lainnya"], width=27)
category_dropdown.grid(row=0, column=1, padx=10, pady=5)

# Amount
tk.Label(input_frame, text="Jumlah (Rp):", font=("Helvetica", 11), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=1, column=0, sticky="w", pady=5)
amount_entry = tk.Entry(input_frame, font=("Helvetica", 11), width=30)
amount_entry.grid(row=1, column=1, padx=10, pady=5)

# Description
tk.Label(input_frame, text="Keterangan:", font=("Helvetica", 11), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=2, column=0, sticky="w", pady=5)
description_entry = tk.Entry(input_frame, font=("Helvetica", 11), width=30)
description_entry.grid(row=2, column=1, padx=10, pady=5)

# Buttons Frame
btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.pack(pady=20)

add_button = tk.Button(btn_frame, text="Tambah", command=add_expense, bg=ACCENT_COLOR, fg="white", width=12, font=("Helvetica", 10, "bold"), relief="flat")
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(btn_frame, text="Hapus", command=delete_expense, bg=DANGER_COLOR, fg="white", width=12, font=("Helvetica", 10, "bold"), relief="flat")
delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(btn_frame, text="Hapus Semua", command=clear_all, bg=SECONDARY_COLOR, fg="white", width=12, font=("Helvetica", 10, "bold"), relief="flat")
clear_button.grid(row=0, column=2, padx=5)

# Expense Listbox with Scrollbar
list_frame = tk.Frame(root, bg=BG_COLOR)
list_frame.pack(pady=10, padx=20)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

expense_listbox = tk.Listbox(list_frame, width=60, height=10, yscrollcommand=scrollbar.set, font=("Courier", 10), borderwidth=0, highlightthickness=1)
expense_listbox.pack()

scrollbar.config(command=expense_listbox.yview)

# Total Label
total_label = tk.Label(root, text="Total Pengeluaran: Rp 0", font=("Helvetica", 16, "bold"), bg=BG_COLOR, fg=PRIMARY_COLOR)
total_label.pack(pady=15)

# Load Previous Data
load_expenses()
calculate_total()

# Exit Button
exit_button = tk.Button(root, text="Keluar", command=root.destroy, bg=PRIMARY_COLOR, fg="white", width=20, font=("Helvetica", 10), relief="flat")
exit_button.pack(pady=10)

# Run Application
root.mainloop()