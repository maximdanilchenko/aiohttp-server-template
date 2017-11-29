import aiohttp_debugtoolbar
from aiohttp import web
from aiohttp_swagger import setup_swagger
import logging

from .db import init_db, close_db
from .routes import setup_routes
from .middlewares import auth_middleware

DEV_ENV = 'dev'


def create_app(config: dict) -> web.Application:
    app = web.Application()
    app['config'] = config
    setup_routes(app)
    app.middlewares.extend([auth_middleware])
    setup_swagger(app, swagger_url='/v1/doc')  # Setup Swagger toolbar (access on '/v1/doc')

    if app['config']['environment'] == DEV_ENV:  # If launched in dev env:
        aiohttp_debugtoolbar.setup(app)  # Setup debug toolbar (access on '/_debugtoolbar')
        logging.basicConfig(level=logging.DEBUG)  # Set logs to DEBUG level

    # Setup db pool:
    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)
    return app
