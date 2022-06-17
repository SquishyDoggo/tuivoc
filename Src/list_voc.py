import curses

def display_voc(vocs):
    w_voc_disp = curses.newwin(5,curses.COLS//3,curses.LINES//3,curses.COLS//3)
    w_voc_resp = curses.newwin(2,curses.COLS//3,curses.LINES//2,curses.COLS//3)
    (y,x) = w_voc_disp.getmaxyx()
    
    ja = vocs[0]
    en = vocs[1]
    
    for i in range(0,len(en)):
        x_pos_text = x//2-len(en[i])//2

        w_voc_disp.addstr(1,x_pos_text,en[i])
        w_voc_disp.refresh()

        user_resp = w_voc_resp.getstr(1,x_pos_text).decode(encoding='utf-8')
        if (user_resp != ja[i]):
            w_voc_disp.addstr(2,x_pos_text,'X:'+ja[i])
            w_voc_disp.refresh()
        else:
            w_voc_disp.addstr(2,x_pos_text,'O')

        w_voc_disp.getch()
        w_voc_disp.clear()
        w_voc_resp.clear()
