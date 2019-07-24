from urllib import request
from lxml import etree
import threading
from Main import *


class Weather(threading.Thread):
    def __init__(self):

        threading.Thread.__init(self)
        url = 'http://www.weather.com.cn/weather1d/101270101.shtml'
        self.url=url

        self.Headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    def run(self):
        req = request.Request(url=self.url, headers=self.Headers)
        resp=request.urlopen(req)
        html=resp.read()

        root=etree.HTML(html)
        weather=root.xpath('//*[@id="today"]/div[2]/ul/li[1]/p[1]/@title')
        temprate=root.xpath('//*[@id="today"]/div[2]/ul/li[1]/p[2]/span/text()')
        #print(weather)
        #print(temprate)
        self.Main.setTemp(temprate)





if __name__ == '__main__':
    #中国天气网
    url='http://www.weather.com.cn/weather1d/101270101.shtml'
    w=Weather(url)
    w.go()