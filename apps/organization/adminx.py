# _*_ coding:utf-8 _*_
__author__ = 'long3ck'
__date__ = '2017/1/10 22:33'
import xadmin
from .models import CityDict,CourseOrg,Teacher


class TeacherAdmin(object):
    list_display = ['name','gender','org','work_years','work_company','work_position','click_nums','fav_nums','points','image','add_time',]
    search_fields= ['name','gender','org','work_years','work_company','work_position','points','click_nums','fav_nums',]
    list_filter = ['name','gender','org','work_years','work_company','work_position','points','click_nums','fav_nums','add_time',]
xadmin.site.register(Teacher,TeacherAdmin)


class CityDictAdmin(object):
    list_display = ['name','add_time',]
    search_fields= ['name',]
    list_filter = ['name','add_time',]
xadmin.site.register(CityDict,CityDictAdmin)


class CourseOrgAdmin(object):
    list_display = ['name','category','tag','course_nums','students','click_nums','fav_nums','city','address','image','desc','add_time',]
    search_fields= ['name','desc','category','tag','click_nums','fav_nums','city','address','image','desc',]
    list_filter = ['name','category','tag','click_nums','fav_nums','city','address','image','add_time',]
    #外键加载时可以搜索
    relfield_style = 'fj-ajax'
xadmin.site.register(CourseOrg,CourseOrgAdmin)