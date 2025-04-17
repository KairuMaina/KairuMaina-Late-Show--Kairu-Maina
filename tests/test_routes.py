import pytest
from app import create_app, db
from app.models import Episode


@pytest.fixture
def app():
    app = create_app('testing')  # Create app in testing mode
    with app.app_context():
        db.create_all()  # Create tables in the test database
    yield app
    with app.app_context():
        db.drop_all()  # Drop tables after tests

@pytest.fixture
def client(app):
    return app.test_client()

# Test the GET /episodes route
def test_get_episodes(client):
    response = client.get('/episodes')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)  # Should return a list of episodes
    assert all('id' in episode for episode in data)  # Each episode should have an 'id' field
    assert all('date' in episode for episode in data)  # Each episode should have a 'date' field
    assert all('number' in episode for episode in data)  # Each episode should have a 'number' field

# Test the GET /episodes/:id route
def test_get_episode_by_id(client):
    response = client.get('/episodes/1')
    data = response.get_json()

    if response.status_code == 200:
        assert 'id' in data
        assert 'date' in data
        assert 'number' in data
        assert 'appearances' in data
    elif response.status_code == 404:
        assert 'error' in data
        assert data['error'] == 'Episode not found'

# Test the GET /guests route
def test_get_guests(client):
    response = client.get('/guests')
    data = response.get_json()
    assert response.status_code == 200
    assert isinstance(data, list)  # Should return a list of guests
    assert all('id' in guest for guest in data)  # Each guest should have an 'id' field
    assert all('name' in guest for guest in data)  # Each guest should have a 'name' field
    assert all('occupation' in guest for guest in data)  # Each guest should have an 'occupation' field

# Test the POST /appearances route
def test_create_appearance(client):
    data = {
        "rating": 5,
        "episode_id": 1,
        "guest_id": 2
    }

    response = client.post('/appearances', json=data)
    data = response.get_json()

    if response.status_code == 201:
        assert 'id' in data
        assert 'rating' in data
        assert data['rating'] == 5
        assert 'guest' in data
        assert 'episode' in data
    else:
        assert 'errors' in data
        assert 'validation errors' in data['errors']

# Test invalid rating
def test_invalid_rating(client):
    data = {
        "rating": 6,  # Invalid rating
        "episode_id": 1,
        "guest_id": 2
    }

    response = client.post('/appearances', json=data)
    data = response.get_json()

    assert response.status_code == 400
    assert 'errors' in data
    assert 'rating must be between 1 and 5' in data['errors']
