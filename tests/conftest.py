import pytest
from app import create_app
import yaml

pytest_plugins = 'aiohttp.pytest_plugin'

# We can use another config for tests if needed:
with open('config.yaml', 'rb') as f:
    config = yaml.load(f)


@pytest.fixture
def cli(loop, test_client):
    app = create_app(config)
    return loop.run_until_complete(test_client(app))

