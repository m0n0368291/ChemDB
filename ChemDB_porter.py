# -*- coding: utf-8 -*-
# !C:\ProgramData\Anaconda3\python.exe

import csv
import sqlite3

GHS_dictionary = {
    'T' : 'GHS06'
    'T+' : 'GHS06'
    'Xn' : 'GHS08'
    'Xi' : 'GHS07'
    'F' : 'GHS02'
    'F+' : 'GHS02'
    'E' : 'GHS01'
    'C' : 'GHS05'
    'N' : 'GHS09'
    'O' : 'GHS03'
    'kA' : 'no_hazard'
                    }


def db2():
    '''
    this function creates a database schema using the GHS system for safety
    hazard declaration. Arsenic and Indium need to be called by their full names,
    to escape SQL syntax.
    '''
    element_list = [
                    'H', 'He',
                    'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
                    'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
                    'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'Arsenic', 'Se', 'Br', 'Kr',
                    'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'Indium', 'Sn', 'Sb', 'Te', 'I', 'Xe',
                    'Cs', 'Ba', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',
                    'Fr', 'Ra', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt',
                    'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu',
                    'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr',
                    'C13', 'D'
                    ]

    chemical_properties_list = [
                                'no_hazard', 'GHS01', 'GHS02', 'GHS03', 'GHS05', 'GHS06', 'GHS07', 'GHS08', 'GHS09',
                                'lab', 'missing', 'in_use_by', 'almost_empty'
                                ]

    sql_list1 = ['{0} INTEGER DEFAULT 0,'.format(i) for i in element_list]
    # list containing all elements in SQL syntax
    sql_list2 = ['{0} TEXT DEFAULT False,'.format(i) for i in chemical_properties_list]
    # list containing all chemical properties in SQL syntax
    db_format = r"""
    CREATE TABLE "Chemikalien" (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                Name TEXT(300),"""
    for i in sql_list1:
        db_format += i.strip("'")
    for i in sql_list2:
        db_format += i.strip("'")
    #print(db_format[:-1]+');')
    connection = sqlite3.connect("Chem.db")
    cursor = connection.cursor()
    cursor.execute(r'PRAGMA encoding = "UTF-8";')
    connection.commit()
    cursor.execute(db_format[:-1]+');')
    connection.commit()
    connection.close()


def porter():
    """
    All apostrophes in the chemicals CVS file have to be escaped
    manually by "searching and replacing" all ' into ''
    Make sure that head and tail of .csv are clean!!
    """
    x = 1  # trigger
    # open old csv file
    with open("alte_liste.csv", 'r') as file:
        contents = csv.reader(file, delimiter=';')
        for line in contents:
            print(len(line), 'items per entry in old database')
            if x == 1:
                connection = sqlite3.connect("Chemikalienliste.db")
                cursor = connection.cursor()
                format_str = """
                INSERT OR IGNORE INTO "Chemikalien" (
                Name, MW, Masse, Vol, H, He, Li, Be, B, C, N,
                O, F, Ne, Na, Mg, Al, Si, P, S, Cl,
                Ar, K, Ca, Sc, Ti, V, Cr, Mn, Fe, Co,
                Ni, Cu, Zn, Ga, Ge, 'As', Se, Br, Kr, Rb,
                Sr, Y, Zr, Nb, Mo, Tc, Ru, Rh, Pd, Ag,
                Cd, 'In', Sn, Sb, Te, I, Xe, Cs, Ba, La,
                Hf, Ta, W, Re, Os, Ir, Pt, Au, Hg, Tl,
                Pb, Bi, Po, At, Rn, Ce, Pr, Nd, Pm, Sm,
                Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, 'no_hazard',
                'explosive', 'oxidizing', 'corrosive', 'toxic', 'toxic+',
                'flammable', 'flammable+', 'irritant',
                'carcinogen', 'environment_hazard','13C', 'D', 'lab')
                VALUES(
                '{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}',
                '{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}','{21}',
                '{22}','{23}','{24}','{25}','{26}','{27}','{28}','{29}','{30}','{31}',
                '{32}','{33}','{34}','{35}','{36}','{37}','{38}','{39}','{40}','{41}',
                '{42}','{43}','{44}','{45}','{46}','{47}','{48}','{49}','{50}','{51}',
                '{52}','{53}','{54}','{55}','{56}','{57}','{58}','{59}','{60}','{61}',
                '{62}','{63}','{64}','{65}','{66}','{67}','{68}','{69}','{70}','{71}',
                '{72}','{73}','{74}','{75}','{76}','{77}','{78}','{79}','{80}','{81}',
                '{82}','{83}','{84}','{85}','{86}','{87}','{88}','{89}','{90}','{91}',
                '{92}','{93}','{94}','{95}','{96}','{97}','{98}','{99}','{100}','{101}','{102}','{103}'
                );
                """.format(line[0], line[107], line[108], line[109], line[3],
                    line[14], line[15], line[16], line[4], line[2], line[5],
                    line[6], [7], line[17], line[18], line[19], line[20],
                    line[8], line[9], [10], line[11], line[21], line[22],
                    line[23], line[24], line[25], [26], line[27], line[28],
                    line[29], line[30], [31], line[32], [33], line[34],
                    line[35], line[36], line[37], line[12], line[38],
                    [39], [40], line[41], line[42], line[43], line[44],
                    line[45], [46], line[47], line[48], line[49], [50],
                    line[51], line[52], [53], line[54], line[13], line[55],
                    line[56], line[57], line[58], [59], line[60], line[61],
                    line[62], line[63], line[64], line[65], [66], line[67],
                    line[68], [69], line[70], line[71], line[72], [73],
                    line[77], line[78], line[79], line[80], line[81], [82],
                    line[83], line[84], line[85], line[86], line[87], line[88],
                    line[89], [90], line[120], [116], line[119], line[117],
                    line[110], [111], line[114], line[115], line[112],
                    line[113], line[118], [106], line[105], line[1])
                print(line[0])
                cursor.execute(format_str)  # Befehl ausführen
                connection.commit()  # Befehl abschicken
    connection.close()  # Verbindung schließen


db2()
# porter()