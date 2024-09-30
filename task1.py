import tkinter as tk
from tkinter import messagebox, font
import csv

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    
    if name and email and age:
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Age: {age}")
        
        # Write data to CSV file
        with open('registration_data.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            
            # Check if the file is empty (no header row)
            if csv_file.tell() == 0:
                # Write the header row
                csv_writer.writerow(["Name", "Email", "Age"])
            
            # Write the user data
            csv_writer.writerow([name, email, age])
        
        messagebox.showinfo("Success", "Registration successful!")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

root = tk.Tk()
root.title("Registration Form")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

title_font = font.Font(family="Helvetica", size=16, weight="bold")
label_font = font.Font(family="Helvetica", size=10)
button_font = font.Font(family="Helvetica", size=10, weight="bold")

title_label = tk.Label(root, text="Registration Form", font=title_font, bg="#f0f0f0", fg="#333333")
title_label.pack(pady=20)

form_frame = tk.Frame(root, bg="#f0f0f0")
form_frame.pack(pady=10)

tk.Label(form_frame, text="Name:", font=label_font, bg="#f0f0f0", fg="#333333").grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(form_frame, font=label_font, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Email:", font=label_font, bg="#f0f0f0", fg="#333333").grid(row=1, column=0, padx=5, pady=5, sticky="e")
email_entry = tk.Entry(form_frame, font=label_font, width=30)
email_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Age:", font=label_font, bg="#f0f0f0", fg="#333333").grid(row=2, column=0, padx=5, pady=5, sticky="e")
age_entry = tk.Entry(form_frame, font=label_font, width=30)
age_entry.grid(row=2, column=1, padx=5, pady=5)

submit_button = tk.Button(root, text="Submit", command=submit_form, font=button_font, bg="#4CAF50", fg="white", activebackground="#45a049", activeforeground="white", relief=tk.FLAT, padx=20, pady=10)
submit_button.pack(pady=20)

root.mainloop()