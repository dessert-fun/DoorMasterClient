from flask import Flask, url_for, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
import base64

app = Flask(__name__)


# 数据库配置
class Config(object):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Xbl18879445215@47.106.137.187:3306/users'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # 查询时显示SQL原语
    app.config['SQLALCHEMY_ECHO'] = True


app.config.from_object(Config)
db = SQLAlchemy(app)


# 用户数据结构
class User(db.Model):
    __tablename__ = 'user_infor'
    username = db.Column(db.String(16), primary_key=True)
    pwd = db.Column(db.String(16), unique=True)
    name = db.Column(db.String(16), unique=True)

    def __repr__(self):
        return '%s' % self.username


# 流量数据结构
class Flow(db.Model):
    __tablename__ = 'flow_infor'
    name = db.Column(db.String(16), primary_key=True)
    Mon_count = db.Column(db.Integer, nullable=True)
    Tues_count = db.Column(db.Integer, nullable=True)
    Wed_count = db.Column(db.Integer, nullable=True)
    Thur_count = db.Column(db.Integer, nullable=True)
    Fri_count = db.Column(db.Integer, nullable=True)
    Sat_count = db.Column(db.Integer, nullable=True)


# 流量操作
# 增加
@app.route('/index/add')
def Flow_contry(name, day):
    user = Flow.filter(Flow.name == name)


# 图片数据结构
class Image(db.Model):
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    image_base = db.Column(db.TEXT)


# 图片储存
@app.route('/save_image', methods=['GET', 'POST'])
def save_image():
    if request.method == 'GET':
        return render_template('contry.html')
    else:
        img = request.files.get('img')
        base64_str = base64.b64encode(img.read()).decode()
        base = Image(image_base=base64_str)
        db.session.add(base)
        db.session.commit()
        return render_template('control.html')


# 图片查询
def search_iamge():
    image_all = Image.query.all()
    temp = []
    for i in image_all:
        temp.append(i.image_base)
    return temp


@app.route('/')
def hollow():
    return redirect('login')


# 登录
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        pwd = request.form['pwd']
        try:
            user = User.query.filter(User.username == username).first()
            if user:
                return redirect('index')
            else:
                return render_template('login.html')
        except Exception:
            return render_template('login.html', msg="用户名或密码输入错误")


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/alert.html')
def alert():
    return render_template('alert.html')


@app.route('/control')
def control():
    newsList1 = [{'name': '同学A', 'num': '001', 'dates': "2018-02-09", 'id': "45211546"},
                 {'name': '同学B', 'num': '002', 'dates': '2018-06-15', 'id': "61341341"},
                 {'name': '同学C', 'num': '003', 'dates': '2018-02-19', 'id': "62451431"}]
    x = 3;
    return render_template('control.html', newsList1=newsList1, x=x)


# 添加成员及图片
# @app.route('/index/save', methods=['GET', 'POST'])
# def save_member():
#     if request.method=="GET":
#         print('get')
#     if request.method=="POST":
#         print("post")
#     name = request.form.get('name')
#     img = request.form.get('img')
#     print(name)
#     print(img)
#     return render_template('index.html')


# 添加成员及图片
@app.route('/index/save', methods=['GET', 'POST'])
def save_member():
    print("imcome")
    if request.method == 'GET':
        print("wo shi get ")
        return render_template('index.html')
    else:
        # id = request.form.get('id')
        name = request.form.get('name')
        print(name)
        img = request.files.get('img')
        print("tupian", type(img))
        # base64_str = base64.b64encode(img).decode("utf-8")
        # base = Image(d=id,name=name,image_base=base64_str)
        # db.session.add(base)
        # db.session.commit()
        return '1'


@app.route('/index/change', methods=['GET', 'POST'])
def change_member():
    # if request.method == 'GET':
    #     return render_template('index.html')
    # else:
    # id = request.form.get('id')
    id = request.form.get('id')
    name = request.form.get('name')
    img = request.files.get('img')
    print(id)
    print(name)
    print(type(img))
    return '1'


@app.route('/index/delete', methods=['GET', 'POST'])
def delete_member():
    # if request.method == 'GET':
    #     return render_template('index.html')
    # else:
    # id = request.form.get('id')
    id = request.form.get('id')

    print(id)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
