"""
Logger
日志记录工具
by:woshishabi
"""

# 导入库
import os
import time

# 声明日志级别
# DEBUG : 调试
# INFO : 一般信息
# ERROR : 错误信息

DEBUG = -1
INFO = 0
ERROR = 1

# 注册日志级别
levels = {
    DEBUG: 'Debug',
    INFO: 'Info',
    ERROR: 'Error',
}


class BasicLogger:
    def __init__(self, settings):
        """
        一个基础的日志系统
        :param settings: sl_settings NMSL设置
        """
        self.settings = settings

        self.DEBUG = -1
        self.INFO = 0
        self.ERROR = 1

        self.log_time = time.strftime('%Y-%m-%d-%H%M%S', time.localtime())
        self.file_path = f'{settings.log_dir}/{self.log_time}.log'

        self.create_file()

    def test(self):
        """
        这是一个测试函数（早期测试）
        """
        print(self.log_time)
        print(self.file_path)
        print(self.file_object)
        for x in range(114514):
            # 哼，哼哼，啊啊啊啊啊啊啊啊啊啊啊啊啊！
            self.log('cnm', level=DEBUG)

    def create_file(self):
        # 创建日志文件
        if not os.path.exists(self.settings.log_dir):
            os.mkdir(self.settings.log_dir)
        self.file_object = open(self.file_path, 'a', encoding='utf-8')

    def log(self, message='', level=INFO, end='\n'):
        # 生成一条日志
        print(f'[ {time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())} | {levels[level]} ] {message}', end=end)
        self.file_object.write(f'[ {time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())} | {levels[level]} ] {message}\n')
