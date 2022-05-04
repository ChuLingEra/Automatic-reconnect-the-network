[English](README.md)|**简体中文**|[繁體中文](README_tw.md)|[日本語](README_ja.md)

# Automatic-reconnect-the-network
_本項目旨在解決高校網絡認證系統不時斷線的問題，
導致學生無法上網，並提出了一些但不是全部的解決方案。_

## 開始

### 1先決條件

##### 1.1

前提條件如果您的學校使用web認證，您需要先安裝Chrome和Chromedriver。請注意Chrome浏覽器和Chromedriver的版本必須相同。否則可能會出現未知錯誤，如使用Chromedriver無法調試Chrome。

_您可以選擇自己的版本進行安裝，但仍然建議您安裝我們推薦的版本。_

```
|-- resource
    |-- precondition
        |-- 99.0.4844.51_chrome64_stable_windows_installer.exe
        |-- chromedriver.exe

```
如上所述，該目錄有我們推薦的版本供您下載。

下面的所有教程都是基于這個版本的Chrome和Chromedriver。

##### 1.2
你將需要安裝你下載的Chrome，並移動Chromedriver.exe到你的Chrome安裝目錄

有幾種方法可以找到您的Chrome安裝目錄，只需將Chromedriver.exe移動到應用程序目錄。

##### 1.3
接下來你需要將你的Chrome安裝目錄添加到你的計算機的全局變量中

**任何問題步驟都可以在[百度](https://www.baidu.com)上進行搜索**

## 目錄結構
```
|-- Automatic-reconnect-the-network
    |-- .gitignore
发v回娘家    |-- README.md·····················帮助
    |-- README_ja.md
    |-- README_tw.md
    |-- README_zh-CN.md
    |
    |-- resource······················文件
    |   |-- precondition
    |
    |-- sort··························代码
        |-- chinese···················国家
            |-- xxxxx·················国家大学
```
### 2.本教程
該教程的源文件需要自己編譯和打包

##### 2.1 包裝插件
```
pip install pyinstaller
```
##### 2.2 包裝代碼
```
pyinstaller xxx.py
```

### 3.使用相關的
-一旦确认您遇到的现象确实是Bug，请提交问题 [Issues](https://github.com/ChuLingEra/Automatic-reconnect-the-network/issues/new?assignees=&labels=&template=bug_report.md&title=), 爲了使問題描述盡可能清晰，
根據提供的信息填寫問題模板。謝謝你的合作

-如果您的校園網絡不時中斷，請進來[Issues](https://github.com/ChuLingEra/Automatic-reconnect-the-network/issues/new?assignees=&labels=&template=feature_Request.md&title=), 提交請求並按格式輸入您的請求。
項目團隊成員最多在兩個工作日內會通過電子郵件聯系您。

## 貢獻

### 主要貢獻:
<a href="https://github.com/ChuLingEra"><img src="https://avatars.githubusercontent.com/u/104434077?s=400" alt="ChuLingEra" width="100"></a>

### 特殊貢獻:

### 其他貢獻:

## 開放源碼的相關
本項目是開源使用 [GPL3.0](https://github.com/ChuLingEra/Automatic-reconnect-the-network/blob/master/LICENSE) 協議

### 參考相關:
主要引用自插件 [Selenium](https://www.selenium.dev/) 和相關的Python包

## 希望您能提出寶貴意見
