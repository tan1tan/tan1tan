from django.shortcuts import render
from django.http import JsonResponse

from lib.http import render_json
from lib.sms import send_sms

def submit_phone(request):
    '''提交手机号，发送验证码'''
    phone = request.POST.get('phone')
    send_sms(phone)
    return render_json()


def a(request):
    '''提交短信验证码，登录'''
    pass


def aa(request):
    '''获取个人资料'''
    pass


def aaa(request):
    '''修改个人资料'''
    pass


def aaaa(request):
    '''头像上传'''
    pass
