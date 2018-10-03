import curses
import npyscreen

class tA(npyscreen.NPSAppManaged):
    def onStart(self):
        #s = "Welcome to PF Character Sheet!"
        #ss = "New Character"
        self.addForm('AddChar', Addchar)
        self.addForm('MAIN', CharSheetIntro, name='Welcome!')

class Addchar(npyscreen.Form):
    def afterEditing(self):
        self.parentApp.setNextFormPrevious()

    def create(self):
        self.charName  = self.add(npyscreen.TitleText, name = "Name:")
        self.lvl = self.add(npyscreen.TitleText, name = "Level:")
        self.rc = self.add(npyscreen.TitleText, name = "Race:")
        clsses = ["Druid","Bard","Rogue","Wizard","Fighter"]
        self.clss = self.add(npyscreen.TitleSelectOne, value = [0,], name="Pick A Class:", values = clsses, scroll_exit=True)

    def getName(self):
        return self.charName.value

    def getRace(self):
        return self.rc.value

    def getClass(self):
        return self.clss.values[self.clss.value[0]]

    def getLevel(self):
        return self.lvl.value

class CharSheetIntro(npyscreen.Form):
    def create(self):
        self.choices = ["Add a new character", "View a list of characters", "View a specific character", "Exit"]
        self.choose = self.add(npyscreen.TitleSelectOne, value = [0,], name="What would you like to do?", values = self.choices, scroll_exit=True)
        #add this back into self.clss before value = if it doesn't work: max_height=6

    def afterEditing(self):
        opt = self.choose.value[0]
        if opt == 0:
            self.parentApp.setNextForm('AddChar')
        else:
            self.parentApp.setNextForm(None)

#Begin curses interface

def stui():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)
    return stdscr

def rsstui(s):
    curses.noecho()
    curses.cbreak()
    s.keypad(1)
    s.clear()
    s.border(0)
    s.refresh()

def say_something():
    App = TestApp()
    s = stui()
    s.border(0)
    ypos = 2
    s.addstr(ypos,2,"Press any key!")
    s.refresh()
    t = s.getkey()
    try:
        while t != 'q':
            if t == 'p':
                App.run()
                rsstui(s)
                ypos = 2
            kp = "You pressed "+t+"! Ypos is currently: "+str(ypos)+"... "
            s.addstr(ypos,2,kp)
            s.refresh()
            ypos += 1
            t = s.getkey()
    finally:
        endui(s)

# End curses interface
def endui(s):
    stdscr = s
    stdscr.clear()
    stdscr.refresh()
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()

#say_something()
