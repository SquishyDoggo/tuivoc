import curses

def make_dicts(dict_list):
    dicts = curses.newwin(curses.LINES,curses.COLS,0,0)
    for i in range(0,len(dict_list)):
        dicts.addstr(i,0,dict_list[i])
    dicts.getch()
    dicts.refresh()
    dicts.clear()

