import datetime

from user.models import User
from social.models import Swiped


def rmcd_users(user):
    '''用户推荐'''
    # 筛选出所有被当前用户滑过的用户的 uid
    swiped = Swiped.objects.get(uid=user.id).only('sid')
    swiped_uid_list = [sw.sid for sw in swiped]
    swiped_uid_list.append(user.id)  # 排除自己

    curr_year = datetime.date.today().year  # 当前年份
    max_birth_year = curr_year - user.profile.min_dating_age
    min_birth_year = curr_year - user.profile.max_dating_age

    # 根据条件筛选 user 对象
    User.objects.filter(
        location=user.profile.location,
        sex=user.profile.dating_sex,
        birth_year__range=[min_birth_year, max_birth_year]
    ).exclude(id__in=swiped_uid_list)
    return user