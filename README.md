## BTTH-so-1
# Thực hiện lấy dữ liệu thời tiết từ url sau: https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&past_days=10&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m
Yêu cầu:
+ Lấy thông tin dữ liệu các trường: latitude, longitude, time, temperature_2m, relative_humidity_2m, wind_speed_10m và lưu vào một file .csv
+ Dựa vào dữ liệu đã lấy được đó. Hãy thực hiện tính tổng các giá trị của temperature_2m, relative_humidity_2m, wind_speed_10m từ đầu đến ngày 29-04

# Bài làm:
* Lấy dữ liệu và lưu vào file csv bằng code :
~
import json
import csv

# Dữ liệu JSON
data = (dữ liệu trong url)
# Tạo danh sách các hàng dữ liệu
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

# Ghi vào file CSV
filename = 'weather_data.csv'
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['latitude', 'longitude', 'time', 'temperature_2m', 'relative_humidity_2m', 'wind_speed_10m']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(rows)

print(f"Dữ liệu đã được lưu vào file {filename}")
~

 
