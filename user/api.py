from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from lib.http import render_json
from lib.sms import send_sms
from common import keys
from common import errors
from user.models import User
from user.models import Profile


def submit_phone(request):
    '''提交手机号，发送验证码'''
    phone = request.POST.get('phone')
    send_sms(phone)
    return render_json(data)


def submit_vcode(request):
    '''提交短信验证码，登录'''
    phone = request.POST.get('phone')
    vcode = request.POST.get('vcode')

    cache_vcode = cache.get(keys.VCODE_KEY % phone)
    if vcode == cache_vcode:
        # 执行登录过程
        user, _ = User.objects.get_or_create(phonenum=phone, nickname=phone)

        # 在 session 中记录登录状态
        request.session['uid'] = user.id

        return render_json(user.to_dict())
    else:
        return render_json('验证码错误',errors.VCODE_ERR)


def get_profile(request):
    '''获取个人资料'''
    uid = request.session['uid']
    user = User.objects.get(id=uid)
    user.profile.to_dict()


def set_profile(request):
    '''修改个人配置'''
    form = ProfileForm(request.POST)
    if form.is_valid():
        profile = form.save(commit=False)
        


def upload_avatar(request):
    '''头像上传'''
    avatar = request.FILES.get('avatar')
    with open('medias/xxx', 'wb') as fp:
        for chunk in avatar.chunks():
            fp.write(chunk)
    return render_json(None)
