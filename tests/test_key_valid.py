from purpleair import BASE_URL, API_KEY

import httpx


def test_key_valid():
    REQ_PARAMS = {
        "api_key": API_KEY,
    }
    r = httpx.get(BASE_URL + "/keys", params=REQ_PARAMS)
    assert r.json()["api_key_type"] == "READ"
