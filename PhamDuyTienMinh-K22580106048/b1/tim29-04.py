import csv
from datetime import datetime

# Đọc dữ liệu từ file CSV
filename = 'weather_data.csv'
temperature_sum = 0.0
humidity_sum = 0
wind_speed_sum = 0.0

with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Chuyển đổi thời gian
        time = datetime.strptime(row['time'], '%Y-%m-%dT%H:%M')
        
        # Kiểm tra nếu thời gian nằm trong khoảng 19-04 đến 29-04
        if datetime(2025, 4, 19) <= time <= datetime(2025, 4, 29, 23, 59):
            temperature_sum += float(row['temperature_2m'])
            humidity_sum += int(row['relative_humidity_2m'])
            wind_speed_sum += float(row['wind_speed_10m'])

# In kết quả
print("Tổng các giá trị từ 19-04 đến 29-04:")
print(f"Tổng temperature_2m: {temperature_sum:.2f} °C")
print(f"Tổng relative_humidity_2m: {humidity_sum} %")
print(f"Tổng wind_speed_10m: {wind_speed_sum:.2f} km/h")