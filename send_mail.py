import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    subject, from_email, to = '来自www.liujiangblog.com的测试邮件', '***@163.com', '***@qq.com'
    text_content = '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！'
    html_content = '<p>欢迎访问<a href="http://www.liujiangblog.com" target=blank>www.liujiangblog.com</a>，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

'''
测试邮件的脚本
import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    send_mail(
        '来自www.liujiangblog.com的测试邮件',
        '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，本站专注于Python和Django技术的分享！',
        'xxx@sina.com',
        ['xxx@qq.com'],
    )
'''