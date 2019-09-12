from django.shortcuts import render, HttpResponse, redirect, reverse
from app01.models import User, Press, Book, Author
from app01 import models
from obsite import settings
import os
import datetime


# Create your views here.


def login(request):
    # 根据请求方法来做判断
    if request.method == 'POST':
        email = request.POST.get("email", None)
        pwd = request.POST.get("pwd", None)
        ret = User.objects.filter(email=email, pwd=pwd)
        if ret:
            return redirect("https://www.baidu.com")
        else:
            return render(request, 'login.html', {"msg_error": "用户名或者密码错误"})
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


def press_list(request):
    # 获取全部的出版社信息
    ret = Press.objects.all()
    return render(request, 'press_list.html', {"press_obj": ret})


def add_press(request):
    # 添加出版社信息
    # 获取用户输入的内容
    # get请求是获取页面，post请求是提交数据
    if request.method == 'POST':
        name = request.POST.get('name')
        obj = Press.objects.create(name=name)
        # 把修改保存到数据库中去
        obj.save()
        return redirect('/press_list/')

    else:
        return render(request, 'add_press.html')


def edit_press(request):
    press_id = request.GET.get('id')
    if request.method == 'POST':
        press_name = request.POST.get("name")
        press_obj = Press.objects.filter(id=press_id)[0]
        press_obj.name = press_name
        press_obj.save()
        return redirect('/press_list/')
    else:
        press = Press.objects.filter(id=press_id)
        print(press, type(press))
        return render(request, 'edit_press.html', {'press': press[0]})


def delete_press(request):
    press_id = request.GET.get("id")
    Press.objects.filter(id=press_id).delete()
    return redirect('/press_list/')


def book_list(request):
    book_obj = Book.objects.all()
    # for i in book_obj:
    #     print(i.)
    return render(request, 'book_list.html', {'book_obj': book_obj})


def add_book(request):
    if request.method == 'POST':
        press_id = request.POST.get("press_id")
        title = request.POST.get("book_name")
        Book.objects.create(title=title, press_id=press_id)
        return redirect('/book_list/')
    else:
        press = Press.objects.all()
        return render(request, 'add_book.html', {'press': press})


def edit_book(request):
    book_id = request.GET.get("id")
    if request.method == 'POST':
        print(book_id)
        press_id = request.POST.get("press_id")
        title = request.POST.get("title")
        print(Book.objects.filter(id=book_id))
        book_obj = Book.objects.filter(id=book_id)[0]
        book_obj.press_id = press_id
        book_obj.title = title
        book_obj.save()
        return redirect('/book_list/')
    else:
        print(book_id)
        book = Book.objects.filter(id=book_id)[0]
        press = Press.objects.all()
        return render(request, 'edit_book.html', {"book": book, "press": press})


def delete_book(request):
    book_id = request.GET.get("id")
    # 实际开发中，一般不会真正的删除数据，而是假删除，增加删除字段，置为true
    Book.objects.filter(id=book_id).delete()
    return render(request, 'delete_wait.html')


def author_list(request):
    author_list = Author.objects.all()

    return render(request, 'author_list.html', {'author_list': author_list})


def add_author(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        book_list = request.POST.getlist("book_id")
        print(book_list)
        author_obj = Author.objects.create(name=name)
        author_obj.books.set(book_list)
        return redirect('/author_list/')
    books = Book.objects.all()
    return render(request, 'add_author.html', {"books": books})


def delete_author(request):
    author_id = request.GET.get("id")
    Author.objects.filter(id=author_id).delete()
    return redirect('/author_list/')


def edit_author(request):
    author_id = request.GET.get("id")
    author = Author.objects.filter(id=author_id)[0]
    if request.method == 'POST':
        name = request.POST.get("name")
        book_id = request.POST.getlist("book_id")
        author.name = name
        author.save()
        author.books.set(book_id)
        return redirect('/author_list/')
    else:
        books = Book.objects.all()
        print({'author': author, 'books': books})
        return render(request, 'edit_author.html', {'author_obj': author, 'books': books})


def upload(request):
    if request.method == 'POST':
        # 使用request.FILES取文件参数
        file = request.FILES.get("file")
        file_name = file.name
        path = os.path.join(settings.BASE_DIR, file_name)
        with open(path, 'wb') as f:
            # 约定使用chunk（）
            for chunk in file.chunks():
                f.write(chunk)
        print(file.name)
    return render(request, "upload.html")


class Putongren():
    def __init__(self, name, work, body):
        self.name = name
        self.work = work
        self.body = body

    def dream(self):
        return '你的梦想是什么'


def tFilter(request):
    p = Putongren('张三', '打鱼', 'good')
    person = {'name': 'lq', 'age': 18, 'height': 2.0}
    hobby = ['java', 'js', 'python', 'php']
    filesize = 12322211111
    dr = '0123456789'
    a_html = '<img src="/static/picture/search.png"></img>'
    s2 = 'hello ! hello! How are you? I\'m fine! Thank you!'
    now = datetime.datetime.now()
    user_list = [{'name': '张三', "age": 36, "dream": "sleep"},
                 {"name": "lisi", "age": 46, "dream": "eat"},
                 {"name": "王五", "age": 18, "dream": "fly"}]
    l1 = [
        ['签到哥', '闷骚哥', '黄袍哥', '戴帽哥'],
        ['签到哥1', '闷骚哥1', '黄袍哥1', '戴帽哥1'],
        ['签到哥2', '闷骚哥', '黄袍哥', '戴帽哥'],
        ['签到哥3', '闷骚哥', '黄袍哥', '戴帽哥'],
    ]
    return render(request, 'test.html', {'person': person, 'hobby': hobby, 'putongren': p, "filesize": filesize, 'dr': dr,
                                         'now': now, 'a_html': a_html, 's2': s2, "user_list": user_list, "l1": l1})


def home(request, year, month):
    print(year, month)
    return HttpResponse("hello")


def home2(request, *args):
    print(*args)
    print(reverse('app01:h', kwargs={'year': '2018', 'month': '10'}),)  # 命名在view中的使用
    return HttpResponse("hi")


def delete(request, table, del_id):
    # 使用反射或字典去值
    table_class = getattr(models, table.capitalize())
    table_class.objects.get(id=del_id).delete()

    return redirect(reverse("app01:"+ table))













