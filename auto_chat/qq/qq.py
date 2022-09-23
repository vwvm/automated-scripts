from qqbot import _bot as bot


def atest():
    # 登录QQ
    bot.Login(['-q', '1647010108'])

    '''
    buddy 获取指定名称/备注的好友
    group 获取群  看个人简介获取资料
    '''
    buddy = bot.List('buddy', 'b.K')

    # 判断是佛存在这个好友
    if buddy:
        b = buddy[0]
        # 发送消息
        bot.SendTo(b, '你好！')


if __name__ == "__main__":
   atest()
