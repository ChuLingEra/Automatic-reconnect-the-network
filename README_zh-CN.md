[English](README.md)|**简体中文**|[繁體中文](README_tw.md)|[日本語](README_ja.md)

# 标题
_本项目旨在解决高校网络认证系统不时断线的问题，
导致学生无法上网，并提出了一些但不是全部的解决方案。_

## 开始

### 1.开始之前

##### 1.1

如果您的学校使用web认证，您需要先安装Chrome和Chromedriver。请注意Chrome浏览器和Chromedriver的版本必须相同。否则可能会出现未知错误，如使用Chromedriver无法调试Chrome。

_您可以选择自己的版本进行安装，但仍然建议您安装我们推荐的版本。_

```
|-- resource
    |-- precondition
        |-- 99.0.4844.51_chrome64_stable_windows_installer.exe
        |-- chromedriver.exe

```
如上，该目录有我们推荐的版本供您下载。

下面的所有教程都是基于这个版本的Chrome和Chromedriver。

##### 1.2
你将需要安装你下载的Chrome，并移动Chromedriver.exe到你的Chrome安装目录

有几种方法可以找到您的Chrome安装目录，只需将Chromedriver.exe移动到应用程序目录。

##### 1.3
接下来你需要将你的Chrome安装目录添加到你的计算机的全局变量中

**任何问题步骤都可以在[百度](https://www.baidu.com)上进行搜索**

## 目录结构
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
### 2.使用教程
该教程的源文件需要自己编译和打包

##### 2.1 包装插件
```
pip install pyinstaller
```
##### 2.2 包装代码
```
pyinstaller xxx.py
```

### 3.使用相关的
-一旦确认您遇到的现象确实是Bug，请提交问题 [Issues](https://github.com/ChuLingEra/Automatic-reconnect-the-network/issues/new?assignees=&labels=&template=bug_report.md&title=), 为了使问题描述尽可能清晰，
根据提供的信息填写问题模板。谢谢你的合作

-如果您的校园网络不时中断，请进来[Issues](https://github.com/ChuLingEra/Automatic-reconnect-the-network/issues/new?assignees=&labels=&template=feature_Request.md&title=), 提交请求并按格式输入您的请求。
项目团队成员最多在两个工作日内会通过电子邮件联系您。

## 贡献

### 主要贡献:
<a href="https://github.com/ChuLingEra"><img src="https://avatars.githubusercontent.com/u/104434077?s=400" alt="ChuLingEra" width="100"></a>

### 特殊贡献:

### 其他贡献:

## 开放源码的相关
本项目是开源使用 [GPL3.0](https://github.com/ChuLingEra/Automatic-reconnect-the-network/blob/master/LICENSE) 协议

### 参考相关:
主要引用自插件 [Selenium](https://www.selenium.dev/) 和相关的Python包

## 我们希望您能提出宝贵意见，并参与到项目中来。
