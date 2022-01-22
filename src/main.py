"""
alpha3
NMSL - New
"""

from settings import Settings
from log import logger
from lang import LangBase
from java import jf


def main():
    sl_settings = Settings.Base()
    sl_lang = LangBase.getLang(sl_settings.language)
    sl_log = logger.BasicLogger(sl_settings)

    sl_log.log(message=sl_lang.start_log)

    java_list = jf.get_java()
    sl_log.log(message=f'{sl_lang.java_detected}:{java_list}')


if __name__ == '__main__':
    main()
