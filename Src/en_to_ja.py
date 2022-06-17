import curses
from time import sleep

def mk_start_win(name):
    x = curses.COLS
    y = curses.LINES
    for cpy in range(0,y//2):
        title = curses.newwin(3,len(name),cpy,x//2-len(name)//2)
        title.box()
        title.addstr(1,0,name)
        title.refresh()
        sleep(2e-2)

def main():
    mk_start_win("Cursary: Your Friendly Neighborhood Voc Trainer")
    stdscr.getch()
