import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Click Counter App")
root.geometry("400x400") # Sedikit lebih tinggi agar tidak sesak
root.configure(bg="#f8f9fa") # Warna background lebih soft

# Counter Variable
counter = 0

# Increment Function
def increment():
    global counter
    counter += 1
    counter_label.config(text=f"Clicks: {counter}")

# Reset Function
def reset():
    global counter
    counter = 0
    counter_label.config(text="Clicks: 0")

# Title Label
title_label = tk.Label(root, text="Click Counter", font=("Helvetica", 24, "bold"), bg="#f8f9fa", fg="#333")
title_label.pack(pady=(30, 10))

# Counter Label
counter_label = tk.Label(root, text="Clicks: 0", font=("Courier New", 20), bg="#ffffff", fg="#2196f3", width=15, relief="flat")
counter_label.pack(pady=20)

# Styling Button common attributes
btn_config = {"font": ("Arial", 12, "bold"), "fg": "white", "width": 12, "cursor": "hand2", "bd": 0, "padx": 10, "pady": 5}

# Increment Button
increment_button = tk.Button(root, text="CLICK ME", command=increment, bg="#4caf50", **btn_config)
increment_button.pack(pady=10)

# Reset Button
reset_button = tk.Button(root, text="RESET", command=reset, bg="#ff9800", **btn_config)
reset_button.pack(pady=10)

# Exit Button
exit_button = tk.Button(root, text="EXIT", command=root.destroy, bg="#f44336", **btn_config)
exit_button.pack(pady=20)

# Run the App
root.mainloop()