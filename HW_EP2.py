import tkinter as tk
import json
from tkinter import ttk

# Create the JSON file if it doesn't exist
with open("person.json", "a+") as f:
    f.seek(0)
    data = f.read()
    if not data:
        f.write("[]")

def save_info():
    # Get the values from the input fields
    name = name_entry.get()
    last_name = last_name_entry.get()
    job = job_entry.get()

    # Create a dictionary with the entered values
    person = {"name": name, "last_name": last_name, "job": job}

    # Read the saved JSON data from the file
    with open("person.json", "r") as f:
        saved_data = json.load(f)

    # Add the new person dictionary to the list of saved data
    saved_data.append(person)

    # Save the updated data to the file
    with open("person.json", "w") as f:
        json.dump(saved_data, f)

    # Clear the input fields
    name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    job_entry.delete(0, tk.END)

def display_info():
    # Read the saved JSON data from the file
    with open("person.json", "r") as f:
        saved_data = json.load(f)

    # Create a new window to display the saved data
    data_window = tk.Toplevel(GUI)
    data_window.title("Employee Information Data")
    data_window.geometry('400x200')
    data_window.config(bg='LightGreen')

    # Create a table to display the saved data
    table_frame = tk.Frame(data_window)
    table_frame.pack()

    # Create the table headers
    name_label = tk.Label(table_frame, text="Name", relief=tk.RIDGE, width=15)
    name_label.grid(row=0, column=0)
    last_name_label = tk.Label(table_frame, text="Last Name", relief=tk.RIDGE, width=15)
    last_name_label.grid(row=0, column=1)
    job_label = tk.Label(table_frame, text="Job", relief=tk.RIDGE, width=15)
    job_label.grid(row=0, column=2)

    # Insert the saved data into the table
    row_num = 1
    for person in saved_data:
        name = person["name"]
        last_name = person["last_name"]
        job = person["job"]

        # Create a label widget for each cell of the table
        name_label = tk.Label(table_frame, text=name, relief=tk.RIDGE, width=15)
        name_label.grid(row=row_num, column=0)
        last_name_label = tk.Label(table_frame, text=last_name, relief=tk.RIDGE, width=15)
        last_name_label.grid(row=row_num, column=1)
        job_label = tk.Label(table_frame, text=job, relief=tk.RIDGE, width=15)
        job_label.grid(row=row_num, column=2)

        row_num += 1

# Create main program
GUI = tk.Tk()
GUI.title("Personal Information")
GUI.geometry('400x200')
GUI.configure(bg='LightBlue')

# Create input text boxs
name_label = tk.Label(GUI, text="Name: ")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(GUI)
name_entry.grid(row=0, column=1, padx=5, pady=5)
name_entry.focus()  # Set the focus to the name entry field

last_name_label = tk.Label(GUI, text="Last Name: ")
last_name_label.grid(row=1, column=0, padx=5, pady=5)
last_name_entry = tk.Entry(GUI)
last_name_entry.grid(row=1, column=1, padx=5, pady=5)

job_label = tk.Label(GUI, text="Job: ")
job_label.grid(row=2, column=0, padx=5, pady=5)
job_entry = tk.Entry(GUI)
job_entry.grid(row=2, column=1, padx=5, pady=5)

# Add Button
save_button = tk.Button(GUI, text="Submit", command=save_info)
save_button.grid(row=3, column=0, padx=5, pady=5)

display_button = tk.Button(GUI, text="Display Info", command=display_info)
display_button.grid(row=3, column=1, padx=5, pady=5)

# Start Tkinter event loop
GUI.mainloop()