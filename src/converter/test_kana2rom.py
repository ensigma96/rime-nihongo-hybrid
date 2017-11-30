from utils.kana2rom import hiragana2rom

def main():
    print(hiragana2rom('うぉーるなっと', style = 'hepburn'))
    print(hiragana2rom('おっぱい', style = 'hepburn'))
    print(hiragana2rom('いっしょ', style = 'hepburn'))

if __name__ == '__main__':
    main()
