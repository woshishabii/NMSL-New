"""
Get vanilla info
获取原版服务端信息
by:woshishabi
"""

# 导入库
import requests
import json


# 获取mojang服务器数据
def get_by_mojang(sl_settings):
    manifest_request = requests.get(sl_settings.sources['mojang'])
    o_data = json.loads(manifest_request.text)
    # sl_log.log(message=data)
    p_data = {}
    # p_data['latest'] = o_data['latest']
    return p_data
