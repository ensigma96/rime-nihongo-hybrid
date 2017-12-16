from utils.hiragana_katakana import katakana2hiragana
from utils.hiragana_katakana import has_katakana

def main():
    print(katakana2hiragana('ファ 0 ぱ'))
    print(has_katakana('あほ 1'))
    print(has_katakana('アホ 1'))
    print(has_katakana('棒をシリアナに'))

if __name__ == '__main__':
    main()
