from utils.romanization_data import hepburn
from utils.hiragana_katakana import hiragana2katakana

x = hepburn

def small_forms(func):
    for item in x.small_forms:
        print(func(item), x.small_forms[item]['roman'], sep = '\t')
    print('')

def gojuuon(func):
    for item in x.gojuuon:
        print(func(item), x.gojuuon[item]['roman'], sep = '\t')
    print('')

def youon(func):
    for item in x.youon:
        print(func(item), x.youon[item]['roman'], sep = '\t')
    print('')

def sokuon(func):
    for item in x.gojuuon:
        prefix = x.gojuuon[item]['prefix']
        if prefix:
            print(func('っ' + item),  prefix + x.gojuuon[item]['roman'], sep = '\t')
    print('')

def youon_with_sokuon(func):
    for item in x.youon:
        prefix = x.youon[item]['prefix']
        if prefix:
            print(func('っ' + item),  prefix + x.youon[item]['roman'], sep = '\t')
    print('')

def print_both(f):
    f(lambda x: x)
    f(hiragana2katakana)

print('# Small forms')
print_both(small_forms)
print('# Gojuuon 五十音')
print_both(gojuuon)
print('# Youon 拗音')
print_both(youon)
print('# Sokuon 促音')
print_both(sokuon)
print('# Youon with sokuon')
print_both(youon_with_sokuon)
