import os
import time

DEBUG = -1
INFO = 0
ERROR = 1

levels = {
    DEBUG: 'Debug',
    INFO: 'Info',
    ERROR: 'Error',
}


class BasicLogger:
    def __init__(self, settings):
        self.settings = settings

        self.log_time = time.strftime('%Y-%m-%d-%H%M%S', time.localtime())
        self.file_path = f'{settings.log_dir}/{self.log_time}.log'

        self.create_file()

    def test(self):
        print(self.log_time)
        print(self.file_path)
        print(self.file_object)
        for x in range(114514):
            self.log('cnm', level=DEBUG)

    def create_file(self):
        if not os.path.exists(self.settings.log_dir):
            os.mkdir(self.settings.log_dir)
        self.file_object = open(self.file_path, 'a', encoding='utf-8')

    def log(self, message='', level=INFO):
        print(f'[ {time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())} | {levels[level]} ] {message}')
        self.file_object.write(f'[ {time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())} | {levels[level]} ] {message}\n')
