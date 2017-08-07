# _*_ coding:utf-8 _*_
__author__ = 'long3ck'
__date__ = '2017/1/10 0:08'

import  xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from django.db import models
from xadmin.layout import Fieldset,Main,Side,Row
from django.utils.translation import ugettext as _
from .models import UserProfile,EmailVerifyRecord,Banner

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView,BaseSetting)


class GlobalSettings(object):
    site_title = '天堂有路你不走，学海无涯苦作舟'
    site_footer = '慕学在线'
    menu_style = 'accordion'
xadmin.site.register(views.CommAdminView,GlobalSettings)


class BannerAdmin(object):
    list_display = ['title','url','index','image','add_time',]
    search_fields = ['title','url','index',]
    list_filter = ['title','url','index','add_time',]
xadmin.site.register(Banner,BannerAdmin)


class UserProfileAdmin(UserAdmin):
    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'username', 'password',
                             css_class='unsort no_title'
                             ),
                    Fieldset(_('Personal info'),
                             Row('first_name', 'last_name'),
                             'email'
                             ),
                    Fieldset(_('Permissions'),
                             'groups', 'user_permissions'
                             ),
                    Fieldset(_('Important dates'),
                             'last_login', 'date_joined'
                             ),
                ),
                Side(
                    Fieldset(_('Status'),
                             'is_active', 'is_staff', 'is_superuser',
                             ),
                )
            )
        return super(UserAdmin, self).get_form_layout()

    list_display = [
        'username','mobile', 'email','nick_name',
        'last_name','first_name', 'gender','birthday',
        'is_superuser','is_staff','is_active','image',
        'date_joined','address','last_login',
    ]
    search_fields = ['username','mobile', 'email', 'last_name','first_name','nick_name',]
    list_filter = ['username','mobile', 'email','nick_name','is_superuser','is_staff','is_active','date_joined',]


# from django.contrib.auth.models import User
# xadmin.site.unregister(User)
# xadmin.site.register(UserProfile,UserProfileAdmin)



class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time',]
    search_fields= ['email','send_type',]
    list_filter = ['email','send_type','send_time',]
    model_icon = 'fa fa-address-book-o'

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)


