from utils.kana2rom import hiragana2rom
import os
import sys

mozc_dict_dir = sys.argv[1]

def convert_file(filename):
    temp_word = ''
    prev_word = ''
    temp_kana = ''
    prev_kana = ''
    with open(filename, 'r') as f:
        for line in f:
            data = line.split('\t')
            # does not print duplicate entries
            temp_word = data[4].strip('\n')
            temp_kana = data[0]
            if temp_word != prev_word or temp_kana != prev_kana:
                prev_word = temp_word
                prev_kana = temp_kana
                print(temp_word + '\t' + hiragana2rom(temp_kana, style = 'hepburn'))

def main():
    for filename in sorted(os.listdir(mozc_dict_dir)):
        if filename[:10] == 'dictionary':
            convert_file(mozc_dict_dir + '/' + filename)

if __name__ == '__main__':
    main()
