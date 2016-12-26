#!/usr/bin/env python
# coding: utf-8

from wxbot import *

'''
  项目参考:https://github.com/liuwons/wxBot
  机器人聊天部分参考
  图灵机器人:http://www.tuling123.com
  AI: http://www.yige.ai
'''


class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        print(msg)
        print '[Text] %s' % (msg['content']['data'])
        print '[name] %s' % (msg["user"]['name'])
        print "msg_type_id:%s" % msg['msg_type_id']
        print "user:%s" % msg["user"]
        print "content:%s" % msg["content"]
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            if msg["user"]['name'] == "xxxx":
                self.send_msg_by_uid(u'不好意思，主人正在忙...... 一会给你答复(微信机器人小秘).', msg['user']['id'])
            else:
                self.send_msg_by_uid(self.queryMessgae(msg['content']['data']), msg['user']['id'])

    @staticmethod
    def queryMessgae(message=None):
        if message is None or len(message) == 0:
            print("消息为空")
        else:
            print(message)
        url = "http://www.yige.ai/v1/query"
        session = SafeSession()
        # session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5'})
        params = {
            'token': "93918E78E9AA82F61CC8F9A3F0BA690F",
            'session_id': "D389A6616BD7227C0D92F3CCC1A3867C",
            "query": message
        }
        r = session.post(url, data=params)
        if r.status_code == 200:
            return r.json()["answer"]
        else:
            return "不好意思，主人正在忙...... 一会给你答复(微信机器人小秘)."


def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'tty'
    # bot.conf['qr'] = 'png'
    bot.is_big_contact = False  # 如果确定通讯录过大，无法获取，可以直接配置，跳过检查。假如不是过大的话，这个方法可能无法获取所有的联系人
    bot.run()


if __name__ == '__main__':
    main()
