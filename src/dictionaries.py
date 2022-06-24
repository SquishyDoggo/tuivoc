import curses
import menu

def make_dicts(dict_list):
    w_dicts = curses.newwin(curses.LINES,curses.COLS,0,0)
    (y,x) = w_dicts.getmaxyx()
    chosen_dict = menu.make_menu(w_dicts,y//2,x//2,menu_entries=dict_list)
    w_dicts.refresh()
    w_dicts.clear()
    return chosen_dict

