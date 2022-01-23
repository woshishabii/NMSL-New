"""
alpha3
NMSL - New
NMSL主文件
by:woshishabi
"""

# 导入库
from settings import Settings
from log import logger
from lang import Language
from java import jf
from net import download


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

    # download.download(sl_log, sl_lang, 'https://addons-ecs.forgesvc.net/api/v2/addon/search?gameId=432&pageSize=50&categoryId=0&sectionId=6&sort=5%E2%80%99', 'curseforge.json')


if __name__ == '__main__':
    # TODO
    # What to do?
    main()
