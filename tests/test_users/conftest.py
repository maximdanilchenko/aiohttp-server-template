import pytest


@pytest.fixture
async def get_users(cli):
    return await cli.get('/v1/users')
