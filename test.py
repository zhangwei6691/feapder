# -*- coding: utf-8 -*-
"""
Created on 2021-12-24 16:58:18
---------
@summary:
---------
@author: zhangwei
"""

import feapder
from feapder.utils.log import log

class InsAir(feapder.AirSpider):
    def start_requests(self):
        yield feapder.Request("https://www.baidu.com")

    def parse(self, request, response):
        print(response)
        log.debug('标题: 百度一下')

    def download_midware(self, request):
        request.headers = {'User-Agent': "lalala"}
        return request

if __name__ == "__main__":
    InsAir().start()
