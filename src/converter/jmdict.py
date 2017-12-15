from utils.kana2rom import hiragana2rom
from utils.hiragana_katakana import katakana2hiragana #, has_katakana
from lxml import etree
import sys

# def gen_freq(pri_list):
#     result = 0

jmdict = sys.argv[1]
tree = etree.parse(jmdict)
final_list = []

for entry in tree.xpath('/JMdict/entry'):
    k_list = []
    r_list = []

    if entry.xpath('k_ele'):
        for k_ele in entry.xpath('k_ele'):
            keb_text = k_ele.xpath('keb')[0].text
            # ke_pri_list = []
            # if k_ele.xpath('ke_pri'):
            #     for ke_pri in k_ele.xpath('ke_pri'):
            #             ke_pri_list.append(ke_pri.text)
            # k_list.append({'keb_text': keb_text, 'ke_pri_list': ke_pri_list})
            k_list.append({'keb_text': keb_text})

    for r_ele in entry.xpath('r_ele'):
        reb_text = r_ele.xpath('reb')[0].text
        re_restr_list = []
        re_pri_list = []
        if r_ele.xpath('re_restr'):
            for re_restr in r_ele.xpath('re_restr'):
                re_restr_list.append(re_restr.text)
        if r_ele.xpath('re_pri'):
            for re_pri in r_ele.xpath('re_pri'):
                    re_pri_list.append(re_pri.text)
        r_list.append({'reb_text': reb_text, 're_restr_list': re_restr_list, 're_pri_list': re_pri_list})

    for r in r_list:
        reb_text = r['reb_text']
        re_restr_list = r['re_restr_list']
        if '・' in reb_text:
            # suppress middot in romanized word
            final_list.append({'word': reb_text, 'roman': hiragana2rom(katakana2hiragana(reb_text.replace('・', '')), style = 'hepburn')})
        else:
            if r['re_restr_list']:
                for k in k_list:
                    if k['keb_text'] in re_restr_list:
                        final_list.append({'word': k['keb_text'], 'roman': hiragana2rom(katakana2hiragana(reb_text), style = 'hepburn')})
            else:
                for k in k_list:
                    final_list.append({'word': k['keb_text'], 'roman': hiragana2rom(katakana2hiragana(reb_text), style = 'hepburn')})
            if (not k_list) or r['re_pri_list']:
                final_list.append({'word': reb_text, 'roman': hiragana2rom(katakana2hiragana(reb_text), style = 'hepburn')})

for item in final_list:
    print(item['word'], item['roman'], sep = '\t')
