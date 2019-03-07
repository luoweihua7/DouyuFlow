#!/usr/bin/python
#_*_ coding:UTF-8 _*_
#
# Copyright by Larify. All Rights Reserved.

import json
import urllib
import urllib2
import sys
import time
import re

from workflow import Workflow3
from i18n import lang

reload(sys)
sys.setdefaultencoding('utf-8')

def getRoomList(category):
    url = 'https://www.douyu.com/gapi/rkc/directory/%s/1?limit=20' % category
    wf.logger.debug('请求地址：%s' % url)
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request(url, headers = {'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"})
    url = opener.open(request)
    result = url.read()
    respJson = json.loads(result)
    return respJson['data']['rl']

def main(wf):
    try:
        if len(wf.args) > 0:
            category = wf.args[0]
            roomList = getRoomList(category)
            for item in roomList:
                wf.add_item(
                    title = item['rn'],
                    subtitle = lang['NICK_NAME'] + item['nn'],
                    icon = DEFAULT_ICON,
                    arg = item['rid'],
                    valid = True
                    )
            wf.send_feedback()
        else:
            wf.send_feedback()
    except:
        wf.add_item(title=lang['ERR_SEARCH_TITLE'],
                subtitle=lang['ERR_SEARCH_SUBTITLE'], icon=DEFAULT_ICON)
        wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    DEFAULT_ICON = 'icon.png'
    sys.exit(wf.run(main))
