[English](README.md)|[简体中文](README_zh-CN.md)|[繁體中文](README_tw.md)|**日本語**

# ネットワークの自動再接続
_このプロジェクトは、短大のネットワーク認証システムが時々切断されるという問題を解決することを目指し、
学生がインターネットにアクセスできなくなり、すべてではないがいくつかの解決策を提案する。_

## はじめに


### 1.前提条件

##### 1.1
学校でウェブ認証を使用している場合は、まず Chrome と Chromedriver をインストールする必要があります。ChromeとChromedriverのバージョンは同じでなければならないことに注意してください。そうしないと、Chromeドライバを使用してChromeをデバッグできないなど、不明なエラーが発生する可能性があります。

_インストールする独自のバージョンを選択できますが、推奨バージョンをインストールすることをお勧めします。_

```
|-- resource
    |-- precondition
        |-- 99.0.4844.51_chrome64_stable_windows_installer.exe
        |-- chromedriver.exe

```
上記のように、ディレクトリにはダウンロードするための推奨バージョンがあります。
以下のチュートリアルはすべて、このバージョンのChromeとChromedriverに基づいています。

##### 1.2
Chromeがインストールされたら、ダウンロードしたChromeをインストールし、ChromeドライバをChromeのインストールディレクトリに移動する必要があります

Chromeのインストールディレクトリを見つけるにはいくつかの方法がありますが、Chromedriver.exeをアプリケーションディレクトリに移動するだけです

##### 1.3
次に、Chromeのインストールディレクトリをコンピュータのグローバル変数に追加する必要があります

**どんな問題でも、Googleで検索することができます**

## ディレクトリ構造
```
|-- Automatic-reconnect-the-network
    |-- .gitignore
    |-- README.md·····················ヘルプ
    |-- README_ja.md
    |-- README_tw.md
    |-- README_zh-CN.md
    |
    |-- resource······················ファイル
    |   |-- precondition
    |
    |-- sort··························コード
        |-- chinese···················国家
            |-- xxxxx·················大学コード
```
### 2.The tutorial
Source files need to be compiled and packaged yourself

##### 2.1 Packaging plug-in
```
pip install pyinstaller
```
##### 2.2 Packaging code
```
pyinstaller xxx.py
```

### 3.Usage related

Upon confirmation of you meet phenomenon is indeed a Bug, please submit problem in [Issues](https://github.com/ChuLingEra/Automatic-reconnect-the-network/issues/new?assignees=&labels=&template=bug_report.md&title=), and for as far as possible the problem description is clear,
Fill in the issue template as provided. Thank you for your cooperation

-If your campus network is interrupted from time to time, Please in [Issues](https://github.com/ChuLingEra/Automatic-reconnect-the-network/issues/new?assignees=&labels=&template=feature_Request.md&title=), submit the request and enter your request in the format.
You will be contacted by email from a project team member at most two business days.

## Source contribution

### Main contributions:
<a href="https://github.com/ChuLingEra"><img src="https://avatars.githubusercontent.com/u/104434077?s=400" alt="ChuLingEra" width="100"></a>

### Special contributions:

### Contribution:

## Open source related
This project is open source using [GPL3.0](https://github.com/ChuLingEra/Automatic-reconnect-the-network/blob/master/LICENSE) protocol



### Refer to relevant:
Mainly referenced from the plug-in in [Selenium](https://www.selenium.dev/) And associated Python packages

## I hope you can put forward your valuable suggestions