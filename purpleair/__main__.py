from purpleair.downloader import download_sensor_list

print("Start Downloading")
location = download_sensor_list("kr")
print(f"Downloaded to {location}")
