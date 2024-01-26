from .exts import db
import shutil,os
# flask db init  初始化
# flask db migrate   数据迁移
# flask db upgrade   改进更新
class User(db.Model):#用户
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, comment="主键ID")
    username = db.Column(db.String(40), unique=False)
    password = db.Column(db.String(40), unique=False)
    name = db.Column(db.String(40), unique=False)
class Sub(db.Model):#订阅管理
    __tablename__ = 'sub'
    id = db.Column(db.Integer, primary_key=True, comment="主键ID")
    name = db.Column(db.String(40), unique=False) #订阅名称
    node = db.Column(db.Text, unique=False) #节点
    remarks = db.Column(db.String(40), unique=False) #备注
class Login(db.Model):#登录记录
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True, comment="主键ID")
    ip = db.Column(db.String(40), unique=False) #ip
    address = db.Column(db.Text, unique=False) #地址
    time = db.Column(db.Text, unique=False) #时间
def create_db():
    db.create_all() # 创建所有表
    # print('创建')
    if User.query.count() == 0: # 如果用户表为空
        print('初始化用户表')
        user = User(username='admin',password='21232f297a57a5a743894a0e4a801fc3',name='管理员')
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print('错误信息:'+str(e))
    def init_db(FilePath, NewFilePath):
        path = os.path.dirname(os.path.abspath(__file__))
        db_path = path + NewFilePath
        if not os.path.exists(db_path) or os.path.getsize(db_path) == 0:  # 数据文件不存在或文件等于0
            shutil.copy(path + FilePath, db_path)
    init_db('/clash.yaml', '/db/clash.yaml')
    init_db('/surge.conf', '/db/surge.conf')
def init_user_pass():
    def handle_error(e):
        db.session.rollback()
        db.session.flush()
        print('错误信息:' + str(e))

    try:
        User.query.delete()
        db.session.commit()
        print("成功清空用户表")
    except Exception as e:
        handle_error(e)
    user = User(username='admin', password='21232f297a57a5a743894a0e4a801fc3', name='管理员')
    try:
        db.session.add(user)
        db.session.commit()
        print("成功初始化账号")

    except Exception as e:
        handle_error(e)
