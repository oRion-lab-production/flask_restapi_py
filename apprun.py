# @copyright Copyright (C) 2023 UTAR Futuretech. Blockchain x Computer Science Club
# @author    Orion <chaosdevil112@gmail.com>
# @license   Proprietary

from route.admin import api_admin
from route.frontend import api_frontend
from app import application

application.register_blueprint(api_admin, url_prefix = '/api/admin')
application.register_blueprint(api_frontend, url_prefix = '/api/frontend')

if __name__ == '__main__':
    application.run()
