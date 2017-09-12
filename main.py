# -*- coding: utf-8 -*-
# !C:/Program Files (x86)/Python 3.5/python.exe

from tkinter import *
from tkinter import filedialog
import re
import sqlite3


def open_database():
    '''This function will be used to open a database.'''
    database = filedialog.askopenfile(initialdir='C:/', title='Select Database', filetypes=(("db files", "*.db"), ("all files", "*.*")))
    return(database)


def atoms():
    '''
    this function defines the maximum number of atoms to choose
    for each element
    '''
    i = 0
    number_of_atoms = []
    while i <= 100:
        number_of_atoms.append(str(i))
        i += 1
    return(number_of_atoms)


def sum_formula():  # prints all values of buttons that are digits
    pattern = r"[1-9]+"  # regex for one or more digits
    for item in button_list:
        if re.match(pattern, button_list[item].get()):
            print(item + ' : ' + button_list[item].get())
        else:
            pass


# 'XX' entries yield empty spaces in periodic table
element_list = [
                'H', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'He',
                'Li', 'Be', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'B', 'C', 'N', 'O', 'F', 'Ne',
                'Na', 'Mg', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
                'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
                'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe',
                'Cs', 'Ba', 'XX', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',
                'Fr', 'Ra', 'XX', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX',
                'XX', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'XX', 'XX',
                'XX', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'XX', 'XX', 'XX'
                ]


def ElementButton(frame, element, x, y):
    '''
    This function defines the buttons. Every element has its own button.
    atoms function defines how many atoms of that element can be selected.
    '''
    variable = StringVar(window)
    variable.set(element)  # default value
    # l = Label()
    w = OptionMenu(frame, variable, *atoms())
    # das * ist notwendig, damit die Funktion funzt
    w.config(width=2, height=1, borderwidth=1, highlightbackground='ghost white', background='LightSteelBlue2',
            relief=RIDGE, font=('Arial', 12))
    # relief types: flat, groove, raised, ridge, solid, or sunken
    w.grid(column=x, row=y)
    # print(variable.get())
    return(variable)


def periodictable(frame):
    # button grid and creation of dictionary with key-value pairs for
    # elements and atoms
    button_list = {}  # this needs to become a dictionary to get the element
    # symbol for the button value!
    x = 1
    y = 1
    i = 0
    for a in element_list:
        if a != 'XX':
            button_list.update({a: ElementButton(frame, a, x, y)})
            i += 1
        if x == 18:
            y += 1
            x = 1
        else:
            x += 1
    return(button_list)


def OpenButton(frame):
    w = Button(frame, text='Open \n Database', command=open_database)
    w.grid(column=0, row=11, columnspan=2)
    # w.config(width=10, height=2)


def SearchButton(frame):
    w = Button(frame, text='Search', command=search)
    w.grid(column=8, row=11, columnspan=2)
    w.config(width=12, height=2)


def AddButton(frame):
    w = Button(frame, text='Add Compound', command=add)
    w.grid(column=10, row=11, columnspan=2)
    w.config(width=12, height=2)


def BackButton(frame):
    w = Button(frame, text='Back', command=back)
    w.grid(column=2, row=11, columnspan=2)
    w.config(width=12, height=2)


def search():
    ''' This function takes all numerical element button values and submits
    an SQL query to the database.
    '''
    pattern = r"[1-9]+"  # regex for one or more digits
    formatted_values = ("id, Name, lab, in_use_by, missing")
    # enter column names for values to be selected by SQL
    formatted_query = str('')
    for value in button_list:
        # button needs to be dictionary like and will come from tkinter gui
        # if the value of a button is a digit it will be added to the sql query
        if re.match(pattern, button_list[value].get()):
            formatted_query = str(formatted_query + ' AND ' + value + '=\'' + str(button_list[value].get())+'\'')
        else:
            pass
    # the first 'AND' needs to be sliced off
    formatted_query = formatted_query[5:]
    print(formatted_query)
    # execution of SQL query___________________________________________
    connection = sqlite3.connect("Chemikalienliste.db")
    cursor = connection.cursor()
    query = r'''SELECT * FROM 'Chemikalien' WHERE {0};
    '''.format(formatted_query)
    print(query)
    cursor.execute(query)  # Befehl ausführen
    results = cursor.fetchall()
    connection.commit()  # Befehl abschicken
    # Listbox containing query results
    w = Listbox(window, selectmode=SINGLE)
    w.grid(row=10, columnspan=28)  # position on window grid
    w.config(width=135, font=('TkFixedFont'))
    # print('results window:',results)
    w.insert(END, "{:^80}|{:^10}|{:^6}|{:^6}|{:^10}|{:^10}".format('Name', 'Lab', 'g', 'ml', 'in use by', 'missing'))
    try:
        for entry in results:
            if entry[-2] == 'None':
                nutzung = '-'
            else:
                nutzung = entry[24]
            if entry[-3] == 'FALSCH':
                vermisst = '-'
            else:
                vermisst = '+'
            w.insert(END, "{:80}|{:^10}|{:^6}|{:^6}|{:^10}|{:^10}".format(entry[1], entry[-4], entry[3], entry[4], nutzung, vermisst))
    except:
        pass
    return(results)


def add_compound():
    pass


def add():
    addframe.tkraise()


def back():
    searchframe.tkraise()


# GENERAL WORKFLOW

# general window details
# window is where all Frames go
window = Tk()
window.title('ChemDB')
window.minsize(500, 300)
window.config(bg='ghost white')


# FRAME LAYOUTS
searchframe = Frame(window)
searchframe.grid(column=0, row=0, sticky="nsew")
searchframe.config(bg='ghost white')
SearchButton(searchframe)
AddButton(searchframe)
button_list = periodictable(searchframe)
OpenButton(searchframe)


addframe = Frame(window)
addframe.config(bg="DeepSkyBlue2")
addframe.grid(column=0, row=0, sticky="nsew")
BackButton(addframe)
button_list_add = periodictable(addframe)


searchframe.tkraise()  # make searchframe the first to be seen


window.mainloop()
