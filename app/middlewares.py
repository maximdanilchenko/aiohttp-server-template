from aiohttp import web


@web.middleware
async def auth_middleware(request: web.Request, handler) -> web.Response:
    # TODO: Some authorization checking
    return await handler(request)
