from app import create_app
from app.model import init_user_pass
app = create_app()
with app.app_context():
    init_user_pass()