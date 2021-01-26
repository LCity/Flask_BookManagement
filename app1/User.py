from flask import Blueprint, render_template, redirect,request,flash
from app1 import db
from .models import User
user = Blueprint('User',__name__)

@user.route('/index')
def index():
    return render_template('User/index.html')

@user.route('/add/',methods=['GET','POST'])
def add():
    if request.method == 'POST':
        p_book = request.form.get('bookName',None)
        p_user= request.form.get('readerName',None)
        p_id= request.form.get('id',None)
        p_bookState=request.form.get('states',None)
        users = User.query.all()
        if not p_book or not p_user or not p_id:
            flash('输入不能为空')
            return render_template('User/add.html', users=users)
        user_all_list = db.session.query(User).filter(User.id == p_id).all()
        if len(user_all_list)==0 :
            if p_bookState =="Return":
                flash("图书在馆内，不需要归还")
                return render_template('User/add.html', users=users)
            newobj = User( bookTitle=p_book,id=p_id,bookState=p_bookState,readerName=p_user)
            db.session.add(newobj)
            db.session.commit()
        else:
            for u in user_all_list:
                if u.bookState =="Borrow" and p_bookState == "Borrow":
                    flash("图书已经借出")
                    return render_template('User/add.html', users=users)
                if u.bookState == "Return" and p_bookState == "Return":
                    flash("图书在馆内，不需要归还")
                    return render_template('User/add.html', users=users)
                db.session.query(User).filter(User.id == p_id).update({"bookState":p_bookState})
                db.session.commit()
        users = User.query.all()
        return render_template('User/add.html',users=users)

    users = User.query.all()
    return render_template('User/add.html',users=users)

@user.route('/delete',methods=['POST'])
def delete():
    if request.method == 'POST':
        # 1.查询书籍并拿数据
        book_name= request.form.get('bookId',None)
        bookobj = User.query.get(book_name)
        try:
            db.session.delete(bookobj)
            db.session.commit()
        except Exception as e:
            flash("删除错误!")
            db.session.rollback()
        # redirect重定向回到根路径, redirect接收路由地址参数, 或者直接接收网址参数(http://xxxxx.com)
        # url_for("index"): 需要传入视图函数名, 返回该视图函数对应的路由地址(url)
        users = User.query.all()
        return render_template('User/add.html',users=users)

@user.route('/show')
def show():
    return 'Book_show'
