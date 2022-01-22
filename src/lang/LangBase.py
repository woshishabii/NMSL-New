class LanguageBase:
    def __init__(self, name=None, description='A basic language basic class for NMSL, XD'):
        self.description = description

        self.name = name

        self.start_log = 'Naughty Minecraft Server Launcher started.'
        self.java_detected = 'Detected Java environment'


class English(LanguageBase):
    def __init__(self):
        LanguageBase.__init__(self, name='en', description='English')

        self.start_log = 'Naughty Minecraft Server Launcher started.'
        self.java_detected = 'Detected Java environment'


class Chinese(LanguageBase):
    def __init__(self):
        LanguageBase.__init__(self, name='cn', description='中文')

        self.start_log = 'NMSL 已启动！'
        self.java_detected = '完成检测Java运行环境'


list = {
    'cn': Chinese,
    'en': English,
}


def getLang(name='cn'):
    try:
        return list[name]()
    except KeyError:
        return LanguageBase
