#this gets a csv file from the github repo and downloads it locally

import requests

# URL of the CSV file
url = 'https://raw.githubusercontent.com/aakashsiv/OSS_Senior_Design/feature/API_data/20230329000001952/10.csv'

# Download the CSV file from the URL and save it locally
res = requests.get(url, allow_redirects=True)
with open('csv10.csv', 'wb') as file:
    file.write(res.content)
