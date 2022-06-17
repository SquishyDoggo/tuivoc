"""XML Dictionary Parser

This script scans all dictionaries present in the project and parses 
them.

The script can be imported as a module and contains the functions:
    
    * list_dicts - returns a list of dictionaries
    * get_voc - returns vocabulary of one dictionary
"""

import os
from bs4 import BeautifulSoup as bs

def list_dicts():
    """Lists all dictionary files of the project

    Returns
    -------
    list_dicts
        a list of strings of the dictionary file names
    """

    os.chdir('..')
    path = os.getcwd()+'/Dicts'
    l_dicts = os.listdir(path)
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
    """

    vocs = []

    path = os.getcwd()+'/Dicts'
    with open(path+'/'+dict_file,'r',encoding='utf-8') as file:
        data = file.read()
    soup = bs(data,'xml')

    tags_en = soup.find_all('german')
    tags_ja = soup.find_all('japanese')
    text_en = []
    text_ja = []
    for i in range(0,len(tags_en)):
        en = tags_en[i].text.replace('\n','')
        en = en.replace('\t','')
        ja = tags_ja[i].text.replace('\n','')
        ja = ja.replace('\t','')
        text_en.append(en)
        text_ja.append(ja)
        
    vocs.append(text_ja)
    vocs.append(text_en)
    return vocs
