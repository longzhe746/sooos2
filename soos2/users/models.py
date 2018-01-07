# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nike_name = models.CharField(max_length=50,verbose_name='昵称',default='')
    birthday = models.DateField(verbose_name='生日',null=True,blank=True)
    gender = models.CharField(max_length=10,choices=(('male','男'),('female','女')),default='female',verbose_name='性别')
    address = models.CharField(max_length=100,default='',verbose_name='地址')
    mobile = models.CharField(max_length=11,null=True,blank=True,verbose_name='手机号')
    image = models.ImageField(upload_to='image/%Y/%m',default='image/default.png',max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class EmailverifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name='验证码')
    email = models.EmailField(max_length=50,verbose_name='邮箱')
    send_type = models.CharField(choices=(('register','注册'),('forget','找回密码')),max_length=10)
    send_time = models.DateTimeField