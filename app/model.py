from .exts import db
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