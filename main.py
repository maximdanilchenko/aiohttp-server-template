import asyncio
import warnings

import yaml
from aiohttp import web

# Try to use uvloop if its possible
try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    warnings.warn('Could not import uvloop. Using custom asyncio loop..')

from app import create_app

with open('config.yaml', 'rb') as f:
    config = yaml.load(f)

application = create_app(config)

if __name__ == "__main__":
    web.run_app(application, host='localhost', port=1000)
    # Or with gunicorn:
    # > gunicorn -c gunicorn.conf.py -b 1000 main:app
