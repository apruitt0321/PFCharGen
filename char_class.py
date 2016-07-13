import sqlite3

conn = sqlite3.connect('example.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

#Defines the class Item
class Player(object):
    
    def __init__(self, name):
        t = (name,)
        c.execute('SELECT * FROM characters WHERE charname=?', t)
        ch = c.fetchone()
        self.name = str(ch[0])
        self.lvl = str(ch[3])
        self.clss = str(ch[2])
        self.race = str(ch[1])
    
    def __str__(self):
        return "\n----------\n Character Name: " + self.name + "\n Character Race: " + self.race + "\n Character Class: " + self.clss + "\n Character Level: " + self.lvl + "\n----------"
    
    #def change_name(self, new_name):
     #   self.name = new_name
    
    #def add_one(self):
     #   self.count = self.count + 1
    
    #def set_total(self, total):
     #   self.count = total
    
    #def remove_one(self):
     #   self.count = self.count - 1
    
   # def change_loc(self, new_loc):
    #    self.loc = new_loc
    
    def get_name(self):
        return self.name
    
    #def get_count(self):
     #   return self.count
    
    #def get_loc(self):
