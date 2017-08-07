# _*_ coding:utf-8 _*_
__author__ = 'long3ck'
__date__ = '2017/1/10 21:51'

from .models import Course,Lesson,Video,CourseResource,BannerCourse
from organization.models import CourseOrg
import xadmin


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0

class CourseAdmin(object):
    list_display = ['name','course_org','category','degree','is_banner','learn_times','students','click_nums','fav_nums','desc','detail','image','get_zj_nums','go_to','add_time',]
    search_fields = ['name','desc','detail','degree','is_banner','learn_times','students','click_nums','fav_nums',]
    list_filter = ['name','desc','detail','degree','is_banner','learn_times','students','click_nums','fav_nums',]
    #默认排序
    ordering = ['-click_nums']
    #在xadmin只读
    readonly_fields = ['fav_nums']
    list_editable = ['degree','desc']
    #不在xadmin展示
    exclude = ['click_nums']
    #关联数据
    inlines = [LessonInline,CourseResourceInline]
    #页面自动刷新，3秒或5秒可选
    refresh_times = [3,5]

    style_fields = {"detail":"ueditor"}
    import_excel = True

    def queryset(self):
        qs = super(CourseAdmin,self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        """
        新建课程时，课程所在的机构的课程数自动+1
        """
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(CourseAdmin, self).post(request, args, kwargs)

xadmin.site.register(Course,CourseAdmin)


class BannerCourseAdmin(object):
    list_display = ['name','course_org','category','degree','is_banner','learn_times','students','click_nums','fav_nums','desc','detail','image','add_time',]
    search_fields = ['name','desc','detail','degree','is_banner','learn_times','students','click_nums','fav_nums',]
    list_filter = ['name','desc','detail','degree','is_banner','learn_times','students','click_nums','fav_nums',]
    #默认排序
    ordering = ['-click_nums']
    #在xadmin只读
    readonly_fields = ['fav_nums']
    #不在xadmin展示
    exclude = ['click_nums']
    inlines = [LessonInline,CourseResourceInline]

    def queryset(self):
        qs = super(BannerCourseAdmin,self).queryset()
        qs = qs.filter(is_banner=True)
        return qs

xadmin.site.register(BannerCourse,BannerCourseAdmin)

class LessonAdmin(object):
    list_display = ['course','name','add_time']
    search_fields = ['course','name',]
    list_filter = ['course__name','name','add_time',]
xadmin.site.register(Lesson,LessonAdmin)


class VideoAdmin(object):
    list_display = ['lesson','name','add_time']
    search_fields = ['lesson','name',]
    list_filter = ['lesson__name','name','add_time',]
xadmin.site.register(Video,VideoAdmin)


class CourseResource1Admin(object):
    list_display = ['course','name','download','add_time',]
    search_fields = ['course','name','download',]
    list_filter = ['course','name','add_time',]
xadmin.site.register(CourseResource,CourseResource1Admin)
