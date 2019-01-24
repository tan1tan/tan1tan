from django.db import models
from django.db.models import Q


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
    stime = models.DateTimeField(auto_now_add=True, verbose_name='滑动的时间')

    @classmethod
    def swipe(cls, flag, uid, sid):
        '''添加滑动记录'''
        return cls.objects.create(flag=flag, uid=uid, sid=sid)

    @classmethod
    def is_liked_someone(cls, uid, sid):
        '''检查是否喜欢过某人'''
        return cls.objects.filter(uid=uid, sid=sid,
                           flag__in=['like', 'superlike']).exists()

    @classmethod
    def liked_me(cls, uid):
        uid_list = []
        swiped = cls.objects.filter(sid=uid, flag__in=['like', 'superlike'])
        for swp in swiped:
            uid_list.append(swp.uid)
        return uid_list


class Friend(object):
    """好友关系表"""
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()

    @classmethod
    def make_friends(cls, uid1, uid2):
        '''创建好友关系'''
        # 为了防止重复添加对 uid 排序
        uid1, uid2 = (uid2, uid1) if uid1 > uid2 else (uid1, uid2)  # uid 排序
        return cls.objects.get_or_create(uid1=uid1, uid2=uid2)

    @classmethod
    def friends_id_list(cls, uid):
        '''获取所有好友的 uid'''
        fid_list = []
        relations = cls.objects.filter(Q(uid1=uid) | Q(uid2=uid))
        for relation in relations:
            fid = relation.uid1 if relation.uid2 == uid else relation.uid2
            fid_list.append(fid)
        return fid_list

    @classmethod
    def break_off(cls, uid1, uid2):
        '''断交'''
        uid1, uid2 = (uid2, uid1) if uid1 > uid2 else (uid1, uid2)
        cls.objects.filter(uid1=uid1, uid2=uid2).delete()







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

