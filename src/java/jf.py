"""
Java Functions
和Java有关的函数
by: woshishabi
"""

import subprocess
import os


# 运行cmd指令并返回输出内容
def run_command(command: str) -> iter:
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')


def get_java() -> dict:
    """
    仅能获取在系统环境变量中的Java
    :return: 电脑上安装的Java环境
    """
    java_list = {}

    # 获取环境变量
    jre_home = os.environ.get('JRE_HOME')
    jdk_home = os.environ.get('JDK_HOME')

    # Java Runtime Environment 环境变量检查
    try:
        temp = list(run_command(f'{jre_home}\\java.exe --version'))[0].decode('utf-8').replace('\r\n', '')
        if temp.startswith("Unrecognized"):
            java_list[list(run_command(f'{jre_home}\\java.exe -version'))[0].decode('utf-8').replace('\r\n', '')] = f'{jre_home}\\java.exe'
        elif temp.startswith("java"):
            java_list[temp] = f'{jre_home}\\java.exe'
        else:
            pass
    except FileNotFoundError:
        pass

    # Java Development Kit 环境变量检查
    try:
        temp = list(run_command(f'{jdk_home}\\java.exe --version'))[0].decode('utf-8').replace('\r\n', '')
        if temp.startswith("Unrecognized"):
            java_list[list(run_command(f'{jdk_home}\\java.exe -version'))[0].decode('utf-8').replace('\r\n', '')] = f'{jdk_home}\\java.exe'
        elif temp.startswith("java"):
            java_list[temp] = f'{jdk_home}\\java.exe'
        else:
            pass
    except FileNotFoundError:
        pass

    # 返回列表
    return java_list


# print(get_java())
