#coding=utf-8
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField
from organization.models import CourseOrg,Teacher

# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg,verbose_name='课程机构',null=True,blank=True)
    name = models.CharField(max_length=50,verbose_name='课程名')
    desc = models.CharField(max_length=300,verbose_name='课程描述')
    detail = UEditorField(verbose_name="课程详情",width=600, height=300,default="",
                          imagePath="course/ueditor/images/",
                          filePath="course/ueditor/files/",
                          )
    is_banner = models.BooleanField(default=False,verbose_name='是否轮播图')
    teacher = models.ForeignKey(Teacher,verbose_name="讲师",null=True,blank=True)
    category = models.CharField(max_length=20,default=u'后端开发',verbose_name='课程类别')
    tag = models.CharField(default="",verbose_name="课程标签",max_length=10)
    image = models.ImageField(upload_to='course/course_logo/%Y/%m',verbose_name='封面图',max_length=100)
    degree = models.CharField(choices=(('cj','初级'),('zj','中级'),('gj','高级')),max_length=2,verbose_name='课程难度')
    learn_times = models.IntegerField(default=0,verbose_name='学习时长(分钟数)')
    click_nums = models.IntegerField(default=0,verbose_name='点击数')
    fav_nums = models.IntegerField(default=0,verbose_name='收藏人数')
    students = models.IntegerField(default=0,verbose_name='学习人数')
    youneed_know = models.CharField(max_length=300,default="",verbose_name="课程描述")
    teacher_tell = models.CharField(max_length=300,default="",verbose_name="课程须知")
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '课程[不轮播]'
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        #获取课程章节数
        return self.lesson_set.all().count()
    get_zj_nums.short_description = '章节数'

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe('''<a href= "/xadmin/courses/lesson/">跳转</a>''')
    go_to.short_description = "跳转"

    def get_learn_users(self):
        #获取学习人数
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        #获取课程章节
        return self.lesson_set.all()[:5]

    def __unicode__(self):
        return self.name


class BannerCourse(Course):
    #可轮播的课程
    class Meta:
        verbose_name = '课程[轮播]'
        verbose_name_plural = verbose_name
        proxy = True

    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    course=models.ForeignKey(Course,verbose_name='课程')
    name=models.CharField(max_length=100,verbose_name='章节名')
    add_time=models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name='章节'
        verbose_name_plural=verbose_name

    def get_lesson_video(self):
        #获取章节视频
        return self.video_set.all()

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson=models.ForeignKey(Lesson,verbose_name='章节')
    name=models.CharField(max_length=100,verbose_name='视频名')
    learn_times = models.IntegerField(default=0,verbose_name='学习时长(分钟数)')
    url = models.CharField(max_length=200,verbose_name='访问地址',default='')
    add_time=models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name='视频'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course,verbose_name='课程')
    name = models.CharField(max_length=100,verbose_name='课程资源')
    download = models.FileField(upload_to='course/resource/%Y/%m',verbose_name='资源文件',max_length=100)
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name='课程资源'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name