from utils.kana2rom import hiragana2rom
import unittest

class MyTest(unittest.TestCase):
    def test_basics(self):
        self.assertEqual(hiragana2rom('あいうえお', style = 'hepburn'), 'aiueo')
        self.assertEqual(hiragana2rom('いろはにほへとちりぬるを', style = 'hepburn'), 'irohanihohetochirinuruwo')
    def test_sokuon(self):
        self.assertEqual(hiragana2rom('まって', style = 'hepburn'), 'matte')
        self.assertEqual(hiragana2rom('べっど', style = 'hepburn'), 'beddo')
        self.assertEqual(hiragana2rom('いっしょ', style = 'hepburn'), 'issho')
        self.assertEqual(hiragana2rom('あっっっ', style = 'hepburn'), 'attt')
        self.assertEqual(hiragana2rom('あっっふぁ', style = 'hepburn'), 'afffa')
    def test_small_form(self):
        self.assertEqual(hiragana2rom('あゕ', style = 'hepburn'), 'a_ka')
    def test_non_kana(self):
        self.assertEqual(hiragana2rom('その他', style = 'hepburn'), 'sono他')
    def test_mixed(self):
        self.assertEqual(hiragana2rom('うぉーるなっと', style = 'hepburn'), 'who-runatto')

if __name__ == '__main__':
    unittest.main()
