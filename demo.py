# coding=utf-8
# 第一行谨防之后用非python3.X系打开
import csv
import time
import requests
import json
#先创建存入数据的文件
finaldata = open('摸的数据.csv', mode='w',encoding = 'utf-8', newline = '')
csvwriter = csv.writer(finaldata)
csvwriter.writerow(['评论者用户名', '评论内容', '评论时间'])
#发送请求
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
for page in range(0,51):
    print( f'正在爬取第{page}页')
    url = "https://club.jd.com/comment/productPageComments.action?&productId=100019125569&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1".format(page)
    resp = requests.get(url,headers=headers)
#转换数据 找到所需数据
    rowdata = resp.json()
    JDcomments = rowdata["comments"]
    for comment in JDcomments:
        name = comment["nickname"]
        content = comment["content"]
        product_time = comment["creationTime"]
        print(name,content,product_time)
        csvwriter.writerow([name,content,product_time])
    time.sleep(5)

