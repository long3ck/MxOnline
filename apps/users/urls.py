# _*_ coding:utf-8 _*_
__author__ = 'long3ck'
__date__ = '2017/7/3 21:15'

from django.conf.urls import url,include
from .views import UserinfoView,UploadImageView,UpdatePwdView,SendEmailCodeView,UpdateEmailView,MyCourseView,MyFavOrgView,MyFavTeacherView,MyFavCourseView,MymessageView

urlpatterns = [
    #个人中心-用户信息
    url(r'^info/$',UserinfoView.as_view(),name='user_info'),

    #个人中心-用户头像上传
    url(r'^image/upload/$',UploadImageView.as_view(),name='image_upoload'),

    #个人中心-用户修改密码
    url(r'^update/pwd/$',UpdatePwdView.as_view(),name='update_pwd'),

    #个人中心-发送修改邮箱验证码到
    url(r'^sendemail_code/$',SendEmailCodeView.as_view(),name='sendemail_code'),

    #个人中心-修改邮箱
    url(r'^update_email/$',UpdateEmailView.as_view(),name='update_email'),

    #个人中心-我的课程
    url(r'^mycourse/$',MyCourseView.as_view(),name='mycourse'),

    #个人中心-我收藏的课程机构
    url(r'^myfave/org/$',MyFavOrgView.as_view(),name='myfav_org'),

    #个人中心-我收藏的课程教师
    url(r'^myfave/teacher/$',MyFavTeacherView.as_view(),name='myfav_teacher'),

    #个人中心-我收藏的课程
    url(r'^myfave/course/$',MyFavCourseView.as_view(),name='myfav_course'),

    #个人中心-我的消息
    url(r'^mymessage/$',MymessageView.as_view(),name='mymessage'),
]