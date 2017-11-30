# Currently only supports conversion from hiragana -> Hepburn-like romanization.
# All おう transliterated -> "ou";
# All は, へ and を -> "ha", "he" and "wo" respectively.
# Could have other bugs.

from .romanization_data import hepburn
from warnings import warn

def hiragana2rom(str, style):
    if style == 'hepburn':
        rom = hepburn
    else:
        warn(' No such romanization style, defaulting to hepburn.')
        rom = hepburn
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
                if curr_char in rom.gojuuon:
                    curr_roman = rom.gojuuon[curr_char]['roman']
                    curr_prefix = rom.gojuuon[curr_char]['prefix']
                elif curr_char == 'ー':
                    curr_roman = '-'
                elif curr_char in rom.small_forms:
                    if i == 0 or ((str[i - 1] + curr_char) not in rom.youon):
                        curr_roman = rom.small_forms[curr_char]['roman']
                    else:
                        curr_roman = rom.youon[str[i - 1] + curr_char]['roman']
                        curr_prefix = rom.youon[str[i - 1] + curr_char]['prefix']
                        flag_skip = True
                else:
                    curr_roman = curr_char
            result = curr_roman + result
    return result
