"""
alpha3
NMSL - New
"""

from settings import Settings
from log import logger
from lang import LangBase
from java import jf
from net import download


def main():
    sl_settings = Settings.Base()
    sl_lang = LangBase.getLang(sl_settings.language)
    sl_log = logger.BasicLogger(sl_settings)

    sl_log.log(message=sl_lang.start_log)
    sl_log.log(message=f'{sl_lang.version_log}: {sl_settings.version[1]}')
    sl_log.log(message=f'{sl_lang.selected_lang}: {sl_settings.language}')
    sl_log.log()

    java_list = jf.get_java()
    sl_log.log(message=f'{sl_lang.java_detected}:{java_list}')

    download.download(sl_log, sl_lang, 'https://addons-ecs.forgesvc.net/api/v2/addon/search?gameId=432&pageSize=50&categoryId=0&sectionId=6&sort=5%E2%80%99', 'curseforge.json')


if __name__ == '__main__':
    main()
