import tkinter as tk

dataDict = { 'somchai':20, 'somsak':15, 'sompong':21, 'somkiat':25}

def checkAge(key):
    value = dataDict[key]
    value_field.delete(1.0, tk.END)
    value_field.insert(tk.END, value)

window = tk.Tk()
window.title("Check Age")
window.geometry('250x150')
window.configure(bg='LightBlue')

for row,key in enumerate(dataDict, start=1):    
    button = tk.Button(window, text=key, command=lambda key=key: checkAge(key))  
    button.grid(row=row, column=0)

value_label = tk.Label(window, text="Age is: ")
value_label.grid(row=0, column=0)
value_field = tk.Text(window, height=1, width=5)
value_field.grid(row=0, column=1)

window.mainloop()