import curses
import parsing
import list_voc
import logo
import menu
import dictionaries
import settings

dicts = parsing.list_dicts()
voc = parsing.get_voc(dicts[0])

stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)

logo.mk_start_win()
qt = ''
while qt != 'quit':
    curses.curs_set(0)
    qt = menu.make_menu(stdscr,curses.LINES//2,curses.COLS//2)
    if qt == 'start':
        curses.curs_set(1)
        curses.echo()
        list_voc.display_voc(voc,disp_type=0)
    elif qt == 'dictionaries':
        dictionaries.make_dicts(dicts) 
    elif qt == 'settings':
        settings.make_settings()

curses.endwin()


