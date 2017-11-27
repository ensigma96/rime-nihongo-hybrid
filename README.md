# rime-nihongo-hybrid

- 简体中文版指南 [→](https://github.com/ensigma96/rime-nihongo-hybrid/blob/master/README_zh-Hans.md)
- 繁體中文版指南 [→](https://github.com/ensigma96/rime-nihongo-hybrid/blob/master/README_zh-Hant.md)

A Japanese input scheme & dictionary for [RIME](http://rime.im/). The dictionary is converted from [mozc](https://github.com/google/mozc)'s ones. See https://github.com/google/mozc/blob/master/src/data/dictionary_oss/README.txt for license.

## Usage
### 1. Copy the files
Copy everything under `dist/` into Rime's user folder. Example: the user folder is `~/.config/ibus/rime/`, then `cp -vr dist/. ~/.config/ibus/rime/` will do the work.

The location of user directory is related to specific input methods (i.e. frontends of Rime). In most cases, information about it can be found either in Rime's [Customization Guide](https://github.com/rime/home/wiki/CustomizationGuide) or in the documentation of the input method.

### 2. Deploy
Deployment also varies across input methods. Usually, you can also find information in the same place(s) above.

### Note
If your input method is using an ancient version of librime, hence an ancient version (<1.0) of opencc, then the json config may not be supported. This will at least make the `simplifier`'s `jp_variants` option ineffectual.
