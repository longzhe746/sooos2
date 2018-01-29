# -*- coding:utf-8 -*-
import xadmin
from .models import EmailverifyRecord, Banner
from xadmin.views import  BaseAdminView, CommAdminView

'''
setting for xadmin main functions
'''
class BaseSetting(object):
    enable_themes = True
    use_bootswatch =True


class GlobalSettings(object):
    site_title = 'sooos.net'
    site_footer = '速速走遍世界'
    menu_style = 'accordion'


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
xadmin.site.register(BaseAdminView,BaseSetting)
xadmin.site.register(CommAdminView,GlobalSettings)