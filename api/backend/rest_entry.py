from flask import Flask
from users import users
from events import events
from engagement import engagement
from backLogs import backlogs
from dotenv import load_dotenv

from analytics import analytics
from systemhealth import systemhealth

import os
import logging

from backend.db_connection import init_app as init_db
from backend.simple.simple_routes import simple_routes
from backend.ngos.ngo_routes import ngos


def create_app():
    app = Flask(__name__)

    app.logger.setLevel(logging.DEBUG)
    app.logger.info('API startup')

    # Load environment variables from the .env file so they are
    # accessible via os.getenv() below.
    load_dotenv()

    # Secret key used by Flask for securely signing session cookies.
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    # Database connection settings — values come from the .env file.
    app.config["MYSQL_DATABASE_USER"] = os.getenv("DB_USER").strip()
    app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("MYSQL_ROOT_PASSWORD").strip()
    app.config["MYSQL_DATABASE_HOST"] = os.getenv("DB_HOST").strip()
    app.config["MYSQL_DATABASE_PORT"] = int(os.getenv("DB_PORT").strip())
    app.config["MYSQL_DATABASE_DB"] = os.getenv("DB_NAME").strip()

    # Register the cleanup hook for the database connection.
    app.logger.info("create_app(): initializing database connection")
    init_db(app)

    # Register the routes from each Blueprint with the app object
    # and give a url prefix to each.
    app.logger.info("create_app(): registering blueprints")
    app.register_blueprint(simple_routes)
    app.register_blueprint(ngos, url_prefix="/ngo")

    #register the flask blueprints
    app.register_blueprint(users)
    app.register_blueprint(events)
    app.register_blueprint(engagement)
    app.register_blueprint(backlogs)

    #register analytics and system health blueprints
    app.register_blueprint(analytics)
    app.register_blueprint(systemhealth)


    return app
