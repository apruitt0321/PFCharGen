import curses

#Begin curses interface
def stui():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)
    return stdscr

def say_something():
    s = stui()
#   try:
    s.border(0)
    ypos = 2
    s.addstr(ypos,2,"Press any key!")
    s.refresh()
    t = s.getkey()
    while t != 'q':
        #s.erase()
        #s.border(0)
        ypos += 1
        kp = "You pressed "+t+"! Ypos is currently:"+str(ypos)+"... "
        s.addstr(ypos,2,kp)
        s.refresh()
        t = s.getkey()
#   except:
    endui(s)

# End curses interface
def endui(s):
    stdscr = s
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()

say_something()
