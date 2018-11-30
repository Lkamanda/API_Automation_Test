'''
python 对json 操作氛围编码解码
编码
dumps : 把python 对象转成字符串
dump : 把python 对象转换成json对象 ， 可以通过流写入文件
解码
loads : 把json 对象转成python
load
'''
import json
# 把python 对象进行解码
str = [{'username':'xiaolin','age':'18'}]
print(type(str))
json_str = json.dumps(str, ensure_ascii=False)
print(json_str)
print(type(json_str))
new_str = json.loads(json_str)
print(new_str)