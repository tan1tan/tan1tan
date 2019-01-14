from django.db import models

# Create your models here.


class User(models.Model):
    SEX = (
        ('male','男性'),
        ('famale','女性')
    )
    phonenum = models.CharField(max_length=20,unique=True,verbose_name='手机号')
    nickname = models.CharField(max_length=32, unique=True,verbose_name='昵称')
    sex = models.CharField(max_length=8,choices=SEX,verbose_name='性别')
    birth_year = models.IntegerField(default=2000,verbose_name='出生年')
    birth_month = models.IntegerField(default=1,verbose_name='出生月')
    birth_day = models.IntegerField(default=1,verbose_name='出生日')
    avatar = models.ImageField(max_length=256,verbose_name='个人形象的URL')
    location = models.CharField(max_length=16,verbose_name='常居地')
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = "users"