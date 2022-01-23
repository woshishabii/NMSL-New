"""
alpha3
NMSL - New
NMSL主文件
by:woshishabi
"""

# 导入库
import wx

from settings import Settings
from log import logger
from lang import Language
from java import jf
from net import download
from net import get_vanilla
from gui import root


# 导入主函数
def main():
    # 设置类
    sl_settings = Settings.Base()
    # 语言类
    sl_lang = Language.getLang(sl_settings.language)
    # 日志类
    sl_log = logger.BasicLogger(sl_settings)

    # 启动日志
    sl_log.log(message=sl_lang.start_log)
    # 输出NMSL版本
    sl_log.log(message=f'{sl_lang.version_log}: {sl_settings.version[1]}')
    # 输出NMSL语言
    sl_log.log(message=f'{sl_lang.selected_lang}: {sl_settings.language}')

    # 获取Java列表
    java_list = jf.get_java()
    # Java日志
    sl_log.log(message=f'{sl_lang.java_detected}:{java_list}')

    # 测试
    # sl_log.log(message=get_vanilla.get_by_mojang(sl_settings), level=sl_log.DEBUG)


def dev():
    mainAPP = wx.App()
    mainFrame = root.MainFrame(None, title='NMSL Alpha 1.0.2')
    mainFrame.Show()
    mainAPP.MainLoop()

if __name__ == '__main__':
    # TODO
    # What to do?
    # main()
    dev()
