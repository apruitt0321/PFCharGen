# An automated character sheet for Pathfinder. Goals include automatic fill-in for stats, roll generation,
# and automatic class-specific skill attribution.

import sqlite3
conn = sqlite3.connect('example.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

# Checks if a spell list table is already available.
def check_spell_table():
    try:
        c.execute("CREATE TABLE spells (spellname, spelleffect, range, duration)")
        #c.execute("INSERT INTO spells VALUES ('Magic Missle', 'Kills enemy dead', '30ft', 'Instant')")
        conn.commit()
        return True
    except:
        return False

# Checks if a character list table is already available.
def check_char_table():
    try:
        c.execute("CREATE TABLE characters (name, level, class, race)")
        conn.commit()
        return True
    except:
        return False

# Debugging condition for spell list.
if check_spell_table() == False:
    print "Spell list table already created!"
else:
    print "Created spell list table!"

# Debugging condition for character list.
if check_char_table() == False:
    print "Character list table already created!"
else:
    print "Created character list table!"

# Function to add a new character to the table of characters
def new_char():
    nm = str(raw_input("What is the name of your new character?\n"))
    lvl = str(raw_input("What level is your new character?\n"))
    cls = str(raw_input("What class is your new character?\n"))
    rc = str(raw_input("What race is your new character?\n"))
    c.execute("INSERT INTO characters VALUES ('nm', 'lvl', 'cls', 'rc')")
    conn.commit()

char_run = True

while char_run:
    print "Hello and Welcome!\n"
    print "What would you like to do?\n"
    print "Enter 'q' to quit."
    print "Enter 'a' to add a new character."
    print "Enter 'v' to view all characters."
    usrinpt = raw_input("Please enter a command: ")
    if usrinpt == 'q':
        char_run = False
    elif usrinpt == 'a':
        new_char()
    elif usrinpt == 'v':
        # Does not display information correctly. 
        t = ('1',)
        c.execute('SELECT * FROM characters WHERE level=?', t)
        #r = c.fetchone()
        r= c.fetchall()
        #print r[0]
        for i in r:
            print i
    else:
        print "Sorry, that is not valid input."
    #debugging prompt
    print "\n----End of loop----\n"

