"""
Basic Settings
NMSL基本设置
NMSL的大部分设置都可以在这里修改
by:woshishabi
"""


class Base:
    def __init__(self):
        """
        初始化一个基础设置
        """
        # 程序名称（未使用）
        self.name = 'Naughty Minecraft Server Launcher'
        # NMSL程序版本
        self.version = [
            ['alpha', 3, 2],
            'Alpha1.0.1'
        ]
        # NMSL开发者（未使用）
        self.author = 'woshishabi'

        # 日志文件夹
        self.log_dir = 'logs'

        # 程序语言
        self.language = 'cn'

        # 下载源
        self.sources = {
            'mojang':'https://launchermeta.mojang.com/mc/game/version_manifest.json',
        }
