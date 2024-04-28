# rime-nihongo-hybrid

[RIME](http://rime.im/) 日语输入方案及词库。

## 使用方法

### 一、复制文件

从 https://github.com/sncix/rime-nihongo-hybrid/releases 下载 `dist.zip` 并解压；将 `dist/` 文件夹中的内容复制到 Rime 的用户文件夹下。例如：用户文件夹为 `~/.config/ibus/rime/`，则相应的命令为 `cp -vr dist/. ~/.config/ibus/rime/`。

用户文件夹的位置与具体输入法（即 Rime 的前端）有关。多数情况下，可以在 [Rime 定制指南](https://github.com/rime/home/wiki/CustomizationGuide) 或相应输入法的文档中找到说明。

### 二、部署

完成复制后，即可部署。部署方法同样因具体输入法而异，一般也可在 Rime 定制指南或相应输入法的文档中找到。

### 注意

若您的输入法所用 librime 版本过旧，从而 opencc 版本过旧（低于 1.0），则 json 配置不被支持。这至少会使 `simplifier` 的 `jp_variants` 开关处于无效状态。

## 许可协议

- 除 `third_party/` 及 `dist/` 下的文件外，其余文件均按照 MIT License 发布。
