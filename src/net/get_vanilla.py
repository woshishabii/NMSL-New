"""
Get vanilla info
获取原版服务端信息
by:woshishabi
"""

# 导入库
import requests
import json
import sys


# 获取mojang服务器数据
def get_by_mojang(sl_settings):
    manifest_request = requests.get(sl_settings.sources['mojang'])
    # Original Data / 原始数据
    o_data = json.loads(manifest_request.text)
    # sl_log.log(message=data)
    p_data = {'release': {}, 'snapshot': {}, 'old_beta': {}, 'old_alpha': {}}
    for temp in o_data['versions']:
        # print(temp)
        p_data[temp['type']][temp['id']] = [temp['url'], temp['time']]

    p_data['latest'] = o_data['latest']
    return p_data
