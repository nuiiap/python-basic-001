import csv
import sys
import os
import tkinter as tk
from tkinter import ttk
import datetime

sys.stdout.reconfigure(encoding='utf-8')

# Get current datetime
curr_time = datetime.datetime.now()
curr_fmtm = curr_time.strftime("%Y%m%d %H:%M:%S")
# print(curr_fmtm)

def writecsv():
    datalist = [curr_fmtm, name_entry.get(), last_name_entry.get(), age_entry.get()]
    file_exists = os.path.isfile('./lesson4/data.csv')
    with open('./lesson4/data.csv', 'a', encoding='utf-8', newline='' ) as csvfile:
        fw = csv.writer(csvfile)
        if not file_exists:
            fw.writerow(['TimeStamp', 'Name', 'LastName', 'Age'])
        fw.writerow(datalist)

        #clear text box
    name_entry.delete(0, 'end')
    last_name_entry.delete(0, 'end')
    age_entry.delete(0, 'end')

def readcsv():
    display_text.delete('1.0', tk.END)
    with open('./lesson4/data.csv', encoding='utf-8', newline='' ) as csvfile:
        fr = csv.reader(csvfile)
        data = list(fr)
        # print(data)
        for row in data:
            # print(row)
            display_text.insert(tk.END, ', '.join(row) + '\n')

    # return(data)

GUI = tk.Tk()
GUI.title("Data Entry and Display")
GUI.geometry('700x550')
GUI.configure(bg='LightGreen')

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

age_label = tk.Label(GUI, text="Age: ")
age_label.grid(row=2, column=0, padx=5, pady=5)
age_entry = tk.Entry(GUI)
age_entry.grid(row=2, column=1, padx=5, pady=5)

# Add Button
save_button = tk.Button(GUI, text="Save to CSV", command=writecsv)
save_button.grid(row=3, column=0, padx=5, pady=5)

display_button = tk.Button(GUI, text="Display Info", command=readcsv)
display_button.grid(row=3, column=1, padx=5, pady=5)

display_text = tk.Text(GUI)
display_text.grid(row=4, column=0, columnspan=4)
#display_text.grid(row=4, column=0, padx=5, pady=5)

GUI.mainloop()