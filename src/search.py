#!/usr/bin/python
# _*_ coding:UTF-8 _*_
#
# Copyright by Larify. All Rights Reserved.

import json
import urllib
import urllib2
import sys
import re

from workflow import Workflow3,web
from i18n import lang

reload(sys)
sys.setdefaultencoding('utf-8')

def search(searchText):
    url = 'https://capi.douyucdn.cn/api/v1/search/%s?limit=10&offset=0' % urllib.quote_plus(searchText.encode('utf-8'))
    wf.logger.debug('请求地址',url)
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request(url, headers = {'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"})
    url = opener.open(request)
    result = url.read()
    respData = json.loads(result)
    return respData['data']

def main(wf):
    try:
        if len(wf.args) > 0:
            text = wf.args[0]
            items = search(text)
            for item in items:
                wf.logger.debug('item',item)
                wf.add_item(
                    title = item['room_name'],
                    subtitle = lang['NICK_NAME'] + item['nickname'],
                    icon = DEFAULT_ICON,
                    arg = item['room_id'],
                    valid = True
                    )
            wf.send_feedback()
        else:
            wf.logger.info('argument require')
            wf.send_feedback()
    except:
        wf.logger.error('Error')
        wf.add_item(title=lang['ERR_SEARCH_TITLE'],
                    subtitle=lang['ERR_SEARCH_SUBTITLE'], icon=DEFAULT_ICON)
        wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow3()
    DEFAULT_ICON = 'icon.png'

    sys.exit(wf.run(main))
