from django.db import models

# Create your models here.


class User(models.Model):
    nickname = models.CharField(max_length=20, unique=True)  # 昵称
    phonenum = models.IntegerField(max_length=11)            # 手机号
    sex = models.BooleanField()                              # 性别
    birth_year = models.IntegerField(max_length=4)           # 出生年
    birth_month = models.IntegerField(max_length=2)          # 出生月
    birth_day = models.IntegerField(max_length=2)            # 出生日
    avatar = models.CharField(max_length=40)                 # 个人形象
    location = models.CharField(max_length=40)               # 常居地
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = "users"


class Profile(models.Model):
    location = models.CharField(max_length=200)          # 目标城市
    min_distance = models.IntegerField(max_length=20)    # 最小查找范围
    max_distance = models.IntegerField(max_length=20)    # 最大查找范围
    min_dating_age = models.IntegerField(max_length=20)  # 最小交友年龄
    max_dating_age = models.IntegerField(max_length=20)  # 最大交友年龄
    dating_sex = models.BooleanField()                   # 匹配的性别
    vibration = models.BooleanField()                    # 开启震动
    only_matche = models.BooleanField()                  # 不让未匹配的人看我的相册
    auto_play = models.BooleanField()                    # 自动播放视频

    class Meta:
        db_table = "profiles"
