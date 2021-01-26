from flask import Flask
# 导入flask包
app = Flask(__name__)
# 将本文件的名字递给app这个已经设定好的全局变量
# 从而使Flask框架知道之后的一些资源（模板以及要加载的页面html）

@app.route('/')
# 此处为设置的路由，如果访问网址后没有任何东西时，会运行此处的函数代码
# 比如说，flask测试时默认运行在http://localhost:3000，而我们访问这个url，就会运行helloworld这个函数
def hello_world():
    return 'Hello, World!'
# 函数返回 helloworld

if __name__ == '__main__':
    app.run()		#执行app.run()，进入Flask消息循环
    				#app.run()，将一直运行，其后不要写任何代码