import sqlite3
import interface

conn = sqlite3.connect('pfcs.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

##Defines the class Item
class Player(object):

    def __init__(self, idnum):
        self.id = idnum
        self.name = "No Name"
        self.lvl = "0"
        self.clss = "No Class"
        self.race = "No Race"

    def __str__(self):
        return "\n----------\n" + self.name + "\n A level " + self.lvl + " "+self.race+" "+self.clss+"\n ID #: "+str(self.id)+"\n----------"

    def new_char(self):
        self.name =str(input("What is your new character's name?\n"))
        t = (self.id, self.name)
        c.execute("INSERT INTO characters VALUES (?,?)", t)
        c.execute("CREATE TABLE PC"+str(self.id)+" (name, race, class, level)")
        print("Table created for PC"+str(self.id)+": "+self.name+"!")
        self.lvl =str(input("What level is your new character?\n"))
        self.clss =str(input("What class is your new character?\n"))
        self.race =str(input("What race is your new character?\n"))
        tttt = (self.name, self.race, self.clss, self.lvl)
        c.execute("INSERT INTO PC"+str(self.id)+" VALUES (?,?,?,?)", tttt)
        conn.commit()

    def newCharForm(self):
        newChar = interface.TestApp()
        newChar.run()
        self.name = newChar.getName()
        self.lvl = newChar.getLevel()
        self.race = newChar.getRace()
        self.clss = newChar.getClass()
        t = (self.id, self.name)
        c.execute("INSERT INTO characters VALUES (?,?)", t)
        c.execute("CREATE TABLE PC"+str(self.id)+" (name, race, class, level)")
        print("Table created for PC"+str(self.id)+": "+self.name+"!")
        tttt = (self.name, self.race, self.clss, self.lvl)
        c.execute("INSERT INTO PC"+str(self.id)+" VALUES (?,?,?,?)", tttt)
        conn.commit()

    def load_char(self):
        t = (self.id,)
        c.execute('SELECT * FROM characters WHERE charid = ?', t)
        ch = c.fetchone()
        # Should not be more than one, but add in error checking.
        self.name = ch[1]
        c.execute("SELECT * FROM PC"+str(self.id)+"")
        ch = c.fetchone()
        self.race = str(ch[1])
        self.clss = str(ch[2])
        self.lvl = str(ch[3])

    def check_db(self):
        c.execute("SELECT * FROM PC"+str(self.id)+"")
        ch = c.fetchone()
        print("Name: "+self.name)
        print("ID #: "+str(self.id))
        print("Race: "+self.race)
        print("Class: "+self.clss)
        print("Level: "+self.lvl)

    def set_attr(self, attr, x):
        strg = 20
        dex = 16
        con = 11
        intl = 13
        wis = 15
        cha = 12
        t = (self.id,strg,dex,con,intl,wis,cha)
        c.execute("INSERT INTO attributes VALUES (?,?,?,?,?,?,?)", t)
        conn.commit()

    def print_attr(self):
        t = (self.id,)
        c.execute("SELECT * FROM attributes WHERE charid = ?", t)
        r = c.fetchone()
        for i in r:
            if i == self.id:
                print(self.name+"'s Attributes: \n----------")
            else:
                print(" "+str(i))

    def get_name(self):
        return self.name

# Stranded functions, need to be updated
