"""XML Dictionary Parser

This script scans all dictionaries present in the project and parses 
them.

The script can be imported as a module and contains the functions:
    
    * list_dicts - returns a list of dictionaries
    * get_voc - returns vocabulary of one dictionary
"""

import os
from bs4 import BeautifulSoup as bs


path = os.path.dirname(os.path.dirname(__file__))+'/dicts'

def list_dicts():
    """Lists all dictionary files of the project

    Returns
    -------
    list_dicts
        a list of strings of the dictionary file names
    """

    l_dicts = os.listdir(path)
    l_dicts.append('new')
    return l_dicts

def get_voc(dict_file):
    """Parses vocabulary in given dictionary file

    Parameters
    ----------
    dict_file : str
        The dictionary file name

    Returns
    -------
    vocs
        A list of lists containing the vocabulary, translations, notes, etc.
        e.g. [ [[ja,ja,ja],ja,ja], [en,[en,en],en], [[furi,furi,furi],furi,furi] ]
    """

    vocs = []

    with open(path+'/'+dict_file,'r',encoding='utf-8') as file:
        data = file.read()
    soup = bs(data,'xml')

    tags_en = soup.find_all('german')
    tags_ja = soup.find_all('japanese')
    text_en = []
    text_ja = []
    text_furi = []
    for i in range(0,len(tags_en)):
        en_words = tags_en[i].find_all('word')
        ja_words = tags_ja[i].find_all('word')
        if ( len(en_words) ==1 ):
            text_en.append(en_words[0].text.replace('\t','').replace('\n',''))
        else:
            en_word_list = []
            for j in range(0,len(en_words)):
                en_word = en_words[j].text.replace('\t','').replace('\n','')
                en_word_list.append(en_word)
            text_en.append(en_word_list)
        if ( len(ja_words) == 1 ):
           text_ja.append(ja_words[0].text.replace('\t','').replace('\n',''))
           text_furi.append(ja_words[0]['furigana'])
        else:
            ja_word_list = []
            for j in range(0,len(ja_words)):
                ja_word = ja_words[j].text.replace('\t','').replace('\n','')
                ja_word_list.append(ja_word)
            text_ja.append(ja_word_list)
    vocs.append(text_ja)
    vocs.append(text_en)
    vocs.append(text_furi)
    return vocs
