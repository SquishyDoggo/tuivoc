import curses
import parsing
import list_voc

stdscr = curses.initscr()
stdscr.clear()

dicts = parsing.list_dicts()
voc = parsing.get_voc(dicts[0])
list_voc.display_voc(voc)

curses.endwin()


