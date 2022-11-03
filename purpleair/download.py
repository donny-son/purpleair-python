import httpx

from purpleair import BASE_URL, Sensor, SensorList, API_KEY

BBOX = {
    "kr": {
        "name": "South Korea",
        "bbox": {
            "nwlng": 124.354847,
            "nwlat": 38.623477,
            "selng": 132.1467806,
            "selat": 32.9104556,
        },
    }
}


def download_sensor_list(country_abb: str) -> str:
    """Download sensor list from PurpleAir API_KEY

    Args:
        country_abb (str): Country abbreviation. e.g. 'kr'

    Returns:
        str: Location of downloaded file
    """

    REQ_PARAMS = {
        "api_key": API_KEY,
        "fields": "name,location_type,model,latitude,longitude",
        **BBOX[country_abb]["bbox"],
    }
    r = httpx.get(BASE_URL + "/sensors", params=REQ_PARAMS)

    sl = SensorList()
    if r.status_code == 200:
        data = r.json()
        for sensor in data["data"]:
            s = Sensor(*sensor)
            sl.add_sensor(s)
    return sl.to_csv()
