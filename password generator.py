import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    # Define character sets for different complexity levels
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine character sets based on user choice (you can customize this)
    characters = lower_letters + upper_letters + digits + special_chars

    # Generate the password using random.choice
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_and_show_dialog():
    try:
        length = int(length_entry.get())
        if length < 1:
            messagebox.showerror("Error", "Please enter a valid length (greater than 0).")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number for length.")
        return

    password = generate_password(length)
    messagebox.showinfo("Generated Password", f"Your generated password is: {password}")

# Create a GUI window
window = tk.Tk()
window.title("Password_Generator")

# Increase the dialog box size
window.geometry("400x200")  # Adjust width and height as needed

# Label and Entry for password length
length_label = tk.Label(window, text="Enter the desired length of the password:",bg='green')
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Generate button
generate_button = tk.Button(window, text="Generate Password", command=generate_password_and_show_dialog,bg='orange')
generate_button.pack()

window.mainloop()
