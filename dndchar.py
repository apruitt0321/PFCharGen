# An automated character sheet for Pathfinder. Goals include automatic fill-in for stats, roll generation,
# and automatic class-specific skill attribution.


import sqlite3
conn = sqlite3.connect('example.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()
#c.execute("INSERT INTO spells VALUES ('Magic Missle', 'Kills enemy dead', '30ft', 'Instant')")
#conn.commit()

def check_table():
    try:
        c.execute("CREATE TABLE spells (spellname, spelleffect, range, duration)")
        return False
    except:
        return True

if check_table() == True:
    print "Hello World!"
else:
    print "Something went wrong!"

t = ('30ft',)
c.execute('SELECT * FROM spells WHERE range=?', t)
r = c.fetchone()

print r[0]

#for i in r:
 #   print i

