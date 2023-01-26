from fastapi.testclient import TestClient

def test_hello_world(test_client: TestClient):
    """Test hello world endpoint returns correctly"""
    result = test_client.get("api/helloworld")

    assert result.status_code == 200
    assert result.json() == ["hello world!"]

