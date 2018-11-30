# use/bin/env python3.6
# conding:utf-8
# Author:xiaolin

import os

def data_dir(data=None, filename=None):
    # os.path.dirname(__file__) : 返回当前脚本路径
    # 查找文件路径
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), data, filename)

print(data_dir('data', 'data.xls'))