from lxml import etree
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
tree = etree.parse(dir_path + '/' + 'hepburn.xml')

gojuuon = {}
small_forms = {}
youon = {}

for entry_elem in tree.xpath('//gojuuon/entry'):
    kana = (entry_elem.xpath('kana'))[0].text
    roman = (entry_elem.xpath('roman'))[0].text
    prefix = (entry_elem.xpath('prefix'))[0].text
    gojuuon.update({kana: {'roman': roman, 'prefix': prefix}})

for entry_elem in tree.xpath('//small_forms/entry'):
    kana = (entry_elem.xpath('kana'))[0].text
    roman = (entry_elem.xpath('roman'))[0].text
    small_forms.update({kana: {'roman': roman}})

for entry_elem in tree.xpath('//youon/entry'):
    kana = (entry_elem.xpath('kana'))[0].text
    roman = (entry_elem.xpath('roman'))[0].text
    prefix = (entry_elem.xpath('prefix'))[0].text
    youon.update({kana: {'roman': roman, 'prefix': prefix}})

# if __name__ == '__main__':
#     print(gojuuon)
