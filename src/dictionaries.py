import curses
import menu
import xml.etree.ElementTree as ET
import os
import parsing

def make_dicts(dict_list):
    w_dicts = curses.newwin(curses.LINES,curses.COLS,0,0)
    (y,x) = w_dicts.getmaxyx()
    chosen_dict = menu.make_menu(w_dicts,y//2,x//2,menu_entries=dict_list)
    w_dicts.refresh()
    w_dicts.clear()
    return chosen_dict

def make_new_dict():
    w_new_dict = curses.newwin(curses.LINES,curses.COLS,0,0)
    (y,x) = w_new_dict.getmaxyx()
    queries = ['dictionary name','german note','german word','japanese note','japanese furigana','japanese word','to quit press q']
    off = 2
    w_new_dict.addstr(y//2,x//2-len(queries[0])//2,queries[0])
    w_new_dict.refresh()
    dict_name = w_new_dict.getstr(y//2+off,x//2-len(queries[0])//2).decode(encoding='utf-8')
    w_new_dict.clear()
    root = ET.Element('dictionary')
    user_quit = ''
    i = 1
    while user_quit != ord('q'):
        voc = ET.SubElement(root,'vocabulary',id=str(i))
        # german note
        w_new_dict.addstr(y//2,x//2-len(queries[1])//2,queries[1])
        w_new_dict.refresh()
        g_note = w_new_dict.getstr(y//2+off,x//2-len(queries[1])//2).decode(encoding='utf-8')
        w_new_dict.clear()
        ger = ET.SubElement(voc,'german',note=g_note)
        # german word
        g_word = '0'
        while g_word != '':
            w_new_dict.addstr(y//2,x//2-len(queries[2])//2,queries[2])
            w_new_dict.refresh()
            g_word = w_new_dict.getstr(y//2+off,x//2-len(queries[2])//2).decode(encoding='utf-8')
            w_new_dict.clear()
            if g_word == '':
                break
            else:
                ET.SubElement(ger,'word').text = g_word

        # japanese note
        w_new_dict.addstr(y//2,x//2-len(queries[3])//2,queries[3])
        w_new_dict.refresh()
        j_note = w_new_dict.getstr(y//2+off,x//2-len(queries[3])//2).decode(encoding='utf-8')
        w_new_dict.clear()
        ja = ET.SubElement(voc,'japanese',note=j_note)
        # japanese word
        j_word = '0'
        while j_word != '':
            # japanese furigana
            w_new_dict.addstr(y//2,x//2-len(queries[4])//2,queries[4])
            w_new_dict.refresh()
            j_furi = w_new_dict.getstr(y//2+off,x//2-len(queries[4])//2).decode(encoding='utf-8')
            w_new_dict.clear()
            # japanese word
            w_new_dict.addstr(y//2,x//2-len(queries[5])//2,queries[5])
            w_new_dict.refresh()
            j_word = w_new_dict.getstr(y//2+off,x//2-len(queries[5])//2).decode(encoding='utf-8')
            w_new_dict.clear()
            if j_word == '':
                break
            else:
                ET.SubElement(ja,'word',furigana=j_furi).text = j_word
        i += 1
        w_new_dict.addstr(y//2,x//2-len(queries[6])//2,queries[6])
        user_quit = w_new_dict.getch()
        w_new_dict.clear()

    tree = ET.ElementTree(root)
    tree.write(dict_name)

    # move new dictionary file to dictionary folder
    dir_path = os.path.dirname(os.path.dirname(__file__))
    cur_path = os.path.curdir
    os.rename(cur_path+'/'+dict_name,dir_path+'/dicts/'+dict_name)

