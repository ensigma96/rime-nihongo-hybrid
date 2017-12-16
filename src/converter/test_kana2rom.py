from utils.kana2rom import hiragana2rom

def main():
    print(hiragana2rom('うぉーるなっと', style = 'hepburn'))
    print(hiragana2rom('おっぱい', style = 'hepburn'))
    print(hiragana2rom('いっしょ', style = 'hepburn'))
    print(hiragana2rom('いっしょ'))
    print(hiragana2rom('いっしょ', style = 'aaa'))

if __name__ == '__main__':
    main()
