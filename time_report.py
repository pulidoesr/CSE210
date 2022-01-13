import tkinter as tk
from tkinter.constants import E
from tkinter import *
from datetime import datetime
import os
from isoweek import Week
import csv
import pandas as pd
import numpy as np

my_entries = []
text_var = []
entries = []
rows, cols = (11,5)
date_range = ''
k_employee = 0
week_num = 0
m_employee = []
m_week = []
# working days 
weekdays = [ "Mon", "Tue", "Wed", "Thu", "Fri"]
# work concepts
workconcept = [ "Meetings", "e-Mail", "IT Research", "Vendor Management", "Troubleshooting", "Conference",
        "Development", "Documentation", "Testing", "Support", "PTO"]
# Each item in the people dictionary is a key value pair.
    # Each key is a unique identifier
employee_dict = {        
        "143": ["James Waddington"],
        "338": ["John Thur"],
        "201": ["Rick Ledford"],
        "203": ["Kevin Grimm"],
        "128": ["Alex Tarabay"],
        "342": ["Tammy Woods"],
        "202": ["Charbel Azzi"],
        "132": ["Paul Gaylord"],
        "445": ["Dan Barness"]
    }
def main():
    # Create the Tk root object.
    frm_main = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    # frm_main = tk.Frame(root)
    frm_main.title('Frontier IT Management - Time Reporting')
    frm_main.iconbitmap('C:/Users/EPULID/Downloads/FrontierLogo.ico')

    # frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
    frm_main.geometry("660x500+120+120")

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    
    populate_main_window(frm_main)
    

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    frm_main.mainloop()

# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and each
# widget is an object, the code to make a GUI usually has many variables
# to store the many objects. Because there are so many variable names,
# programmers often adopt a naming convention to help a programmer keep
# track of all the variables. One popular naming convention is to type a
# three letter prefix in front of the names of all variables that store
# GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click

def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main window
    Return: nothing
    """
    # Start the tkinter matrix to capture the hours
    def multipleentry(frm_main): 
        x2 = 0
        y2 = 0
        for x in range(2,7):
            dayslabel = Label(frm_main,text = weekdays[x-2])
            dayslabel.place(x=460 + x2, y=75)
            x2 += 30
        for y in range(2,13):
            worklabel = Label(frm_main, text = workconcept[y-2])
            worklabel.place(x=315, y=100 + y2)
            y2 += 30
        x2 = 0
        y2 = 0
        for y in range(2,13):
            text_var.append([])
            entries.append([])
            i = y - 2
            for x in range(2,7):
                j = x - 2
                # my_entry= Entry(frm_main, justify=RIGHT, width=5)
                # my_entry.grid(row=y, column=x, pady=20, padx=5)
                text_var[i].append(StringVar())
                entries[i].append(Entry(frm_main, textvariable=text_var[i][j],width=5))
                entries[i][j].place(x=460 + x2, y=100 + y2)
                x2 += 30
            y2 += 30
            x2 = 0
        btn_submit.place(x=360, y=450)
        btn_clear.place(x=530, y=450)

    # Create a labels for data entry"
    lbl_employee = tk.Label(frm_main, text="Input employee number: ")
    lbl_employee_name = tk.Label(frm_main, text="")
    lbl_date = tk.Label(frm_main, text="Input date report (YYYY-MM-DD): ")
    lbl_status = Label(frm_main, text="")

    # Create data entry box where the user will enter the data of the report.
    ent_employee = tk.Entry(frm_main, justify=RIGHT, width=10)
    ent_date = tk.Entry(frm_main, justify=RIGHT, width=10)     
    

    # Create the buttons: Create, Submit, Clear.
    btn_create = tk.Button(frm_main, text="Create report")
    btn_submit = tk.Button(frm_main, text="Submit report")
    btn_clear = tk.Button(frm_main, text="Clear report")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_employee.grid(row=0, column=0, padx=3, pady=3)
    lbl_date.grid(row=1, column=0, padx=3, pady=3)
    ent_employee.grid(row=0, column=1, padx=3, pady=3)
    ent_date.grid(row=1, column=1, padx=3, pady=3)
    btn_create.grid(row=1, column=2, padx=3, pady=3, sticky="W")

# This function will be called each time a new employee is enter
    def employee_lookup(event):
        k_employee = ent_employee.get()
        if len(k_employee) == 3:
            if k_employee in employee_dict:
                name_key = 0
                value = employee_dict[k_employee]
                name = value[name_key]
                lbl_employee_name = Label(frm_main, text = name)
                lbl_employee_name.place(x=420, y=5)
                if len(m_employee) == 0:
                    for i in range(rows):
                        m_employee.append(k_employee)

            else:
                lbl_employee_name = Label(frm_main, text= "Employee not found")
                lbl_employee_name.place(x=420, y=5)
        pass
    
    ent_employee.bind("<KeyRelease>", employee_lookup)

    # This function will be called each time
    # the user presses the "Clear" button.
    # Give the keyboard focus to the radio entry box.
    
    def create():
        """Create the report"""
        a_date = ent_date.get()
        error = verifydate(a_date)
        if error == "":
           week_num = dateformat(a_date) 
           multipleentry(frm_main)
        else:
            lbl_status = Label(frm_main, text = error)
            lbl_status.place(x=30, y=460)
        return 

    def dateformat(a_date):
        format = '%Y/%m/%d'
        i_date = datetime.strptime(a_date, format)
        year, week_num, day_of_week = i_date.isocalendar()
        lbl_week = Week(year, week_num)
        lbl_start = lbl_week.monday()
        lbl_end = lbl_week.sunday()
        date_range = f'From: {lbl_start} to {lbl_end} week: {week_num}'
        lbl_status = Label(frm_main, text = 'Date is correct                                  ')  
        lbl_status.place(x=30, y=460)
        datelabel = Label(frm_main, text = date_range)
        datelabel.place(x=360, y=35)
        if len(m_week) == 0:
            for i in range(rows):
                m_week.append(week_num)
        return 
    def submit():
        """Create the file with the employee, week and hours reported"""
        matrix = []
        for i in range(rows):
            matrix.append([])
            for j in range(cols):
                matrix[i].append(text_var[i][j].get())
        dict = {"employee": m_employee, "week": m_week, "concept": workconcept,
                        "data": matrix}
        print(f'{len(m_employee)} {len(m_week)} {len(workconcept)} {len(matrix)}')
        df = pd.DataFrame(dict)
        df.to_csv('timereport.csv')
        frm_main.destroy()
        pass

    def clear():
            """Clear the date & messages"""
            ent_employee.delete(0, tk.END)
            ent_date.delete(0, tk.END)
            lbl_employee_name = Label(frm_main, text = '                                                                        ')
            datelabel = Label(frm_main, text = '                                                                        ')
            datelabel.place(x=360, y=35)
            lbl_status = Label(frm_main, text = '                                                                       ')
            lbl_status.place(x=30, y=460)
            lbl_employee_name.place(x=20, y=460)
            m_employee = []
            m_week = []
            text_var.append([])
            entries.append([])
            ent_employee.focus()

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_create.config(command=create)
    btn_submit.config(command=submit)
    btn_clear.config(command=clear)
    ent_employee.focus()
    pass

# Verify the date input
def verifydate(a_date):
    try:
        format = '%Y/%m/%d'
        i_date = datetime.strptime(a_date, format)   
        error = '' 
    except ValueError:
        error = 'Date error'
    return error


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
