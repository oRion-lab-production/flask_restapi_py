# application run

from route.admin import api_admin
from route.frontend import api_frontend
from app import application

application.register_blueprint(api_admin, url_prefix = '/api/admin')
application.register_blueprint(api_frontend, url_prefix = '/api/frontend')

if __name__ == '__main__':
    application.run()
