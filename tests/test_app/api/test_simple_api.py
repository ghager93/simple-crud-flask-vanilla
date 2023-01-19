import flask

from app.api import simple_api
from app.models import Simple


valid_payload = {
    "name": "a name",
    "number": 1324,
}
invalid_payload = {"not string": "invalid"}

valid_payloads = [{"name": str(i), "number": i} for i in range(3)]


def _pop_datetimes(payload):
    if type(payload) == dict:  
        payload.pop("created_at", "")
        payload.pop("updated_at", "")  
    if type(payload) == list:
        for p in payload:
            p.pop("created_at", "")
            p.pop("updated_at", "")
    return payload



def test_hello_world(app: flask.Flask):
    """Test hello world endpoint returns correctly."""
    result = simple_api.hello_world()

    assert result == "hello world!"


def test_post_no_assert(mocked_db_app: flask.Flask):
    """Test endpoint handles post request. No assert."""

    with mocked_db_app.test_request_context("api/simple", method="POST", json={}):
        result = simple_api.SimpleAPI(Simple).post()


def test_post_request_no_assert(mocked_db_app: flask.Flask):
    """Test actual request. No assert."""
    result = mocked_db_app.post("/simple")


def test_post_valid_payload_2xx_status(mocked_db_client):
    result = mocked_db_client.post("/simple/", json=valid_payload)

    assert 200 <= result.status_code < 300


def test_post_valid_save_to_db(mocked_db_client):
    mocked_db_client.post("/simple/", json=valid_payload)

    result = mocked_db_client.get("/simple/")

    assert _pop_datetimes(result.json[0]) == valid_payload


def test_post_invalid_4xx_status(mocked_db_client):
    result = mocked_db_client.post("/simple/", json=invalid_payload)
    
    assert 400 <= result.status_code < 500


def test_post_invalid_not_saved_to_db(mocked_db_client):
    mocked_db_client.post("/simple/", json=invalid_payload)
    result = mocked_db_client.get("/simple/")

    assert result.json == []


def test_get_all_2xx_status(mocked_db_client):
    result = mocked_db_client.get("/simple/")

    assert 200 <= result.status_code < 300


def test_get_all_empty_return(mocked_db_client):
    result = mocked_db_client.get("/simple/")

    assert result.json == []


def test_get_all_one_return(mocked_db_client):
    mocked_db_client.post("/simple/", json=valid_payload)

    result = mocked_db_client.get("/simple/")

    assert _pop_datetimes(result.json) == [valid_payload]


def test_get_all_three_return(mocked_db_client):
    [mocked_db_client.post("/simple/", json=valid_payloads[i]) for i in range(3)]

    result = mocked_db_client.get("/simple/")

    assert sorted(_pop_datetimes(result.json), key=lambda x: x["name"]) == sorted(valid_payloads, key=lambda x: x["name"])


def test_get_valid_id_2xx_status(mocked_db_client):
    mocked_db_client.post("/simple/", json=valid_payload)

    result = mocked_db_client.get("/simple/1")

    assert 200 <= result.status_code < 300


def test_get_invalid_id_404_status(mocked_db_client):
    mocked_db_client.post("/simple/", json=valid_payload)

    result = mocked_db_client.get("/simple/2")

    assert result.status_code == 404


def test_get_valid_id(mocked_db_client):
    mocked_db_client.post("/simple/", json=valid_payload)

    result = mocked_db_client.get("/simple/1")

    assert _pop_datetimes(result.json) == valid_payload
