import pytest

@pytest.fixture
def test_client():
    """ Create a test client of our app.
        This will probably be depracted in favor of client_with_redis fixture.
    """
    from sqllearning.app import create_app

    app = create_app()
    app.testing = True
    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()

@pytest.fixture
def mocked_session(mocker):
    """ Creates mock session
    """
    from sqllearning.app.api import database, models
    session = database.create_session('sqlite://')

    # Create all tables
    models.Base.metadata.create_all(session.get_bind())

    create_session_mock = mocker.patch('sqllearning.app.api.database.create_session')
    create_session_mock.return_value = session
    yield session