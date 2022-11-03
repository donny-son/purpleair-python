from dataclasses import dataclass
import os
from datetime import datetime

import pandas as pd
from dotenv import load_dotenv

load_dotenv()
BASE_URL = "https://api.purpleair.com/v1"
API_KEY = os.getenv("PURPLE_AIR_READ_KEY")


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

    def to_csv(self):
        download_dir = os.path.join(os.getcwd(), ".downloads")
        os.makedirs(download_dir, exist_ok=True)
        location = os.path.join(download_dir, f"sensor_list_{self.crawl_time}.csv")
        df = self.to_dataframe()
        try:
            df.to_csv(location, index=False)
            return location
        except Exception as e:
            raise e
