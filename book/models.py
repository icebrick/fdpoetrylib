#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    '''图书数据模型'''

    # 索书号
    ISBN = models.CharField(max_length=50)
    # 书名
    title  = models.CharField(max_length= 100)
    # 作者
    author = models.ManyToManyField('Author')
    # 出版社
    press = models.ForeignKey('Press', blank=True, null=True, on_delete=models.SET_NULL)
    # 类别
    category = models.CharField(max_length=50)
    # 备注，允许为空
    remark = models.CharField(max_length=300, blank=True)
    # 出借状态，True为在架上，False为被借走
    state = models.BooleanField(default=True)
    # 借书人
    borrow_by = models.ForeignKey(User, blank=True, null=True)
    # 出借日期
    borrow_date = models.DateField(blank=True, null=True)
    # 应归还日期
    should_return_date = models.DateField(blank=True, null=True)
    # 豆瓣链接
    url_douban = models.URLField(blank=True)
    # 书的简介
    abstract = models.TextField(blank=True)

    def __str__(self):
        return self.title

class BorrowRecord(models.Model):
    '''图书出借记录'''
    # 出借的图书
    book = models.ForeignKey(Book)
    # 出借日期
    borrow_date = models.DateField()
    # 归还日期
    return_date = models.DateField()
    # 借书用户
    borrow_by = models.ForeignKey(User)

    def __str__(self):
        return '{}: {}'.format(self.user.username, self.book.name)

class Author(models.Model):
    '''图书作者数据模型'''

    # 作者姓名
    name = models.CharField(max_length=30)
    # 国籍
    country = models.CharField(max_length=10, blank=True)
    # 作者信息链接
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Press(models.Model):
    '''出版社数据模型'''

    # 出版社名称
    name = models.CharField(max_length=50)
    # 出版社信息链接
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    '''图书评论数据模型'''

    # 评论内容
    content = models.TextField(max_length=1000)
    # 评论发表日期时间
    pub_date = models.DateTimeField(auto_now_add=True)
    # 评论的用户名
    user = models.ForeignKey(User)
    # 评论对应的书籍
    book = models.ForeignKey(Book)

    def __str__(self):
        return '{}: {}...'.format(self.user.username, self.content[:10])

# class Category(models.Model):
#     '''图书类别'''
#
#     category = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.category
