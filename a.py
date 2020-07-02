import requests
import re
from urllib.request import urlopen

url = 'http://www.cae.cn/cae/html/main/col48/column_48_1.html'
respond = requests.get(url)
respond.encoding = 'utf-8'

every_num = re.findall('<a href="/cae/html/main/colys/(\d+).html" target="_blank">', respond.text)

count = 1

for man in every_num[:1000]:

    man_url = 'http://www.cae.cn/cae/html/main/colys/{}.html'.format(man)
    man_respond = requests.get(man_url)
    man_respond.encoding = 'utf-8'

    text1 = re.findall('<div class="intro">(.*?)</div>', man_respond.text, re.S)
    text2 = re.sub(r'<p>|&ensp;|&nbsp;|</p>', '', text1[0]).strip()

    # print(text2)
    file_name = re.findall('<div class="right_md_name">(.*?)</div>', man_respond.text)[0]
    with open(file_name + '.txt', mode='a+', encoding="utf-8") as f:
        f.write('{}. '.format(count) + text2 + '\n')
        count += 1

    photo = r'<img src="/cae/admin/upload/img/(.+)" style='
    result = re.findall(photo, man_respond.text, re.I)

    if result:
        picurl = r'http://www.cae.cn/cae/admin/upload/img/{0}'.format(result[0].replace(' ', r'%20'))
        img_name = re.findall('<div class="right_md_name">(.*?)</div>', man_respond.text)[0]
        with open(img_name + '.jpg', 'wb') as fpic:
            fpic.write(urlopen(picurl).read())
