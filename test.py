import pytest
import json
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_receive_message(client):
    data = {
        "game_id": "12345",
        "object_id": "548",
        "operation_id": "move",
        "args": {
            "speed": 2
        }
    }
    response = client.post('/receive_message', json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {"message": "Command received successfully"}
