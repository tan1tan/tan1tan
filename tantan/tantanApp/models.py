from django.db import models

# Create your models here.
'''
phonenum
nickname(昵称)
sex
birth_year
birth_month
birth_day
avatar(个人形象)
location
'''



class User(models.Model):
    nickname = models.CharField(max_length=20)
    phonenum = models.IntegerField(max_length=11)
    sex = models.BooleanField()
    birth_year = models.IntegerField(max_length=4)
    birth_month = models.IntegerField(max_length=2)
    birth_day = models.IntegerField(max_length=2)
    avatar = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = "users"