from lxml import etree
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
tree = etree.parse(dir_path + '/' + 'hiragana_katakana.xml')
tups = []
for entry_elem in tree.xpath('//entry'):
    tups.append((entry_elem.xpath('hiragana')[0].text, entry_elem.xpath('katakana')[0].text))

def katakana2hiragana_c(char):
    for tup in tups:
        if (char == tup[1]):
            return tup[0]
    return char

def hiragana2katakana_c(char):
    for tup in tups:
        if (char == tup[0]):
            return tup[1]
    return char

def katakana2hiragana(str):
    result = ''
    for char in str:
        result += katakana2hiragana_c(char)
    return result

def hiragana2katakana(str):
    result = ''
    for char in str:
        result += hiragana2katakana_c(char)
    return result
