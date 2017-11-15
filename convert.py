# Currently only supports conversion from hiragana -> Hepburn-like romanization.
# All おう transliterated -> "ou";
# All は, へ and を -> "ha", "he" and "wo" respectively.
# Could have other bugs.

import hepburn

def kana2hepburn(str):
    result = ''
    curr_prefix = ''
    curr_roman = ''
    flag_skip = False
    char_list = list(str)
    for i in reversed(range(len(char_list))):
        if flag_skip:
            flag_skip = False
        else:
            if char_list[i] == 'っ':
                    curr_roman = curr_prefix if curr_prefix else 't'
            else:
                curr_prefix = ''
                if char_list[i] in hepburn.gojuuon:
                    curr_roman = hepburn.gojuuon[char_list[i]]['roman']
                    curr_prefix = hepburn.gojuuon[char_list[i]]['prefix']
                elif char_list[i] == 'ー':
                    curr_roman = '-'
                elif char_list[i] in hepburn.small_forms:
                    if i == 0 or ((char_list[i - 1] + char_list[i]) not in hepburn.youon):
                        curr_roman = hepburn.small_forms[char_list[i]]['roman']
                    else:
                        curr_roman = hepburn.youon[char_list[i - 1] + char_list[i]]['roman']
                        curr_prefix = hepburn.gojuuon[char_list[i - 1]]['prefix']
                        flag_skip = True
                else:
                    curr_roman = char_list[i]
            result = curr_roman + result
    return result

if __name__ == '__main__':
    print(kana2hepburn('うぉーるなっと'))
    print(kana2hepburn('おっぱい'))
    print(kana2hepburn('いっしょ'))
