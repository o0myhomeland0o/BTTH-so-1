## BTTH-so-1
# Thực hiện lấy dữ liệu thời tiết từ url sau: https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&past_days=10&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m
Yêu cầu:
+ Lấy thông tin dữ liệu các trường: latitude, longitude, time, temperature_2m, relative_humidity_2m, wind_speed_10m và lưu vào một file .csv
+ Dựa vào dữ liệu đã lấy được đó. Hãy thực hiện tính tổng các giá trị của temperature_2m, relative_humidity_2m, wind_speed_10m từ đầu đến ngày 29-04

# Bài làm:
* Lấy dữ liệu và lưu vào file csv bằng code :

import json
import csv

data = (dữ liệu trong url)

rows = []
for i in range(len(data['hourly']['time'])):
    row = {
        'latitude': data['latitude'],
        'longitude': data['longitude'],
        'time': data['hourly']['time'][i],
        'temperature_2m': data['hourly']['temperature_2m'][i],
        'relative_humidity_2m': data['hourly']['relative_humidity_2m'][i],
        'wind_speed_10m': data['hourly']['wind_speed_10m'][i]
    }
    rows.append(row)

filename = 'weather_data.csv'
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['latitude', 'longitude', 'time', 'temperature_2m', 'relative_humidity_2m', 'wind_speed_10m']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Dữ liệu đã được lưu vào file {filename}")

ta sẽ được: 
![image](https://github.com/user-attachments/assets/eaf8535f-cea0-4787-9e1a-b9874ee883ce)

* Từ dữ liệu đã lấy được ta tính tổng các giá trị của temperature_2m, relative_humidity_2m, wind_speed_10m từ đầu đến ngày 29-04

import csv
from datetime import datetime

filename = 'weather_data.csv'
temperature_sum = 0.0
humidity_sum = 0
wind_speed_sum = 0.0

with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        time = datetime.strptime(row['time'], '%Y-%m-%dT%H:%M')
        if datetime(2025, 4, 19) <= time <= datetime(2025, 4, 29, 23, 59):
            temperature_sum += float(row['temperature_2m'])
            humidity_sum += int(row['relative_humidity_2m'])
            wind_speed_sum += float(row['wind_speed_10m'])

print("Tổng các giá trị từ 19-04 đến 29-04:")
print(f"Tổng temperature_2m: {temperature_sum:.2f} °C")
print(f"Tổng relative_humidity_2m: {humidity_sum} %")
print(f"Tổng wind_speed_10m: {wind_speed_sum:.2f} km/h")

ta sẽ có:
![image](https://github.com/user-attachments/assets/277fe8eb-696a-46f9-beda-c5902ecdf1bb)



 
