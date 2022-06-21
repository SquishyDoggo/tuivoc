import curses
import parsing
import list_voc
import logo

stdscr = curses.initscr()
stdscr.clear()

logo.mk_start_win()
dicts = parsing.list_dicts()
voc = parsing.get_voc(dicts[0])
list_voc.display_voc(voc,disp_type=0)

curses.endwin()


