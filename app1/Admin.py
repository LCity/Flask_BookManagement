from flask import Blueprint, render_template, redirect,request,flash
from app1 import db
from .models import Admin
admin = Blueprint('Admin',__name__)

@admin.route('/')
def index():
    return render_template('Admin/index.html')

@admin.route('/Log/',methods=['POST'])
def log():
	if request.method == 'POST':
		p_user = request.form.get('userName', None)
		p_pass = request.form.get('PASSWORD', None)
		print(p_user + " "+p_pass)
		if not p_user or not p_pass:
			flash("输入不能为空")
			return render_template("Admin/index.html")
		user_all_list = Admin.query.all()
		print(type(user_all_list))
		print(len(user_all_list))
		print(user_all_list)
		for u in user_all_list:
			print(type(u))
			if u.PASSWORD == p_pass and u.userName == p_user:
				flash("Load Success")
				flash("Welcome  "+ p_user)
				return render_template("Admin/choose.html", adminname=p_user)
		flash("密码错误")
		return render_template("Admin/index.html")
