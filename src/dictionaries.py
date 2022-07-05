import curses
import menu
import xml.etree.ElementTree as ET
import os
from parsing import list_dicts

dir_path = os.path.dirname(os.path.dirname(__file__))
cur_path = os.path.curdir

def make_dicts(dict_list):
    w_dicts = curses.newwin(curses.LINES,curses.COLS,0,0)
    (y,x) = w_dicts.getmaxyx()
    options = ['select','delete']
    option = '0'

    def make_dict_options(chosen_dict):
        w_opts = curses.newwin(curses.LINES,curses.COLS,0,0)
        user_option = menu.make_menu(w_opts,y//2,x//2,menu_entries=options)
        w_opts.refresh()
        w_opts.clear()
        if user_option == options[1]:
            os.remove(dir_path+'/dicts/'+chosen_dict)
        return user_option


    while option != options[0]:
        chosen_dict = menu.make_menu(w_dicts,y//2,x//2,menu_entries=dict_list)
        if chosen_dict == 'new':
            break
        else:
            option = make_dict_options(chosen_dict)
            dict_list = list_dicts()
    w_dicts.refresh()
    w_dicts.clear()

    return chosen_dict


def make_new_dict():
    queries = ['dictionary name','german note','german word','japanese note','japanese furigana','japanese word','to quit press q']
    off = 2
    i = 1
    w_new_dict = curses.newwin(curses.LINES,curses.COLS,0,0)
    (y,x) = w_new_dict.getmaxyx()

    def get_input(query_idx):
        if query_idx != 0:
            w_new_dict.addstr(y//4,x//2-len(queries[query_idx])//2,str(i)+'. vocabulary')
        w_new_dict.addstr(y//2,x//2-len(queries[query_idx])//2,queries[query_idx])
        w_new_dict.refresh()
        user_input = w_new_dict.getstr(y//2+off,x//2-len(queries[query_idx])//2).decode(encoding='utf-8')
        w_new_dict.clear()
        return user_input

    dict_name = get_input(0)
    root = ET.Element('dictionary')
    user_quit = ''
    while user_quit != ord('q'):
        voc = ET.SubElement(root,'vocabulary',id=str(i))
        # german word
        g_word = '0'
        while g_word != '':
            g_word = get_input(2)
            if g_word == '':
                break
            else:
                # german note
                g_note = get_input(1)
                ger = ET.SubElement(voc,'german',note=g_note)

                ET.SubElement(ger,'word').text = g_word

        # japanese word
        j_word = '0'
        while j_word != '':
            # japanese word
            j_word = get_input(5)
            if j_word == '':
                break
            else:
                # japanese note
                j_note = get_input(3)
                ja = ET.SubElement(voc,'japanese',note=j_note)
                # japanese furigana
                j_furi = get_input(4)

                ET.SubElement(ja,'word',furigana=j_furi).text = j_word
        i += 1
        w_new_dict.addstr(y//2,x//2-len(queries[6])//2,queries[6])
        user_quit = w_new_dict.getch()
        w_new_dict.clear()

    tree = ET.ElementTree(root)
    tree.write(dict_name)

    # move new dictionary file to dictionary folder
    os.rename(cur_path+'/'+dict_name,dir_path+'/dicts/'+dict_name)

