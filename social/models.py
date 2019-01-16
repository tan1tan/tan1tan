from django.db import models


class Swiped(models.Model):
    """划过的记录"""
    FLAGS = (
        ('disklike', '左滑'),
        ('like', '右滑'),
        ('superlike', '上滑')
    )

    flag = models.CharField(max_length=16, choices=FLAGS, verbose_name='滑动类型')
    uid = models.IntegerField(verbose_name='滑动者的 id')
    sid = models.IntegerField(max_length=20, verbose_name='被滑的陌生人id')

    time = models.DateTimeField.auto_now(default=True, verbose_name='滑动的时间')


# class Friend(object):
#     """匹配到的好友"""
#     uid1 =
#     uid2 =
#
#
# class VIP(models.Model):
#     '''会员'''
#     name = models.CharField(verbose_name='会员名称')
#     level =
#     price =
#
#
# class Permission(models.Model):
#     '''权限'''
#     name =
#     description =

