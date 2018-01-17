# -*- coding:utf-8 -*-
import xadmin
from .models import EmailverifyRecord, Banner


class EmailverifyRecordAdmin(object):

    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type' ]
    list_filter = ['code','email','send_type','send_time']


class BannerAdmin(object):

    list_display = ['title','image','url','index','add_time']
    search_fields = ['title','image','url','index']
    list_filter = ['title','image','url','index','add_time']



xadmin.site.register(EmailverifyRecord,EmailverifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)