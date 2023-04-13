# Download the CSV file from the URL and save it to a local file
import requests

url = 'https://raw.githubusercontent.com/aakashsiv/OSS_Senior_Design/feature/API_data/20230329000001952/10.csv'
res = requests.get(url, allow_redirects=True)

with open('myCSV.csv', 'wb') as file:
    file.write(res.content)
