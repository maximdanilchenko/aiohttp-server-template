

async def test_get_users(get_users):
    resp = get_users
    assert resp.status == 200
