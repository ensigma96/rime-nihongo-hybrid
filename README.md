# rime-nihongo-hybrid

- 简体中文版指南 [→](https://github.com/ensigma96/rime-nihongo-hybrid/blob/master/README_zh-Hans.md)
- 繁體中文版指南 [→](https://github.com/ensigma96/rime-nihongo-hybrid/blob/master/README_zh-Hant.md)

A Japanese input scheme & dictionary for [RIME](http://rime.im/).

## Usage

### 1\. Copy the files

Copy everything under `dist/` into Rime's user folder. For example: the user folder is `~/.config/ibus/rime/`, then `cp -vr dist/. ~/.config/ibus/rime/` will do the work.

The location of user directory is related to specific input methods (i.e. frontends of Rime). In most cases, information about it can be found either in Rime's [Customization Guide](https://github.com/rime/home/wiki/CustomizationGuide) or in the documentation of the input method.

### 2\. Deploy

Deployment also varies across input methods. Usually, you can also find information in the same place(s) above.

## License

- All files other than those under `third_party/` and `dist/` are released under MIT License.
- Files under `third_party/`:

  - `data/JMdict/JMdict_e.xml`

    - What: The JMdict (Japanese-Multilingual Dictionary) file, with only the English translations.
    - Author: The Electronic Dictionary Research and Development Group
    - Link: <http://www.edrdg.org/jmdict/j_jmdict.html>
    - License: [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/), see [this link](http://www.edrdg.org/edrdg/licence.html) for more information.

  - `data/mozc_dictionaries/*`

    - What: dictionary files of the input method [mozc](https://github.com/google/mozc)
    - Author: multiple authors
    - Link: <https://github.com/google/mozc/tree/master/src/data/dictionary_oss>
    - License: [mixed license](https://github.com/google/mozc/blob/master/src/data/dictionary_oss/README.txt)

  - `data/internet-jp-forms.num`

    - What: a Japanese frequency list
    - Author: Serge Sharoff
    - Link: <http://corpus.leeds.ac.uk/frqc/internet-jp-forms.num>
    - License: [CC BY 2.5](https://creativecommons.org/licenses/by/2.5/)

  - `data/opencc/*`

    - What: [opencc](https://github.com/BYVoid/OpenCC) dictionaries
    - Author: BYVoid
    - Link: <https://github.com/BYVoid/OpenCC/blob/master/data/dictionary/JPVariants.txt>
    - License: Apache License 2.0
