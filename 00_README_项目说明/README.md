# SDXCode 整理说明

本次整理以 `01_SpaDigiX主程序/SpaDigiX_1.0.7.20230910_Beta.py` 为当前重点主程序。

## 主要目录

- `01_SpaDigiX主程序/`: 当前重点主程序及其运行所需图片、ini 配置。为兼容原代码的相对路径，关键资源同时平铺在主程序同级，并备份在 `assets/`、`configs/` 中。
- `02_SpaDigiX函数版/app0_基础排盘/`: 应用0基础排盘函数，主文件为 `functionSpaDigiXAPPONE.py`。
- `02_SpaDigiX函数版/app1_app2_后续函数/`: 基于应用0继续发展的定位、定级、取值函数。
- `03_STDLAB定位定级/`: STDLAB、定位定级相关原目录，保留原上下文。
- `04_数据文件/`: 大型数据文件、Excel、星历文件等。
- `90_历史版本归档/`: 旧版 GUI、测试脚本、备份脚本、打包产物和其他实验文件。

## 应用0说明

当前主应用0版本来自：

`03_STDLAB定位定级/STDLABGO20240409/functionSpaDigiXAPPONE.py`

整理后复制到：

`02_SpaDigiX函数版/app0_基础排盘/functionSpaDigiXAPPONE.py`

旧版三返回值版本保留在：

`02_SpaDigiX函数版/versions/functionSpaDigiXAPPONE_20231227_三返回值.py`

## 注意事项

- 本次没有重构代码。
- 本次没有修改主程序源码。
- `SpaDigiX_1.1.6.20230910_Beta/` 目录移动时被系统提示正在被其他进程占用，因此暂时保留在根目录。
- 原项目没有 `XLJT.png`，但主程序引用了该文件名；已将现有 `XLJT.jpg` 复制为 `01_SpaDigiX主程序/XLJT.png` 和 `01_SpaDigiX主程序/assets/XLJT.png` 以保持兼容。
