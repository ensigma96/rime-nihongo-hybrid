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
* All files other than those under `src/data` are released under MIT License.
* `src/data/JMdict/JMdict_e.xml` comes from [JMdict](http://www.edrdg.org/jmdict/j_jmdict.html) project, and is released under CC BY-SA 3.0 license. See http://www.edrdg.org/edrdg/licence.html for more information.
  `dist/nihongo-hybrid.dict/nihongo-hybrid.jmdict.dict.yaml` is generated from the file(s) above.
* `src/data/mozc_dictionaries` comes from [mozc](https://github.com/google/mozc). See `src/data/mozc_dictionaries/README.txt` for license.
  `dist/nihongo-hybrid.dict/nihongo-hybrid.mozc.dict.yaml` is generated from the file(s) above.
* `src/data/opencc/JPVariants.ocd` comes from [OpenCC](https://github.com/BYVoid/OpenCC) .
  `dist/opencc/JPVariants.ocd` is the same file as above.
