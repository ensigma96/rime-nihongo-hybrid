import hepburn_data
import kana_form_conv

def small_forms(func):
    for item in hepburn_data.small_forms:
        print(func(item), hepburn_data.small_forms[item]['roman'], sep = '\t')
    print('')

def gojuuon(func):
    for item in hepburn_data.gojuuon:
        print(func(item), hepburn_data.gojuuon[item]['roman'], sep = '\t')
    print('')

def youon(func):
    for item in hepburn_data.youon:
        print(func(item), hepburn_data.youon[item]['roman'], sep = '\t')
    print('')

def sokuon(func):
    for item in hepburn_data.gojuuon:
        prefix = hepburn_data.gojuuon[item]['prefix']
        if prefix:
            print(func('っ' + item),  prefix + hepburn_data.gojuuon[item]['roman'], sep = '\t')
    print('')

def youon_with_sokuon(func):
    for item in hepburn_data.youon:
        prefix = hepburn_data.youon[item]['prefix']
        if prefix:
            print(func('っ' + item),  prefix + hepburn_data.youon[item]['roman'], sep = '\t')
    print('')

def print_both(f):
    f(lambda x: x)
    f(kana_form_conv.hiragana2katakana)

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
