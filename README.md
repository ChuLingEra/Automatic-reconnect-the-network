**English**|[简体中文](README_zh-CN.md)|[繁體中文](README_tw.md)|[日本語](README_ja.md)

# Automatic-reconnect-the-network
_This project aims to solve the problem that the network authentication system of colleges and universities is disconnected from time to time,
leading to students' inability to access the Internet, and proposes some but not all solutions._  

## Get started

### 1.Precondition

##### 1.1
If your school uses web authentication, you need to install Chrome and Chromedriver first.Please note that the versions of Chrome and Chromedriver must be the same.Otherwise, unknown errors may occur, such as failure to debug Chrome using Chromedriver.

_You can choose your own version to install, but it is still recommended that you install our recommended version._

```
|-- resource
    |-- precondition
        |-- 99.0.4844.51_chrome64_stable_windows_installer.exe
        |-- chromedriver.exe

```
As mentioned above, the directory has our recommended version for you to download. 
All the following tutorials are based on this version of Chrome and Chromedriver.

##### 1.2
You will need to install the Chrome you downloaded and move Chromedriver to your Chrome installation directory once Chrome is installed

There are several ways to find your Chrome installation directory, just move Chromedriver.exe to the Application directory.

##### 1.3
Next you need to add your Chrome installation directory to your computer's global variables  

**Any problems step can be to search on Google**

## Directory structure
```
|-- Automatic-reconnect-the-network
    |-- .gitignore
    |-- README.md·····················help
    |-- README_ja.md
    |-- README_tw.md
    |-- README_zh-CN.md
    |
    |-- resource······················file
    |   |-- precondition
    |
    |-- sort··························code
        |-- chinese···················nation
            |-- xxxxx·················College code
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
-Upon confirmation of you meet phenomenon is indeed a Bug, please submit problem in [Issues](https://github.com/ChuLingEra/Automatic-reconnect-the-network/issues/new?assignees=&labels=&template=bug_report.md&title=), and for as far as possible the problem description is clear,
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



