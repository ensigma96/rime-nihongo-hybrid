# rime-nihongo-hybrid

- 简体中文版指南 [→](https://github.com/ensigma96/rime-nihongo-hybrid/blob/master/README_zh-Hans.md)
- 繁體中文版指南 [→](https://github.com/ensigma96/rime-nihongo-hybrid/blob/master/README_zh-Hant.md)

A Japanese input scheme & dictionary for [RIME](http://rime.im/).

## Usage
### 1. Copy the files
Copy everything under `dist/` into Rime's user folder. Example: the user folder is `~/.config/ibus/rime/`, then `cp -vr dist/. ~/.config/ibus/rime/` will do the work.

The location of user directory is related to specific input methods (i.e. frontends of Rime). In most cases, information about it can be found either in Rime's [Customization Guide](https://github.com/rime/home/wiki/CustomizationGuide) or in the documentation of the input method.

### 2. Deploy
Deployment also varies across input methods. Usually, you can also find information in the same place(s) above.

### Note
If your input method is using an ancient version of librime, hence an ancient version (<1.0) of opencc, then the json config may not be supported. This will at least make the `simplifier`'s `jp_variants` option ineffectual.

## License
* All files other than those under `src/data` and `dist` are released under MIT License.
* Files and folders under `src/data`:
  * `JMdict/JMdict_e.xml` is released by [JMDict Project](http://www.edrdg.org/jmdict/j_jmdict.html) under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license. See http://www.edrdg.org/edrdg/licence.html .
  * Files under `mozc_dictionaries` directory is part of [mozc](https://github.com/google/mozc). For license information, see `README.txt` under the same directory.
  * `opencc/JPVariants.ocd` is part of [OpenCC](https://github.com/BYVoid/OpenCC), which is released under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
  * `internet-jp-forms.num` comes from the [file](http://corpus.leeds.ac.uk/frqc/internet-jp-forms.num), and is used in accordance with [CC BY 2.5](https://creativecommons.org/licenses/by/2.5/) license.
