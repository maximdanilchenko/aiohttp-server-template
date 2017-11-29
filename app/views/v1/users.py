from aiohttp import web


async def get_users(request: web.Request) -> web.Response:
    """
    ---
    summary: Get users
    description: Description
    tags:
    - users
    produces:
    - json
    responses:
        "200":
            description: Success
    """
    return web.Response()


async def get_user(request: web.Request) -> web.Response:
    """
    ---
    summary: Get user
    description: Description
    tags:
    - users
    produces:
    - json
    responses:
        "200":
            description: Success
    """
    user_id = request.match_info['user_id']
    return web.Response()


async def add_user(request: web.Request) -> web.Response:
    """
    ---
    summary: Add user
    description: Description
    tags:
    - users
    produces:
    - json
    responses:
        "200":
            description: Success
    """
    return web.Response()


async def delete_user(request: web.Request) -> web.Response:
    """
    ---
    summary: Delete user
    description: Description
    tags:
    - users
    produces:
    - json
    responses:
        "200":
            description: Success
    """
    user_id = request.match_info['user_id']
    return web.Response()
