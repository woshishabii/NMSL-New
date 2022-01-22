import subprocess
import os


def run_command(command: str) -> iter:
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')


def get_java():
    """
    Only for java in environment variable
    :return: java installed on the computer
    """
    java_list = {}
    jre_home = os.environ.get('JRE_HOME')
    jdk_home = os.environ.get('JDK_HOME')

    temp = list(run_command(f'{jre_home}\\java.exe --version'))[0].decode('utf-8').replace('\r\n', '')
    if temp.startswith("Unrecognized"):
        java_list[list(run_command(f'{jre_home}\\java.exe -version'))[0].decode('utf-8').replace('\r\n', '')] = f'{jre_home}\\java.exe'
    elif temp.startswith("java"):
        java_list[temp] = f'{jre_home}\\java.exe'
    else:
        pass

    temp = list(run_command(f'{jdk_home}\\java.exe --version'))[0].decode('utf-8').replace('\r\n', '')
    if temp.startswith("Unrecognized"):
        java_list[list(run_command(f'{jdk_home}\\java.exe -version'))[0].decode('utf-8').replace('\r\n', '')] = f'{jdk_home}\\java.exe'
    elif temp.startswith("java"):
        java_list[temp] = f'{jdk_home}\\java.exe'
    else:
        pass

    return java_list


# print(get_java())
