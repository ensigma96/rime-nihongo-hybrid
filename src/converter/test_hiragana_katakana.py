from utils.hiragana_katakana import katakana2hiragana, hiragana2katakana
import unittest

class MyTest(unittest.TestCase):
    def test_katakana2hiragana(self):
        self.assertEqual(katakana2hiragana('サクラ'), 'さくら')
    def test_hiragana2katakana(self):
        self.assertEqual(hiragana2katakana('さくら'), 'サクラ')

if __name__ == '__main__':
    unittest.main()
