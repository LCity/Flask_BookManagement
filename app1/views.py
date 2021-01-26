from app1 import app
from .Book import book
from .User import user
from .Admin import admin
from .Baidu_OCR import baidu_ocr

app.register_blueprint(book, url_prefix='/Flask/Book')
app.register_blueprint(user, url_prefix='/Flask/User')
app.register_blueprint(admin, url_prefix='/Flask/Admin')
app.register_blueprint(baidu_ocr, url_prefix='/Flask/OCR')
