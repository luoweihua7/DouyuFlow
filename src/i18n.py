# -*- coding: utf-8 -*-

import os

_dics = {
    'en_US': {
        'ERR_SEARCH_TITLE': u'Nothing match',
        'ERR_SEARCH_SUBTITLE': u'Search failure, please try later.',
        'NICK_NAME': u'Anchor: ',
        'GAME_NAME': u'Game: ',
    },
    'zh_CN': {
        'ERR_SEARCH_TITLE': u'没有搜到匹配的内容',
        'ERR_SEARCH_SUBTITLE': u'查询失败，请稍后再试',
        'NICK_NAME': u'主播：',
        'GAME_NAME': u'游戏：',
    }
}

lang = _dics['zh_CN']

# local = os.popen('defaults read -g AppleLocale').read().rstrip()

# try:
#     lang = _dics[local]
# except KeyError as e:
#     lang = _dics['zh_CN']
