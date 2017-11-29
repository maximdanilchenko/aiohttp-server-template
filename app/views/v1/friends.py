from aiohttp import web


async def get_friends(request: web.Request) -> web.Response:
    """
    ---
    summary: Get friends
    description: Description
    tags:
    - friends
    produces:
    - json
    responses:
        "200":
            description: Success
    """
    user_id = request.match_info['user_id']
    return web.Response()


async def add_friend(request: web.Request) -> web.Response:
    """
    ---
    summary: Add friend
    description: Description
    tags:
    - friends
    produces:
    - json
    responses:
        "200":
            description: Success
    """
    user_id = request.match_info['user_id']
    return web.Response()


async def get_friend(request: web.Request) -> web.Response:
    """
    ---
    summary: Get friend
    description: Description
    tags:
    - friends
    produces:
    - json
    responses:
        "200":
            description: Success
    """
    user_id = request.match_info['user_id']
    friend_id = request.match_info['friend_id']
    return web.Response()


async def delete_friend(request: web.Request) -> web.Response:
    """
    ---
    summary: Delete friend
    description: Description
    tags:
    - friends
    produces:
    - json
    responses:
        "200":
            description: Success
    """
    user_id = request.match_info['user_id']
    friend_id = request.match_info['friend_id']
    return web.Response()
