from utils.kana2rom import hiragana2rom
from utils.hiragana_katakana import katakana2hiragana
from lxml import etree
import sys

jmdict = sys.argv[1]
tree = etree.parse(jmdict)
final_list = []

def to_rom(str):
    return hiragana2rom(katakana2hiragana(str), style = 'hepburn')

for entry in tree.xpath('/JMdict/entry'):
    k_list = []
    r_list = []

    for k_ele in entry.xpath('k_ele'):
        keb_text = k_ele.xpath('keb')[0].text
        k_list.append({'keb_text': keb_text})

    for r_ele in entry.xpath('r_ele'):
        reb_text = r_ele.xpath('reb')[0].text
        re_restr_text_list = []
        re_pri_text_list = []
        for re_restr in r_ele.xpath('re_restr'):
            re_restr_text_list.append(re_restr.text)
        for re_pri in r_ele.xpath('re_pri'):
                re_pri_text_list.append(re_pri.text)
        r_list.append({'reb_text': reb_text, 're_restr_text_list': re_restr_text_list, 're_pri_text_list': re_pri_text_list})

    for r in r_list:
        reb_text = r['reb_text']
        re_restr_text_list = r['re_restr_text_list']
        if '・' in reb_text:
            # suppress middot in romanized word
            final_list.append({'word': reb_text, 'roman': to_rom(reb_text.replace('・', ''))})
        else:
            if r['re_restr_text_list']:
                for k in k_list:
                    if k['keb_text'] in re_restr_text_list:
                        final_list.append({'word': k['keb_text'], 'roman': to_rom(reb_text)})
            else:
                for k in k_list:
                    final_list.append({'word': k['keb_text'], 'roman': to_rom(reb_text)})
            if (not k_list) or r['re_pri_text_list']:
                final_list.append({'word': reb_text, 'roman': to_rom(reb_text)})

for item in final_list:
    print(item['word'], item['roman'], sep = '\t')
