# > gunicorn -c gunicorn.conf.py -b 1000 main:app
workers = 1
worker_class = 'aiohttp.GunicornUVLoopWebWorker'
