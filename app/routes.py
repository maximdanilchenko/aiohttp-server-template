from aiohttp import web

from .views import v1


def setup_routes(app: web.Application):
    app.router.add_routes([
        # REST API v1
        # Friends:
        web.get('/v1/users/{user_id}/friends', v1.friends.get_friends),
        web.post('/v1/users/{user_id}/friends', v1.friends.add_friend),
        web.get('/v1/users/{user_id}/friends/{friend_id}', v1.friends.get_friend),
        web.delete('/v1/users/{user_id}/friends/{friend_id}', v1.friends.delete_friend),
        # Users:
        web.get('/v1/users', v1.users.get_users),
        web.post('/v1/users', v1.users.add_user),
        web.get('/v1/users/{user_id}', v1.users.get_user),
        web.delete('/v1/users/{user_id}', v1.users.delete_user),

        # REST API v2
        # ...
            ])
