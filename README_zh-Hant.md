# rime-nihongo-hybrid
[RIME](http://rime.im/) 日語輸入方案及詞庫。

## 使用方法
### 一、複製文件
將 `dist/` 文件夾中的內容複製到 Rime 的用戶文件夾下。例如：用戶文件夾爲 `~/.config/ibus/rime/`，則相應的命令爲 `cp -vr dist/. ~/.config/ibus/rime/`。

用戶文件夾的位置與具體輸入法（即 Rime 的前端）有關。多數情況下，可以在 [Rime 定製指南](https://github.com/rime/home/wiki/CustomizationGuide) 或相應輸入法的文檔中找到說明。

### 二、部署
完成複製後，即可部署。部署方法同樣因具體輸入法而異，一般也可在 Rime 定製指南或相應輸入法的文檔中找到。

### 注意
若您的輸入法所用 librime 版本過舊，從而 opencc 版本過舊（低於 1.0），則 json 配置不被支持。這至少會使 `simplifier` 的 `jp_variants` 開關處於無效狀態。

## 許可協議
* 除 `src/data` 下的文件外，其餘文件均按照 MIT License 發佈。
* `src/data/JMdict/JMdict_e.xml` 文件來自 [JMdict](http://www.edrdg.org/jmdict/j_jmdict.html)，按照 CC BY-SA 3.0 許可協議发布，参见 http://www.edrdg.org/edrdg/licence.html 。
  `dist/nihongo-hybrid.dict/nihongo-hybrid.jmdict.dict.yaml` 由上述文件轉換而得。
* `src/data/mozc_dictionaries` 下的文件來自開源輸入法 [mozc](https://github.com/google/mozc)，授權信息見 `src/data/mozc_dictionaries/README.txt`。
  `dist/nihongo-hybrid.dict/nihongo-hybrid.mozc.dict.yaml` 由上述文件轉換而得。
* `src/data/opencc/JPVariants.ocd` 來自 [OpenCC](https://github.com/BYVoid/OpenCC)，按照 Apache License 2.0 發佈。
  `dist/opencc/JPVariants.ocd` 與上述文件相同。
