# Currently only supports conversion from hiragana -> Hepburn-like romanization.
# All おう transliterated -> "ou";
# All は, へ and を -> "ha", "he" and "wo" respectively.
# Could have other bugs.

def kana2hepburn(str):
    gojuuon = {
        'あ': {'roman': 'a', 'prefix': ''}, 'い': {'roman': 'i', 'prefix': ''}, 'う': {'roman': 'u', 'prefix': ''}, 'え': {'roman': 'e', 'prefix': ''}, 'お': {'roman': 'o', 'prefix': ''},
        'ゔ': {'roman': 'vu', 'prefix': 'v'},
        'か': {'roman': 'ka', 'prefix': 'k'}, 'き': {'roman': 'ki', 'prefix': 'k'}, 'く': {'roman': 'ku', 'prefix': 'k'}, 'け': {'roman': 'ke', 'prefix': 'k'}, 'こ': {'roman': 'ko', 'prefix': 'k'},
        'が': {'roman': 'ga', 'prefix': 'g'}, 'ぎ': {'roman': 'gi', 'prefix': 'g'}, 'ぐ': {'roman': 'gu', 'prefix': 'g'}, 'げ': {'roman': 'ge', 'prefix': 'g'}, 'ご': {'roman': 'go', 'prefix': 'g'},
        'さ': {'roman': 'sa', 'prefix': 's'}, 'し': {'roman': 'shi', 'prefix': 's'}, 'す': {'roman': 'su', 'prefix': 's'}, 'せ': {'roman': 'se', 'prefix': 's'}, 'そ': {'roman': 'so', 'prefix': 's'},
        'ざ': {'roman': 'za', 'prefix': 'z'}, 'じ': {'roman': 'ji', 'prefix': 'j'}, 'ず': {'roman': 'zu', 'prefix': 'z'}, 'ぜ': {'roman': 'ze', 'prefix': 'z'}, 'ぞ': {'roman': 'zo', 'prefix': 'z'},
        'た': {'roman': 'ta', 'prefix': 't'}, 'ち': {'roman': 'chi', 'prefix': 't'}, 'つ': {'roman': 'tsu', 'prefix': 't'}, 'て': {'roman': 'te', 'prefix': 't'}, 'と': {'roman': 'to', 'prefix': 't'},
        'だ': {'roman': 'da', 'prefix': 'd'}, 'ぢ': {'roman': 'ji', 'prefix': 'j'}, 'づ': {'roman': 'zu', 'prefix': 'z'}, 'で': {'roman': 'de', 'prefix': 'd'}, 'ど': {'roman': 'do', 'prefix': 'd'},
        'な': {'roman': 'na', 'prefix': ''}, 'に': {'roman': 'ni', 'prefix': ''}, 'ぬ': {'roman': 'nu', 'prefix': ''}, 'ね': {'roman': 'ne', 'prefix': ''}, 'の': {'roman': 'no', 'prefix': ''},
        'は': {'roman': 'ha', 'prefix': 'h'}, 'ひ': {'roman': 'hi', 'prefix': 'h'}, 'ふ': {'roman': 'fu', 'prefix': 'f'}, 'へ': {'roman': 'he', 'prefix': 'h'}, 'ほ': {'roman': 'ho', 'prefix': 'h'},
        'ば': {'roman': 'ba', 'prefix': 'b'}, 'び': {'roman': 'bi', 'prefix': 'b'}, 'ぶ': {'roman': 'bu', 'prefix': 'b'}, 'べ': {'roman': 'be', 'prefix': 'b'}, 'ぼ': {'roman': 'bo', 'prefix': 'b'},
        'ぱ': {'roman': 'pa', 'prefix': 'p'}, 'ぴ': {'roman': 'pi', 'prefix': 'p'}, 'ぷ': {'roman': 'pu', 'prefix': 'p'}, 'ぺ': {'roman': 'pe', 'prefix': 'p'}, 'ぽ': {'roman': 'po', 'prefix': 'p'},
        'ま': {'roman': 'ma', 'prefix': ''}, 'み': {'roman': 'mi', 'prefix': ''}, 'む': {'roman': 'mu', 'prefix': ''}, 'め': {'roman': 'me', 'prefix': ''}, 'も': {'roman': 'mo', 'prefix': ''},
        'ら': {'roman': 'ra', 'prefix': 'r'}, 'り': {'roman': 'ri', 'prefix': 'r'}, 'る': {'roman': 'ru', 'prefix': 'r'}, 'れ': {'roman': 're', 'prefix': 'r'}, 'ろ': {'roman': 'ro', 'prefix': 'r'},
        'や': {'roman': 'ya', 'prefix': ''}, 'ゆ': {'roman': 'yu', 'prefix': ''}, 'よ': {'roman': 'yo', 'prefix': ''},
        'わ': {'roman': 'wa', 'prefix': ''}, 'ゐ': {'roman': 'wi', 'prefix': ''}, 'ゑ': {'roman': 'we', 'prefix': ''}, 'を': {'roman': 'wo', 'prefix': ''},
        'ん': {'roman': 'n', 'prefix': ''}
    }

    small_forms = {
        'ぁ': {'roman': '_a'},
        'ぃ': {'roman': '_i'},
        'ぅ': {'roman': '_u'},
        'ぇ': {'roman': '_e'},
        'ぉ': {'roman': '_o'},
        'ゃ': {'roman': '_ya'},
        'ゅ': {'roman': '_yu'},
        'ょ': {'roman': '_yo'},
        'ゎ': {'roman': '_wa'},
    }

    youon = {
        # 'いぇ': {'roman': 'ye'},
        'うぁ': {'roman': 'wha'}, 'うぃ': {'roman': 'whi'}, 'うぇ': {'roman': 'whe'}, 'うぉ': {'roman': 'who'},
        'ゔぁ': {'roman': 'va'}, 'ゔぃ': {'roman': 'vi'}, 'ゔぇ': {'roman': 've'}, 'ゔぉ': {'roman': 'vo'}, 'ゔゃ': {'roman': 'vya'}, 'ゔゅ': {'roman': 'vyu'}, 'ゔょ': {'roman': 'vyo'},
        'きゃ': {'roman': 'kya'}, 'きゅ': {'roman': 'kyu'}, 'きょ': {'roman': 'kyo'}, 'くぁ': {'roman': 'kwa'}, 'くぃ': {'roman': 'kwi'}, 'くぇ': {'roman': 'kwe'}, 'くぉ': {'roman': 'kwo'}, 'くゎ': {'roman': 'kwa'},
        'ぎゃ': {'roman': 'gya'}, 'ぎゅ': {'roman': 'gyu'}, 'ぎょ': {'roman': 'gyo'}, 'ぐぁ': {'roman': 'gwa'}, 'ぐぃ': {'roman': 'gwi'}, 'ぐぇ': {'roman': 'gwe'}, 'ぐぉ': {'roman': 'gwo'}, 'ぐゎ': {'roman': 'gwa'},
        'しぇ': {'roman': 'she'}, 'しゃ': {'roman': 'sha'}, 'しゅ': {'roman': 'shu'}, 'しょ': {'roman': 'sho'}, 'すぃ': {'roman': 'si'},
        'じぇ': {'roman': 'je'}, 'じゃ': {'roman': 'ja'}, 'じゅ': {'roman': 'ju'}, 'じょ': {'roman': 'jo'}, 'ずぃ': {'roman': 'zi'},
        'ちぇ': {'roman': 'che'}, 'ちゃ': {'roman': 'cha'}, 'ちゅ': {'roman': 'chu'}, 'ちょ': {'roman': 'cho'}, 'つぁ': {'roman': 'tsa'}, 'つぃ': {'roman': 'tsi'}, 'つぇ': {'roman': 'tse'}, 'つぉ': {'roman': 'tso'}, 'てぃ': {'roman': 'ti'}, 'てゃ': {'roman': 'tya'}, 'てゅ': {'roman': 'tyu'}, 'てょ': {'roman': 'tyo'}, 'とぅ': {'roman': 'tu'},
        'ぢぇ': {'roman': 'je'}, 'ぢゃ': {'roman': 'ja'}, 'ぢゅ': {'roman': 'ju'}, 'ぢょ': {'roman': 'jo'}, 'でぃ': {'roman': 'di'}, 'でゃ': {'roman': 'dya'}, 'でゅ': {'roman': 'dyu'}, 'でょ': {'roman': 'dyo'}, 'どぅ': {'roman': 'du'},
        'にゃ': {'roman': 'nya'}, 'にゅ': {'roman': 'nyu'}, 'にょ': {'roman': 'nyo'},
        'ひゃ': {'roman': 'hya'}, 'ひゅ': {'roman': 'hyu'}, 'ひょ': {'roman': 'hyo'}, 'ふぁ': {'roman': 'fa'}, 'ふぃ': {'roman': 'fi'}, 'ふぇ': {'roman': 'fe'}, 'ふぉ': {'roman': 'fo'}, 'ふゃ': {'roman': 'fya'}, 'ふゅ': {'roman': 'fyu'}, 'ふょ': {'roman': 'fyo'}, 'ほぅ': {'roman': 'hu'},
        'びゃ': {'roman': 'bya'}, 'びゅ': {'roman': 'byu'}, 'びょ': {'roman': 'byo'},
        'ぴゃ': {'roman': 'pya'}, 'ぴゅ': {'roman': 'pyu'}, 'ぴょ': {'roman': 'pyo'},
        'みゃ': {'roman': 'mya'}, 'みゅ': {'roman': 'myu'}, 'みょ': {'roman': 'myo'},
        'りゃ': {'roman': 'rya'}, 'りゅ': {'roman': 'ryu'}, 'りょ': {'roman': 'ryo'},
    }

    result = ''
    curr_prefix = ''
    curr_roman = ''
    flag_skip = False
    char_list = list(str)
    for i in reversed(range(len(char_list))):
        if flag_skip:
            flag_skip = False
            curr_prefix = ''
        else:
            if char_list[i] == 'っ':
                    curr_roman = curr_prefix if curr_prefix else 't'
            else:
                curr_prefix = ''
                if char_list[i] in gojuuon:
                    curr_roman = gojuuon[char_list[i]]['roman']
                    curr_prefix = gojuuon[char_list[i]]['prefix']
                elif char_list[i] == 'ー':
                    curr_roman = '-'
                elif char_list[i] in small_forms:
                    if i == 0 or ((char_list[i - 1] + char_list[i]) not in youon):
                        curr_roman = small_forms[char_list[i]]['roman']
                    else:
                        curr_roman = youon[char_list[i - 1] + char_list[i]]['roman']
                        curr_prefix = gojuuon[char_list[i - 1]]['roman']
                        flag_skip = True
                else:
                    curr_roman = char_list[i]
            result = curr_roman + result
    return result

if __name__ == '__main__':
    print(kana2hepburn('うぉーるなっと'))
    print(kana2hepburn('おっぱい'))
    print(kana2hepburn('いんむ'))
