from dataclasses import dataclass
import os
from datetime import datetime

import pandas as pd
from dotenv import load_dotenv

load_dotenv()
BASE_URL = "https://api.purpleair.com/v1"
API_KEY = os.getenv("PURPLE_AIR_READ_KEY")
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


@dataclass
class Sensor:
    index: int
    name: str
    is_indoor: int
    model: str
    latitude: float
    longitude: float


@dataclass
class SensorList:
    sensors: list[Sensor]
    crawl_time: str = datetime.now().isoformat()

    def __init__(self):
        self.sensors = []

    def add_sensor(self, sensor: Sensor):
        self.sensors.append(sensor)

    def to_dataframe(self):
        return pd.DataFrame([sensor.__dict__ for sensor in self.sensors])

    def to_csv(self, filename: str = "sensor_list_{self.crawl_time}.csv"):
        download_dir = os.path.join(os.getcwd(), ".downloads")
        os.makedirs(download_dir, exist_ok=True)
        location = os.path.join(download_dir, filename)
        df = self.to_dataframe()
        try:
            df.to_csv(location, index=False)
            return location
        except Exception as e:
            raise e
