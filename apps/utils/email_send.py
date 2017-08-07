# _*_ coding:utf-8 _*_
__author__ = 'long3ck'
__date__ = '2017/3/1 21:52'
from random import Random
from users.models import EmailVerifyRecord
from django.core.mail import send_mail
from MxOnline.settings import EMAIL_FROM

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhJjKkMmNnPpQqRrSsTtUuVvWwXxYyZz23456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str +=chars[random.randint(0,length)]
    return str


def send_register_email(email,send_type="register"):
    email_record = EmailVerifyRecord()
    if send_type =="update_email":
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "慕学在线网注册激活链接"
        email_body = "请点击下面的链接激活你的账号：http://192.168.1.101:8001/active/{0}".format(code)

        send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            pass

    elif send_type == "forget":
        email_title = "慕学在线网密码重置链接"
        email_body = "请点击下面的链接重置密码：http://192.168.1.101:8001/reset/{0}".format(code)

        send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            pass

    elif send_type == "update_email":
        email_title = "慕学在线网修改邮箱地址验证码"
        email_body = "您的邮箱验证码为：{0}".format(code)

        send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            pass