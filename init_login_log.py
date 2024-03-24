from app import create_app
from app.model import init_login_log
app = create_app()
with app.app_context():
    init_login_log()