import json
from bs4 import BeautifulSoup
import requests
import random
url = "http://www.seputu.com/"
user_agent_list = [
    "Mozilla/4.0(compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0(compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0(compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
]
user_agent = random.choice(user_agent_list)
headers = {
    "User_agent": user_agent
}
req = requests.get(url)
html = req.text

# 构建bs4对象, 解析方式为lxml, 也可以为parmas
soup = BeautifulSoup(html, 'lxml')
content = []
for mulu in soup.find_all(class_="mulu"):
    list=[]
    h2 = mulu.find('h2')
    # print(h2)
    if h2 != None:
        h2_title = h2.string
        # print(h2_title)
        # 获取章节内容，url地址
        for a in mulu.find(class_="box").find_all('a'):
            href = a.get('href')
            # split('') 指定字符串中指定字符进行切片
            # strip('') 吧字符串收尾指定字符切掉
            box_title = a.get('title').split(']')[-1].strip(' ')
            list.append({'href': href, 'box_title': box_title})
        content.append({'title': h2_title, 'content': list})
        # print(content)
with open('gcd.json', 'a', encoding='utf-8') as fp:
    json.dump(content, fp=fp, indent=4, ensure_ascii=False)

