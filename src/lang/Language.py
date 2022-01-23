"""
Language classes
NMSL语言文件
包括大部分语言
by:woshishabi
"""


class LanguageBase:
    """
    NMSL 语言模板
    如果在语言类中没有找到对应的翻译就会使用这里的默认值
    """
    def __init__(self, name, description='A basic language basic class for NMSL, XD'):
        """
        LanguageBase 初始化
        :param name: 语言识别名称
        :param description: 语言描述
        """

        self.description = description
        self.name = name

        # 启动时的输出
        self.start_log = 'Naughty Minecraft Server Launcher started.'
        self.version_log = 'NMSL version'
        self.selected_lang = 'Current Language'
        self.java_detected = 'Detected Java environment'

        # 下载时的输出
        self.start_download_part = 'Download started - parts count'
        self.download_progress_bar = 'Downloading'


class English(LanguageBase):
    def __init__(self):
        LanguageBase.__init__(self, 'en', description='English')

        self.start_log = 'Naughty Minecraft Server Launcher started.'
        self.version_log = 'NMSL version'
        self.selected_lang = 'Current Language'
        self.java_detected = 'Detected Java environment'

        self.start_download_part = 'Download started - parts count'
        self.download_progress_bar = 'Downloading'


class Chinese(LanguageBase):
    def __init__(self):
        LanguageBase.__init__(self, 'cn', description='中文')

        self.start_log = 'NMSL 已启动！'
        self.version_log = 'NMSL版本'
        self.selected_lang = '当前语言'
        self.java_detected = '完成检测Java运行环境'

        self.start_download_part = '开始下载-分块数'
        self.download_progress_bar = '下载文件'


# 语言列表
# 定义的语言需要在这里注册
list = {
    'cn': Chinese,
    'en': English,
}


# 获取语言类，默认中文
def getLang(name='cn'):
    try:
        return list[name]()
    except KeyError:
        return LanguageBase
