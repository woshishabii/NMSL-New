"""
woshishabi的编译工具
使用pyinstaller
"""

# 导入库
import os
import time
import shutil

import src.settings.Settings


# 获取当前时间
current_time = time.strftime('%y%m%d%H%M', time.localtime())
print(f'编译日期 - {current_time}')

# 获取程序版本
build_settings = src.settings.Settings.Base()
version = f'{build_settings.version[0][0]}-{build_settings.version[0][1]}-{build_settings.version[0][2]}'

# 输出文件名称
out_name = f'{version}-{current_time}'

# 编译
print('输出文件：', f'{out_name}.exe')
os.system(f'pyinstaller -n {out_name} -F main.py')

# 清理文件
try:
    shutil.rmtree('build')
    os.remove(f'{out_name}.spec')
except:
    pass

print('编译完成')