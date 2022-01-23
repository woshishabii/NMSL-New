class LanguageBase:
    def __init__(self, name=None, description='A basic language basic class for NMSL, XD'):
        self.description = description

        self.name = name

        self.start_log = 'Naughty Minecraft Server Launcher started.'
        self.version_log = 'NMSL version'
        self.selected_lang = 'Current Language'
        self.java_detected = 'Detected Java environment'

        self.start_download_part = 'Download started - parts count'
        self.download_progress_bar = 'Downloading'


class English(LanguageBase):
    def __init__(self):
        LanguageBase.__init__(self, name='en', description='English')

        self.start_log = 'Naughty Minecraft Server Launcher started.'
        self.version_log = 'NMSL version'
        self.selected_lang = 'Current Language'
        self.java_detected = 'Detected Java environment'

        self.start_download_part = 'Download started - parts count'
        self.download_progress_bar = 'Downloading'


class Chinese(LanguageBase):
    def __init__(self):
        LanguageBase.__init__(self, name='cn', description='中文')

        self.start_log = 'NMSL 已启动！'
        self.version_log = 'NMSL版本'
        self.selected_lang = '当前语言'
        self.java_detected = '完成检测Java运行环境'

        self.start_download_part = '开始下载-分块数'
        self.download_progress_bar = '下载文件'


list = {
    'cn': Chinese,
    'en': English,
}


def getLang(name='cn'):
    try:
        return list[name]()
    except KeyError:
        return LanguageBase
