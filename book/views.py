from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, base
import re
import xlrd

from .models import Book, Author, Comment, Press


class BookListView(ListView):

    context_object_name = 'book_list'
    template_name = 'book/book_list.html'

    # TODO: 去除结果中重复值
    def get_queryset(self):
        book_list = Book.objects.all()
        # 每页显示10篇文章
        paginator = Paginator(book_list, 20)
        page = self.kwargs.get('page', 1)

        try:
            book_paginated = paginator.page(page)
        except PageNotAnInteger:
            book_paginated = paginator.page(1)
        except EmptyPage:
            book_paginated = paginator.page(paginator.num_pages)
        return book_paginated


class BookSearchResultsView(ListView):
    context_object_name = 'book_search_results'
    template_name = 'book/book_search_results.html'

    def get_queryset(self):
        search_pattern = self.request.GET.get('search_pattern', '')
        # 0 按书名搜索; 1　按作者搜索
        search_by = self.request.GET.get('search_by', 0)
        if search_pattern:
            if search_by == '0':
                search_results = Book.objects.filter(title__contains=search_pattern)
            elif search_by == '1':
                search_results = Book.objects.filter(author__name__contains=search_pattern)
            else:
                search_results = Book.objects.none()
        else:
            search_results = Book.objects.none()
        return search_results


def add_view(requset):
    # wb = xlrd.open_workbook(filename = '../data.xlsx')
    # table = wb.sheet_by_name(u'Sheet3')
    #
    #
    # #添加作者信息到数据库
    # for i_row in range(2,924):
    #     row = table.row_values(i_row)
    #     author_list = re.split(r'[, 、]+', row[2])
    #     if author_list:
    #         for author_name in author_list:
    #             res = Author.objects.filter(name=author_name)
    #             if not res:
    #                 author = Author(name=author_name)
    #                 author.save()
    #
    # author = Author(name='匿名')
    # author.save()
    #
    # #添加出版社信息到数据库
    # for i_row in range(2,924):
    #     row = table.row_values(i_row)
    #     press_name = row[3]
    #
    #     if press_name:
    #         res = Press.objects.filter(name=press_name)
    #         if not res:
    #             press = Press(name=press_name)
    #             press.save()
    # press = Press(name='无出版社')
    # press.save()
    #
    # #添加书籍信息到数据库
    # for i_row in range(2,924):
    #     row = table.row_values(i_row)
    #     isbn = row[0]
    #     book_title = row[1]
    #     author_list = re.split(r'[, 、]+', row[2])
    #     press = row[3]
    #     #为同名的每册书分别建模
    #     if not author_list:
    #         author_list = ['匿名']
    #     if press:
    #         press_name = press
    #     else:
    #         press_name = '无出版社'
    #     book_num = int(row[4] or 1)
    #     category = row[5]
    #     remark = row[6]
    #     #调出相应的出版社信息
    #     press = Press.objects.get(name=press_name)
    #
    #     #保存书籍模型
    #     for i in range(book_num):
    #         book = Book(ISBN=isbn, title=book_title, press=press,  category=category, remark=remark)
    #         #关联ManyToManyField对象，需要先保持模型实例，再用Add方法添加
    #         book.save()
    #         for temp in author_list:
    #             author = Author.objects.get(name=temp)
    #             book.author.add(author)

    return HttpResponse('success')
