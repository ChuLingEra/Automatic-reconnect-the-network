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
### 2. チュートリアル
ソースファイルは自分でコンパイルしてパッケージ化する必要がある

##### 2.1 プラグインのパッケージ化
```
pip install pyinstaller
```
##### 2.1 パッケージコード
```
pyinstaller xxx.py
```

### 3. 関連性を使う

-あなたが遭遇した現象が確かにバグであることを確認した后、[Issues](https://github.com/ChuLingEra/Automatic-reconnect-the-network/issues/new?assignees=&labels=&template=bug_report.md&title=) に問題を提出してください。そしてこの問題のためにできるだけはっきり説明して、提供されたissueテンプレートに従って記入します。ご協力ありがとうございます。

-キャンパスネットワークが随時中断される場合は、[Issues](https://github.com/ChuLingEra/Automatic-reconnect-the-network/issues/new?assignees=&labels=&template=feature_Request.md&title=) でリクエストを送信し、リクエストをフォーマットで入力します。 プロジェクト チーム メンバーは、最大 2 営業日以内に電子メールで連絡します。


## 貢献の源泉

### 主な貢献:
<a href="https://github.com/ChuLingEra"><img src="https://avatars.githubusercontent.com/u/104434077?s=400" alt="ChuLingEra" width="100"></a>

### 特別な貢献

### 貢献:

## オープンソース関係
本プロジェクトは、[GPL-3.0](https://github.com/ChuLingEra/Automatic-reconnect-the-network/blob/master/LICENSE)プロトコルを使用したオープンソースプロジェクトである。

### 主な引用:
[Selenium](https://www.selenium.dev/)のプラグインと関連するPythonパッケージから主に引用

## 貴いご意見をいただきたいのですが
