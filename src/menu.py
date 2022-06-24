import curses

def make_menu(window,y,x,menu_entries=['start','dictionaries','settings','quit']):
    curses.noecho()
    y_spacing = 3
    y -= (len(menu_entries)*y_spacing-1)//2
    x -= len(max(menu_entries))//2

    def update_menu_text(idx):
        window.clear()
        for i in range(0,len(menu_entries)):
            if (i == idx):
                window.addstr(y+i*y_spacing,x,menu_entries[i],curses.A_BOLD)
            else:
                window.addstr(y+i*y_spacing,x,menu_entries[i])
        window.refresh()

    def navigate_menu():
        cur_idx = 0
        max_idx = len(menu_entries)-1
        update_menu_text(cur_idx)
        user_input = 0
        while user_input != 10:
            user_input = window.getch()
            if (user_input == ord('j')) and (cur_idx < max_idx):
                cur_idx += 1
                update_menu_text(cur_idx)
            elif (user_input == ord('j')) and (cur_idx >= max_idx):
                cur_idx = 0
                update_menu_text(cur_idx)
            elif (user_input == ord('k')) and (cur_idx > 0):
                cur_idx -= 1
                update_menu_text(cur_idx)
            elif (user_input == ord('k')) and (cur_idx <= 0):
                cur_idx = max_idx
                update_menu_text(cur_idx)
        
        window.clear()
        window.refresh()
        return menu_entries[cur_idx]

    return navigate_menu()
