# Currently only supports conversion from hiragana -> Hepburn-like romanization.
# All おう transliterated -> "ou";
# All は, へ and を -> "ha", "he" and "wo" respectively.
# Could have other bugs.

import hepburn_data

def hiragana2hepburn(str):
    result = ''
    curr_prefix = ''
    curr_roman = ''
    flag_skip = False
    for i in reversed(range(len(str))):
        curr_char = str[i]
        if flag_skip:
            flag_skip = False
        else:
            if curr_char == 'っ':
                    curr_roman = curr_prefix if curr_prefix else 't'
            else:
                curr_prefix = ''
                if curr_char in hepburn_data.gojuuon:
                    curr_roman = hepburn_data.gojuuon[curr_char]['roman']
                    curr_prefix = hepburn_data.gojuuon[curr_char]['prefix']
                elif curr_char == 'ー':
                    curr_roman = '-'
                elif curr_char in hepburn_data.small_forms:
                    if i == 0 or ((str[i - 1] + curr_char) not in hepburn_data.youon):
                        curr_roman = hepburn_data.small_forms[curr_char]['roman']
                    else:
                        curr_roman = hepburn_data.youon[str[i - 1] + curr_char]['roman']
                        curr_prefix = hepburn_data.youon[str[i - 1] + curr_char]['prefix']
                        flag_skip = True
                else:
                    curr_roman = curr_char
            result = curr_roman + result
    return result

if __name__ == '__main__':
    print(hiragana2hepburn('うぉーるなっと'))
    print(hiragana2hepburn('おっぱい'))
    print(hiragana2hepburn('いっしょ'))
