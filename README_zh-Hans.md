# rime-nihongo-hybrid
[RIME](http://rime.im/) 日语输入方案及词库。

## 使用方法
### 一、复制文件
将 `dist/` 文件夹中的内容复制到 Rime 的用户文件夹下。例如：用户文件夹为 `~/.config/ibus/rime/`，则相应的命令为 `cp -vr dist/. ~/.config/ibus/rime/`。

用户文件夹的位置与具体输入法（即 Rime 的前端）有关。多数情况下，可以在 [Rime 定制指南](https://github.com/rime/home/wiki/CustomizationGuide) 或相应输入法的文档中找到说明。

### 二、部署
完成复制后，即可部署。部署方法同样因具体输入法而异，一般也可在 Rime 定制指南或相应输入法的文档中找到。

### 注意
若您的输入法所用 librime 版本过旧，从而 opencc 版本过旧（低于 1.0），则 json 配置不被支持。这至少会使 `simplifier` 的 `jp_variants` 开关处于无效状态。

## 许可协议
* 除 `src/data` 及 `dist` 下的文件外，其余文件均按照 MIT License 发布。
* `src/data/JMdict/JMdict_e.xml` 文件来自 [JMdict](http://www.edrdg.org/jmdict/j_jmdict.html)，按照 CC BY-SA 3.0 许可协议发布，参见 http://www.edrdg.org/edrdg/licence.html 。
  `dist/nihongo-hybrid.dict/nihongo-hybrid.jmdict.dict.yaml` 由上述文件转换而得。
* `src/data/mozc_dictionaries` 下的文件来自开源输入法 [mozc](https://github.com/google/mozc)，授权信息见 `src/data/mozc_dictionaries/README.txt`。
  `dist/nihongo-hybrid.dict/nihongo-hybrid.mozc.dict.yaml` 由上述文件转换而得。
* `src/data/opencc/JPVariants.ocd` 来自 [OpenCC](https://github.com/BYVoid/OpenCC)，按照 Apache License 2.0 发布。
  `dist/opencc/JPVariants.ocd` 与上述文件相同。
* `src/data/internet-jp-forms.num` 来自该 [文件](http://corpus.leeds.ac.uk/frqc/internet-jp-forms.num)，用于生成词频，按照 [CC BY 2.5](https://creativecommons.org/licenses/by/2.5/) 许可协议发布.
