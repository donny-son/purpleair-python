import httpx

from purpleair import BASE_URL, Sensor, SensorList, API_KEY, BBOX


def download_sensor_list(country_abb: str) -> str:
    """Download sensor list from PurpleAir API_KEY

    Args:
        country_abb (str): Country abbreviation. e.g. 'kr'

    Returns:
        str: Location of downloaded file
    """

    r = httpx.get(
        BASE_URL + "/sensors",
        params={
            "api_key": API_KEY,
            "fields": "name,location_type,model,latitude,longitude",
            **BBOX[country_abb]["bbox"],
        },
    )

    sl = SensorList()
    if r.status_code == 200:
        data = r.json()
        for sensor in data["data"]:
            s = Sensor(*sensor)
            sl.add_sensor(s)
    return sl.to_csv(f"sensor_list_{country_abb}_{sl.crawl_time}.csv")
