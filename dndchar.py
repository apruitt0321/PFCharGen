# An automated character sheet for Pathfinder. Goals include automatic fill-in for stats, roll generation,
# and automatic class-specific skill attribution.

import sqlite3
import testClasses
import npyscreen

conn = sqlite3.connect('pfcs.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()
char_count = 1

# Checks if a spell list table is already available.
def check_spell_table():
    try:
        c.execute("CREATE TABLE spells (spellname, spelleffect, range, duration)")
        conn.commit()
        return True
    except:
        return False

def check_attr_table():
    try:
        c.execute("CREATE TABLE attributes (charid, strg, dex, con, intl, wis, cha)")
        conn.commit()
        return True
    except:
        return False

# Checks if a character list table is already available.
def check_char_table():
    try:
        c.execute("CREATE TABLE characters (charid, charname)")
        conn.commit()
        return True
    except:
        return False

# Debugging condition for spell list.
def spell_table_init():
    if check_spell_table() == False:
        print("Spell list table already created!")
    else:
        print("Created spell list table!")

def attr_table_init():
    if check_attr_table() == False:
        print("Attribute table already created!")
    else:
        print("Created attribute table!")

# Debugging condition for character list.
def char_table_init():
    global char_count
    if check_char_table() == False:
        print("Character list table already created!")
        c.execute("SELECT * FROM characters")
        r = c.fetchall()
        for i in r:
            char_count += 1
        print("There are currently %i characters saved." % (char_count-1))
    else:
        print("Created new character list table!")

# Function to add a new character to the table of characters.
def new_char():
    print("Would you like to generate a new character or record an already-created character?")
    while True:
        inpt = input("Enter 'g' to generate a new character, or 'r' to record one: ")
        if inpt == 'r':
            rec_new_char()
            break
        elif inpt == 'g':
            rec_new_char()
            break
        else:
            print("That is not valid input.")

def rec_new_char():
    plch = testClasses.Player(char_count)
    plch.new_char()

def gen_new_char():
    plch = testClasses.Player(char_count)
    plch.new_char()

# Function to add a new spell.
def new_spell():
    spnm = str(input("What is the name of the new spell?\n"))
    spdis = str(input("What does the spell do?\n"))
    sprng = str(input("What is the range of the spell?\n"))
    spdur = str(input("What is the spell duration?\n"))
    sptup = (spnm, spdis, sprng, spdur)
    c.execute("INSERT INTO spells VALUES (?,?,?,?)", sptup)
    conn.commit()

# Function to select a character to view.
def view_char():
    view_char_list()
    m = input("Please enter the number of the character you would like to view: ")
    try:
        plch = testClasses.Player(int(m))
        plch.load_char()
        print(plch.__str__())
    except:
        print("That is not a valid input.")

# Function to view a list of all characters currently in the database.
def view_char_list():
    print("")
    c.execute("SELECT * FROM characters")
    r = c.fetchall()
    for i in r:
        print(str(i[0])+". "+i[1])

# Function to select a spell to view.
def view_spell():
    m = input("What is the range of the spells you want to view?\n")
    t = (m,)
    c.execute('SELECT * FROM spells WHERE range=?', t)
    r = c.fetchall()
    for i in r:
        print("\n----------")
        for x in i:
            print(x)
        print("----------\n")

# Function to roll dice
def roll_dice(self,x,y):
    i = 0
    s = []
    while i < x:
        s.append(random.randint(1,y))
        i += 1
    return s
