import re #导入正则表达式模块
import requests #python HTTP客户端 编写爬虫和测试服务器经常用到的模块
import time
from PIL import Image
from lxml import etree
 
#定义函数方法
def spiderPic(html):
    print('正在查找壁纸，请稍后......')
    html = etree.HTML(html)
    html_data = html.xpath('/html/head/link[@id="bgLink"]/@href')   #查找URL
    for addr in html_data:
        actaddr="https://cn.bing.com"+addr
        print('正在下载壁纸：'+addr[11:42]+'...')  #爬取的地址长度超过30时，用'...'代替后面的内容
 
        try:
            pics = requests.get(actaddr,timeout=10)  #请求URL时间（最大10秒）
        except requests.exceptions.ConnectionError:
            print('您当前请求的URL地址出现错误')
            continue

        localtime = time.localtime(time.time())
        filename=re.findall(r'([a-zA-Z0-9_-]*)_1920x1080.jpg',addr)
        fq = open('D:\\Photos\\壁纸\\' + (str(filename[0])+"_"+str(localtime.tm_year)+'_'+str(localtime.tm_mon)+'_'+str(localtime.tm_mday)+'.jpg'),'wb')     #下载图片，并保存和命名
        fq.write(pics.content)
        fq.close()

        im = Image.open('D:\\Photos\\壁纸\\' + (str(filename[0])+"_"+str(localtime.tm_year)+'_'+str(localtime.tm_mon)+'_'+str(localtime.tm_mday)+'.jpg'))
        im.show()
 
#python的主方法
if __name__ == '__main__':
    print("现在时间："+time.asctime(time.localtime(time.time())) + ",为您下载今日Bing壁纸")
    result = requests.get('https://cn.bing.com/')
    # result = requests.get('https://cn.bing.com/?FORM=BEHPTB&ensearch=1')
 
    #调用函数
    spiderPic(result.text)
