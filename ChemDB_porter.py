# -*- coding: utf-8 -*-
#!C:/Program Files (x86)/Python 2.7/python.exe

import sys
import os
import datetime # Umwandlung von Datum in Wochentag
import glob   #zum öffnen mehrerer files
import csv # comma separated value
import sqlite3 #sqlite3 database support
from os import remove

def create_database():
    connection = sqlite3.connect("Chemikalienliste.db")
    cursor = connection.cursor()
    db_format =r"""
    CREATE TABLE "Chemikalien" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT(300),
    MW INTEGER DEFAULT 0,
    Masse INTEGER DEFAULT 0,
    Vol INTEGER DEFAULT 0,
    H INTEGER DEFAULT 0,
    He INTEGER DEFAULT 0,
    Li INTEGER DEFAULT 0,
    Be INTEGER DEFAULT 0,
    B INTEGER DEFAULT 0,
    C INTEGER DEFAULT 0,
    N INTEGER DEFAULT 0,
    O INTEGER DEFAULT 0,
    F INTEGER DEFAULT 0,
    Ne INTEGER DEFAULT 0,
    Na INTEGER DEFAULT 0,
    Mg INTEGER DEFAULT 0,
    Al INTEGER DEFAULT 0,
    Si INTEGER DEFAULT 0,
    P INTEGER DEFAULT 0,
    S INTEGER DEFAULT 0,
    Cl INTEGER DEFAULT 0,
    Ar INTEGER DEFAULT 0,
    K INTEGER DEFAULT 0,
    Ca INTEGER DEFAULT 0,
    Sc INTEGER DEFAULT 0,
    Ti INTEGER DEFAULT 0,
    V INTEGER DEFAULT 0,
    Cr INTEGER DEFAULT 0,
    Mn INTEGER DEFAULT 0,
    Fe INTEGER DEFAULT 0,
    Co INTEGER DEFAULT 0,
    Ni INTEGER DEFAULT 0,
    Cu INTEGER DEFAULT 0,
    Zn INTEGER DEFAULT 0,
    Ga INTEGER DEFAULT 0,
    Ge INTEGER DEFAULT 0,
    'As' INTEGER DEFAULT 0,
    Se INTEGER DEFAULT 0,
    Br INTEGER DEFAULT 0,
    Kr INTEGER DEFAULT 0,
    Rb INTEGER DEFAULT 0,
    Sr INTEGER DEFAULT 0,
    Y INTEGER DEFAULT 0,
    Zr INTEGER DEFAULT 0,
    Nb INTEGER DEFAULT 0,
    Mo INTEGER DEFAULT 0,
    Tc INTEGER DEFAULT 0,
    Ru INTEGER DEFAULT 0,
    Rh INTEGER DEFAULT 0,
    Pd INTEGER DEFAULT 0,
    Ag INTEGER DEFAULT 0,
    Cd INTEGER DEFAULT 0,
    'In' INTEGER DEFAULT 0,
    Sn INTEGER DEFAULT 0,
    Sb INTEGER DEFAULT 0,
    Te INTEGER DEFAULT 0,
    I INTEGER DEFAULT 0,
    Xe INTEGER DEFAULT 0,
    Cs INTEGER DEFAULT 0,
    Ba INTEGER DEFAULT 0,
    La INTEGER DEFAULT 0,
    Hf INTEGER DEFAULT 0,
    Ta INTEGER DEFAULT 0,
    W INTEGER DEFAULT 0,
    Re INTEGER DEFAULT 0,
    Os INTEGER DEFAULT 0,
    Ir INTEGER DEFAULT 0,
    Pt INTEGER DEFAULT 0,
    Au INTEGER DEFAULT 0,
    Hg INTEGER DEFAULT 0,
    Tl INTEGER DEFAULT 0,
    Pb INTEGER DEFAULT 0,
    Bi INTEGER DEFAULT 0,
    Po INTEGER DEFAULT 0,
    At INTEGER DEFAULT 0,
    Rn INTEGER DEFAULT 0,
    Ce INTEGER DEFAULT 0,
    Pr INTEGER DEFAULT 0,
    Nd INTEGER DEFAULT 0,
    Pm INTEGER DEFAULT 0,
    Sm INTEGER DEFAULT 0,
    Eu INTEGER DEFAULT 0,
    Gd INTEGER DEFAULT 0,
    Tb INTEGER DEFAULT 0,
    Dy INTEGER DEFAULT 0,
    Ho INTEGER DEFAULT 0,
    Er INTEGER DEFAULT 0,
    Tm INTEGER DEFAULT 0,
    Yb INTEGER DEFAULT 0,
    Lu INTEGER DEFAULT 0,
    'no_hazard' TEXT DEFAULT FALSCH,
    'explosive' TEXT DEFAULT FALSCH,
    'oxidizing' TEXT DEFAULT FALSCH,
    'corrosive' TEXT DEFAULT FALSCH,
    'toxic' TEXT DEFAULT FALSCH,
    'toxic+' TEXT DEFAULT FALSCH,
    'flammable' TEXT DEFAULT FALSCH,
    'flammable+' TEXT DEFAULT FALSCH,
    'irritant' TEXT DEFAULT FALSCH,
    'carcinogen' TEXT DEFAULT FALSCH,
    'environment_hazard' TEXT DEFAULT FALSCH,
    '13C' INTEGER DEFAULT FALSCH,
    'D' INTEGER DEFAULT FALSCH,
    'lab' TEXT,
    'missing' TEXT DEFAULT FALSCH,
    'in_use_by' TEXT DEFAULT None,
    'almost_empty' TEXT DEFAULT FALSCH);
    """
    cursor.execute(r'PRAGMA encoding = "UTF-8";')
    connection.commit()
    cursor.execute(db_format)#Befehl ausführen
    connection.commit()#Befehl abschicken
    connection.close()#Verbindung schließen



def porter():
    """
    All apostrophes in the chemicals CVS file have to be escaped
    manually by "searching and replacing" all ' into ''
    Make sure that head and tail of .csv are clean!!
    """
    x = 1 #trigger
    #open old csv file
    with open("alte_liste.csv", 'r') as file:
        contents = csv.reader(file, delimiter=';')
        for line in contents:
            print(len(line),'items per entry in old database')
            if x==1:
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
                'explosive', 'oxidizing', 'corrosive', 'toxic', 'toxic+', 'flammable', 'flammable+', 'irritant',
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
                """.format(line[0],line[107],line[108],line[109],line[3],line[14],line[15],line[16],line[4],line[2],line[5],
                line[6],line[7],line[17],line[18],line[19],line[20],line[8],line[9],line[10],line[11],
                line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],
                line[31],line[32],line[33],line[34],line[35],line[36],line[37],line[12],line[38],line[39],
                line[40],line[41],line[42],line[43],line[44],line[45],line[46],line[47],line[48],line[49],
                line[50],line[51],line[52],line[53],line[54],line[13],line[55],line[56],line[57],line[58],
                line[59],line[60],line[61],line[62],line[63],line[64],line[65],line[66],line[67],line[68],
                line[69],line[70],line[71],line[72],line[73],line[77],line[78],line[79],line[80],line[81],
                line[82],line[83],line[84],line[85],line[86],line[87],line[88],line[89],line[90],line[120],
                line[116],line[119],line[117],line[110],line[111],line[114],line[115],line[112],line[113],line[118],line[106],line[105],line[1])
                print(line[0])
                cursor.execute(format_str)#Befehl ausführen
                connection.commit()#Befehl abschicken
    connection.close()#Verbindung schließen


create_database()
porter()
