from random import randrange

import requests

from swiper import config


def gen_vcode(length=4):
    '''生成一个验证码'''
    start = 10 ** (length - 1)
    end = 10 ** length
    return str(randrange(start, end))


def send_sms(phonenum, vcode):
    '''发送手机验证码'''
    params = config.YZX_SMS_PARAMS.copy()
    params['mobile'] = phonenum
    params['param'] = gen_vcode()
    resp = requests.post(config.YZX_SMS_API, json=params)
    if resp.status_code == 200:
        result = resp.json()
        if result['code'] == '000000':
            return True, result['msg']
        else:
            return False,result['msg']
    else:
        return False,'短信服务器错误'
