import curses

def make_settings():
    settings = curses.newwin(curses.LINES-1,curses.COLS-1,0,0)
    settings.addstr(0,0,'under construction')
    settings.getch()
    settings.clear()
    settings.refresh()
