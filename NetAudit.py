# Date:2022.4.23
# Author:ChuLingEr
# Tip:nothing

import os
import time
from time import sleep
from pythonping import ping

a = 100
cnt = 1
# 监控网络通断    Monitor network connectivity
while a > 0:
    ping('www.baidu.com', count=1)
    # 判断ping是否成功    Determine whether the ping is successful
    if ping('www.baidu.com').success(True):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        print('网络正常')
    else:
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        print('已重连 第{}次'.format(cnt))
        os.system("python JSSMAuto.py")  # 调用自动登录脚本 Invoke automatic login script
        cnt += 1
    sleep(5)  # 每5秒检查一次 Check every 5 seconds
