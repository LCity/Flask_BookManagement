# Flask_BookManagement
基于Flask的简单图书管理系统
# Flask项目-图书管理系统-笔记

## 环境

Python 3.7

Flask 

Mysql8.0.2

Bootstrap



>  首先解释一些形而上的东西，会方便对整体的理解

## MVC模型

- M（model）：模型，指获得数据（本项目是通过pymysql从本地数据库中获得的数据）
- V（View）：视图，将数据转换为用户能够交互和操作的图形界面，也就是我们通常使用的网页
- C（Control）：控制，使视图界面的操作和模型中的数据能够联通，也就是后台控制交互的代码



> 然后对代码构成进行一定解释

## 开始写代码（bug）

>  首先展示一下文件结构

- app1
  - templates
    - 保存的都是各个功能所对应的网页，html
  - views.py 保存路由代码
  - User.py   对图书借还数据库的增删查操作
  - Book.py  对图书信息数据库的增删查操作
  - Admin.py  对登录用户信息的操作，仅支持登录时判断密码是否正确
  - Baidu_OCR.py 对百度API调用/发送的代码
  - models.py  数据库实体到python对象的映射，定义了可以操作的数据对象（**也就是上文提到的MVC中的M**）
- config.py 保存设置的代码
- run.py  项目运行代码，运行项目时需要执行的代码，可以简单理解为启动器
- 稍微撇一眼上面内容有个印象，看完下面的部分再来看上面的部分就能够理解了



## Flask代码部分

> 首先来看一段和本项目无关的Flask代码，来理解一下flask框架大概的书写规则

```python
from flask import Flask
# 导入flask包
app = Flask(__name__)
# 将本文件的名字递给app这个已经设定好的全局变量
# 从而使Flask框架知道之后的一些资源（模板以及要加载的页面html）的位置

@app.route('/')
# 此处为设置的路由，如果访问网址后没有任何东西时，会运行此处的函数代码
# 比如说，flask测试时默认运行在http://localhost:5000，而我们访问这个url，就会运行helloworld这个函数
def hello_world():
    return 'Hello, World!'
# 函数返回 helloworld

if __name__ == '__main__':
    app.run()		#执行app.run()，进入Flask消息循环
    				#app.run()，将一直运行，其后不要写任何代码
```

- 将上面这段代码保存为run.py，然后使用python运行
- 然后在浏览器中访问http://localhost:5000，就可以看到效果
- 此处也可以设置环境变量，从而使用flask命令来运行，但我觉得有点多此一举

> 此处可以自己尝试更改代码，测试一下自己是否理解 



**当然仅仅返回一般的文字是没有用的，所以我们需要一个返回网页的方法，而flask提供了这样的方法**

```python
return render_template('Admin/index.html') 
```

- 代码解释：返回templates文件夹下的Admin文件夹下的index.html文件，也就是他所对应的网页

```python
return render_template("Admin/choose.html", adminname=p_user)
```

- 当然，你也可以向html内传输内容，而内容的显示则由html中的语句实现
  - 具体方法之后说明前端html页面的时候会进行说明

> 此处，返回的页面其实并不是单纯的html文件，而是通过render_template函数渲染好的文件，也就是说，html内部可能有需要得到传递的内容之类的。
>
> 这里的渲染应该指的是重启浏览器主线程直接重绘网页之类的
>
> *这段渲染我也有点迷，可以当作我的胡言乱语，不看也罢*





## 数据库连接部分

本项目使用的是mysql作为数据库储存数据，所以同时也选用了pymysql和sqlalchey来连接数据库和项目

1. 首先是设置mysql的连接，放在了config.py文件中，方便之后的引用

```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://mysqlusername:mysqluserpassword@sql's url/databasename?charset=utf8'
# 此处的URI是访问mysql的url，填写内容和需要替换的内容较多，下面给出示例
# 'mysql+pymysql://root（用户名称，一般为root）:123456（登录mysql时使用的代码）@localhost:3306（数据库url，此处因为是本地，所以是localhost，如果是远程服务器，也可以使用ip进行替换）/db_book(数据库名字）?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = True
```

2. 然后我们 需要将数据库内的信息映射到我们的项目文件中

```python
# app1/__init__.py
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
# 生成关联的SQLalchemy实例
```

> 使用flask内置的数据库工具，对app进行绑定

3. 下来书写对应的模型文件

```python
from app1 import db
# 引入上面关联的实例

# 书的定义
class Book(db.Model):
    __tablename__ = 't_book'
    # 对应的表的名称
    id = db.Column(db.Integer,primary_key=True)
    # id为整形（即db.Integer,并且为主键）
    # 下面的内容也可以顾名思义，unique为当前内容是否有唯一的限制
    # 前面的db都是SQLalchemy的实例名称
    bookName = db.Column(db.String(80),  unique=True)
    author = db.Column(db.String(20), unique=True)
    bookDesc = db.Column(db.String(110), unique=True)
    bookTypeId =db.Column(db.Integer,unique=True)
    def __repr__(self):
        return '<User %r>' % self.bookname
# 其他内容也就是照猫画虎
```

4. 下面是通过SQLalchemy对数据库进行的一些增删改查的操作

```

```

## 前端网页部分

> 首先建议先自学HTML基础，了解下面用到的几个标签，着重学习



> Flask文件的创建过程

- 创建app1文件
- 创建run.py 文件
- 

> 和Django的比较：因为Flask是一个更微型的框架，所以并没有提供像Django一样，通过命令行添加应用的方式，而是需要通过手动添加的方式加上所有的代码和文件





# 参考资料

[Flask和Vue.js构建全栈单页面web应用【通过Flask开发RESTful API】](https://zhuanlan.zhihu.com/p/76588212)

[Flask中文文档](https://dormousehole.readthedocs.io/en/latest/quickstart.html#id2)


