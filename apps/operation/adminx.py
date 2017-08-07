# _*_ coding:utf-8 _*_
__author__ = 'long3ck'
__date__ = '2017/1/10 22:30'

import xadmin
from .models import UserAsk,UserCourse,CourseComments,UserMessage,UserFavorite


class UserAskAdmin(object):
    list_display = ['name','mobile','course_name','add_time',]
    search_fields= ['name','mobile','course_name',]
    list_filter = ['name','mobile','course_name','add_time',]
xadmin.site.register(UserAsk,UserAskAdmin)


class UserCourseAdmin(object):
    list_display = ['user','course','add_time',]
    search_fields= ['user','course',]
    list_filter = ['user','course','add_time',]
xadmin.site.register(UserCourse,UserCourseAdmin)


class UserMessageAdmin(object):
    list_display = ['user','message','has_read','add_time',]
    search_fields= ['user','message','has_read',]
    list_filter = ['user','message','has_read','add_time',]
xadmin.site.register(UserMessage,UserMessageAdmin)


class UserFavoriteAdmin(object):
    list_display = ['user','fav_id','fav_type','add_time',]
    search_fields= ['user','fav_id','fav_type',]
    list_filter = ['user','fav_id','fav_type','add_time',]
xadmin.site.register(UserFavorite,UserFavoriteAdmin)


class CourseCommentsAdmin(object):
    list_display = ['user','course','comments','add_time',]
    search_fields= ['user','course','comments',]
    list_filter = ['user','course','comments','add_time',]
xadmin.site.register(CourseComments,CourseCommentsAdmin)