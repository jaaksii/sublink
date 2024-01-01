from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
db = SQLAlchemy() #数据库
migrate = Migrate()
jwtmanager = JWTManager()
def init_exts(app):
    db.init_app(app=app)
    migrate.init_app(app=app,db=db)
    jwtmanager.init_app(app=app)
