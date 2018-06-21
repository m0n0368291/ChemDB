# -*- coding: utf-8 -*-
# !C:/Program Files (x86)/Python 3.5/python.exe

from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import sqlite3

# Windows and frames layout
window = Tk()
window.title('ChemDB')
window.minsize(500, 300)
window.config(bg='ghost white')

searchframe = Frame(window)
searchframe.grid(column=0, row=0, sticky="nsew")
#searchframe.config(bg='ghost white')

addframe = Frame(window)
#addframe.config(bg="DeepSkyBlue2")
addframe.grid(column=0, row=0, sticky="nsew")


def config():
    '''
    Tries to open an existing 'chemdb.config' file in the same directory as
    'main.py'. If found, uses assigned database location in Client.search()
    method. Otherwise a new config is created. Also an "unknown" user is
    registered. Manually entering user credentials might become necessary at a
    later development stage. Also the format of the config file is pretty dumb,
    but i have no elegant way of parsing it yet.
    '''
    try:
        print('trying to open existing chemdb.config')
        with open('chemdb.config', 'r+') as configfile:
            database = configfile.readline().split(";")
            database = database[1].strip('"')
            print('using database at:',database[1:])
            return(database[1:])
    except FileNotFoundError:
        print('File not found! Opening new database.')
        database = filedialog.askopenfile(initialdir='C:/', title='Select \
                                          Database', filetypes=(("db files",
                                          "*.db"), ("all files", "*.*")))
        with open('chemdb.config', 'w') as configfile:
            configuration = 'database ; '+ database.name + ';\nuser ; unknown;'
            configfile.write(configuration)
            print('new chemdb.config created!')
        return(database.name)


class Client():

    def __init__(self, query=None, results=None):
        self.results = results
        self.query = query

    def search(self):
        ''' Creates an SQL query as a string
        '''
        formatted_values = ("id, Name, lab, in_use_by, missing")
        formatted_query = str('')
        for value in button_list:
            # button needs to be dictionary like and will come from tkinter gui
            # if the value of a button is a digit between 1-100 it will be added to the sql query
            if not button_list[value].get() == '':
                formatted_query = str(formatted_query + ' AND ' + value + '=\''
                                      + str(button_list[value].get())+'\'')
        # the first 'AND' needs to be sliced off
        formatted_query = formatted_query[5:]
        self.query = r"SELECT * FROM 'Chemikalien' WHERE {0};".format(formatted_query)
        print(self.query)
        return(self.query)


    def execute_query(self):
        ''' Takes an SQL query as a string and commits it to the database
        '''
        connection = sqlite3.connect(database.get())
        cursor = connection.cursor()
        print(self.query)
        cursor.execute(self.query)  # Befehl ausführen klappt nicht!!!! query is Object, not string
        self.results = cursor.fetchall()
        connection.commit()  # Befehl abschicken
        print(self.results)
        return(self.results)

    def listbox(self):
        entries = StringVar(value=self.results)
        # Listbox containing query results
        lbox = Listbox(window, selectmode=SINGLE)
        lbox.grid(row=10, columnspan=28)  # position on window grid
        lbox.config(width=135, font=('TkFixedFont'))
        lbox.insert(END, "{:^80}|{:^10}|{:^6}|{:^6}|{:^10}|{:^10}".format('Name', 'Lab', 'g', 'ml', 'in use by', 'missing'))
        try:
            for entry in self.results:
                if entry[-2] == 'None':
                    nutzung = '-'
                else:
                    nutzung = entry[24]
                if entry[-3] == 'FALSCH':
                    vermisst = '-'
                else:
                    vermisst = '+'
                lbox.insert(END, "{:80}|{:^10}|{:^6}|{:^6}|{:^10}|{:^10}".format(entry[1], entry[-4], entry[3], entry[4], nutzung, vermisst))
        except:
            pass


    def add(self):
        pass


# 'XX' entries yield empty spaces in periodic table
# Indium and Arsenic still messing up the query!!!
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


def ElementEntry(frame, element, x, y):
    '''
    This function defines the buttons. Every element has its own button. It
    can either be an Entry Widget or an OptionMenu.
    '''
    variable = StringVar(window)
    variable.set(element)  # default value, substitutes 'zero'
    e = Entry(frame, textvariable=variable, width=9, justify=CENTER)
    e.grid(column=x, row=y)
    e.delete(0,END)
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
            element_label = Label(frame, text=a)
            element_label.grid(column=x, row=y)
            button_list.update({a: ElementEntry(frame, a, x, y+1)})
            i += 1
        if x == 18:
            y += 2
            x = 1
        else:
            x += 1
    return(button_list)


def AddButton(frame):
    w = Button(frame, text='Add \nCompound', command=add)
    w.grid(column=10, row=20, columnspan=3, rowspan=3)
    #w.config(width=12, height=2)


def BackButton(frame):
    w = Button(frame, text='Back', command=back)
    w.grid(column=2, row=20, columnspan=2)
    #w.config(width=12, height=2)


def add():
    addframe.tkraise()


def back():
    searchframe.tkraise()


session = Client()

button_list = periodictable(searchframe)  # dictionary with button elements and values

database = StringVar()  # database location variable for search method of session class
database.set(config())  # look for config file and create one if necessary

def full_search():
    session.search()
    session.execute_query()
    session.listbox()

def SearchButton(frame):
    w = Button(frame, text='Search', command=full_search)
    w.grid(column=7, row=20, columnspan=3)
    #w.config(width=12, height=2)


# Widgets for all frames
SearchButton(searchframe)
AddButton(searchframe)

#OpenButton(searchframe)

BackButton(addframe)
button_list_add = periodictable(addframe)  # dictionary with button elements and values



searchframe.tkraise()  # make searchframe the first to be seen



window.mainloop()