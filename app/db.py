from aiohttp import web
from asyncpg import create_pool


async def init_db(app: web.Application):
    app['db'] = await create_pool(**app['config']['postgres'])


async def close_db(app: web.Application):
    app['db'].close()
    await app['db'].wait_closed()
