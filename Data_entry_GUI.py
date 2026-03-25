#Write a Python program that writes data to a CSV file using the Tkinter.

#Importing the required module #Tkinter is the standard python library
import tkinter as tk
from tkinter import ttk
import csv

# ( Defined the function to save the data) #Tkinter is the standard python library for creating GUI
# This function is triggered when the user clicks the "Save to CSV" button
def save_to_csv():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    
    with open('output.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, email])
    
    # Clear the entry boxes after saving
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

#window creation
# creates the main app window
#sets the window to data entry
root = tk.Tk()
root.title("Data Entry")

# Create and place the labels and entry boxes
#cretes label and input field for name/rows/columns/email/age
ttk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5)
age_entry = ttk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
email_entry = ttk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

# Create and place the save button
#The button which creates save to cvs is created
#when clicked it calles save to file function
save_button = ttk.Button(root, text="Save to CSV", command=save_to_csv)
save_button.grid(row=3, columnspan=2, pady=10)

# Run the application
root.mainloop()

    

