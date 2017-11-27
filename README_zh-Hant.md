# rime-nihongo-hybrid
[RIME](http://rime.im/) 日語輸入方案及詞庫，詞庫部分由開源輸入法 [mozc](https://github.com/google/mozc) 的詞典轉換而來。關於詞典的授權，可參閱 https://github.com/google/mozc/blob/master/src/data/dictionary_oss/README.txt 。

## 使用方法
### 一、複製文件
將 `dist/` 文件夾中的內容複製到 Rime 的用戶文件夾下。例如：用戶文件夾爲 `~/.config/ibus/rime/`，則相應的命令爲 `cp -vr dist/. ~/.config/ibus/rime/`。

用戶文件夾的位置與具體輸入法（即 Rime 的前端）有關。多數情況下，可以在 [Rime 定製指南](https://github.com/rime/home/wiki/CustomizationGuide) 或相應輸入法的文檔中找到說明。

### 二、部署
完成複製後，即可部署。部署方法同樣因具體輸入法而異，一般也可在 Rime 定製指南或相應輸入法的文檔中找到。

### 復古模式
若您的輸入法所用 librime 版本過舊（從而 opencc 版本過舊（低於 1.0）），則 json 配置可能不被支持。在此情況下，請將 `main.conf.example` 重命名爲 `main.conf`，並修改 `main.conf`，設置 `OPENCC_LEGACY_MODE` 爲 1。然後執行 `./main.sh`，再按照步驟一、二做即可。
