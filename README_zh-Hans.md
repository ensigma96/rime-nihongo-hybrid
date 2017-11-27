# rime-nihongo-hybrid
[RIME](http://rime.im/) 日语输入方案及词库，词库部分由开源输入法 [mozc](https://github.com/google/mozc) 的词典转换而来。关于词典的授权，可参阅 https://github.com/google/mozc/blob/master/src/data/dictionary_oss/README.txt 。

## 使用方法
### 一、复制文件
将 `dist/` 文件夹中的内容复制到 Rime 的用户文件夹下。例如：用户文件夹为 `~/.config/ibus/rime/`，则相应的命令为 `cp -vr dist/. ~/.config/ibus/rime/`。

用户文件夹的位置与具体输入法（即 Rime 的前端）有关。多数情况下，可以在 [Rime 定制指南](https://github.com/rime/home/wiki/CustomizationGuide) 或相应输入法的文档中找到说明。

### 二、部署
完成复制后，即可部署。部署方法同样因具体输入法而异，一般也可在 Rime 定制指南或相应输入法的文档中找到。

### 复古模式
若您的输入法所用 librime 版本过旧（从而 opencc 版本过旧（低于 1.0）），则 json 配置可能不被支持。在此情况下，请将 `main.conf.example` 重命名为 `main.conf`，并修改 `main.conf`，设置 `OPENCC_LEGACY_MODE` 为 1。然后执行 `./main.sh`，再按照步骤一、二做即可。
