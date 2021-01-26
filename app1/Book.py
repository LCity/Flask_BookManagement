from flask import Blueprint, render_template, redirect,request,flash
from app1 import db
from .models import Book,bookType
book = Blueprint('Book',__name__)

@book.route('/index')
def index():
    return render_template('Book/index.html')

@book.route('/add/',methods=['GET','POST'])
def add():
    if request.method == 'POST':
        p_book = request.form.get('bookName',None)
        p_author= request.form.get('author',None)
        p_describe= request.form.get('describe',None)
        p_type=request.form.get('types',None)
        print(p_type)
        booktype = bookType.query.all()
        if not p_book or not p_author:
            flash('输入不能为空')
            users = Book.query.all()
            return render_template('Book/add.html', users=users,  booktype = bookType.query.all())

        newobj = Book( bookName=p_book,  author=p_author,bookDesc=p_describe,bookTypeId=p_type)
        db.session.add(newobj)
        db.session.commit()
        users = Book.query.all()

        return render_template('Book/add.html',users=users,booktype=booktype)
    booktype = bookType.query.all()
    users = Book.query.all()
    return render_template('Book/add.html',users=users,booktype=booktype)

@book.route('/delete',methods=['POST'])
def delete():
    if request.method == 'POST':
        # 1.查询书籍并拿数据
        book_name= request.form.get('bookId',None)
        bookobj = Book.query.get(book_name)
        try:
            db.session.delete(bookobj)
            db.session.commit()
        except Exception as e:
            flash("删除错误!")
            db.session.rollback()
        # redirect重定向回到根路径, redirect接收路由地址参数, 或者直接接收网址参数(http://xxxxx.com)
        # url_for("index"): 需要传入视图函数名, 返回该视图函数对应的路由地址(url)
        users = Book.query.all()
        return render_template('Book/add.html',users=users,booktype=bookType.query.all())

@book.route('/show')
def show():
    return 'Book_show'
