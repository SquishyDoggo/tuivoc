"""Generates title screen

This script generates the screen that appears when the program is first
started.

The script can be imported as a module and contains the functions:

    * mk_start_win - generate the title screen
"""

import curses
from time import sleep

def mk_start_win(title='TUIVOC: Your friendly neighborhood vocabulary trainer'):
    """Generate the title screen appearing on startup

    Parameters
    ----------
    title : str 
        Optional argument setting the title screen text
    """

    x = curses.COLS
    y = curses.LINES
    (lh,lw) = (3,len(title)+2)
    w_logo = curses.newwin(lh,lw,y//2-lh//2,x//2-lw//2)
    w_logo.box()
    w_logo.addstr(1,1,title)
    w_logo.refresh()
    w_logo.getch()
    w_logo.clear()
    w_logo.refresh()
