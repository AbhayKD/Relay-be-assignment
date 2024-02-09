import json


class TestHealth:
    def test_hello_world(self, client):
        response = client.get("/health_check")
        assert response.status_code == 200
        assert {"message": "All AOK!"} == json.loads(response.data)
