from app1 import db
# db是在app/__init__.py生成的关联后的SQLAlchemy实例



class Book(db.Model):
    __tablename__ = 't_book'
    id = db.Column(db.Integer,primary_key=True)
    bookName = db.Column(db.String(80),  unique=True)
    author = db.Column(db.String(20), unique=True)
    bookDesc = db.Column(db.String(110), unique=True)
    bookTypeId =db.Column(db.Integer,unique=True)
    def __repr__(self):
        return '<User %r>' % self.bookname

class User(db.Model):
    __tablename__ = 't_reader'

    id = db.Column(db.Integer,primary_key=True)
    bookTitle = db.Column(db.String(80),  unique=True)
    readerName = db.Column(db.String(20), unique=True)
    bookState = db.Column(db.String(110), unique=True)
    def __repr__(self):
        return '<User %r>' % self.bookName

class Admin(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(20), unique=True)
    PASSWORD = db.Column(db.String(20), unique=True)

    def __repr__(self):
        return '<User %r>' % self.userName

class bookType(db.Model):
    __tablename__ = 't_bookType'
    id = db.Column(db.Integer, primary_key=True)
    bookTypeName = db.Column(db.String(20), unique=True)
    bookTypeDesc = db.Column(db.String(20), unique=True)

    def __repr__(self):
        return '<User %r>' % self.bookTypeName

class Baidu_OCR():

    userName ="Baidu_OCR"

    def __repr__(self):
        return '<User %r>' % self.userName
