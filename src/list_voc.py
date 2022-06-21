"""Curses TUI for querying vocabulary

This script displays all the vocabulary in a dictionary and
queries the user for the translation. To be called the curses
screen needs to be initialized.

The script can be imported as a module and contains the functions:

    * display_voc - displays vocabulary and queries user for translation
"""

import curses

def display_voc(vocs,disp_type=0):
    """Display vocabulary of one dictionary sequentially and query user 
    their translation.

    Parameters
    ----------
    vocs
        A list containing all vocabulary in one dictionary
    disp_type : int 
        Optional variable defining query type. It defaults to 0 where
        english vocabulary is displayed and the translation is requested
        by the user.

    """
    w_voc_disp = curses.newwin(5,curses.COLS//3,curses.LINES//3,curses.COLS//3)
    w_voc_resp = curses.newwin(2,curses.COLS//3,curses.LINES//2,curses.COLS//3)
    (y,x) = w_voc_disp.getmaxyx()
    
    if (disp_type == 0):
        ja = vocs[0]
        en = vocs[1]
    else:
        ja = vocs[1]
        en = vocs[0]
    
    for i in range(0,len(en)):
        if (not isinstance(en[i],list)):
            x_pos_text = x//2-len(en[i])//2

            w_voc_disp.addstr(1,x_pos_text,en[i])
            w_voc_disp.refresh()

            user_resp = w_voc_resp.getstr(1,x_pos_text).decode(encoding='utf-8')
            if (user_resp != ja[i]):
                w_voc_disp.addstr(2,x_pos_text,'X:'+ja[i])
            else:
                w_voc_disp.addstr(2,x_pos_text,'O')
        else:
            concat_word_en = ''
            for j in range(0,len(en[i])):
                if (j == len(en[i])-1):
                    concat_word_en += en[i][j]
                else: 
                    concat_word_en += en[i][j]+';'
            x_pos_text = x//2-len(concat_word_en)//2
            w_voc_disp.addstr(1,x_pos_text,concat_word_en)
            w_voc_disp.refresh()

            user_resp = w_voc_resp.getstr(1,x_pos_text).decode(encoding='utf-8')
            if not (isinstance(ja[i],list)):
                if (user_resp != ja[i]):
                    w_voc_disp.addstr(2,x_pos_text,'X:'+ja[i])
                else:
                    w_voc_disp.addstr(2,x_pos_text,'O')
            else:
                concat_word_ja = ''
                for k in range(0,len(ja[i])):
                    if (k == len(ja[i])-1):
                        concat_word_ja += ja[i][k]
                    else:
                        concat_word_ja += ja[i][k]+';'

                if (user_resp in ja[i]):
                    w_voc_disp.addstr(2,x_pos_text,'O')
                else:
                    w_voc_disp.addstr(2,x_pos_text,'X:'+concat_word_ja)

        w_voc_disp.refresh()
        w_voc_disp.getch()
        w_voc_disp.clear()
        w_voc_resp.clear()
