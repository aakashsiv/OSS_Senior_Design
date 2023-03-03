import requests
import csv
import os
import sys
#make sure to install requests and csv with pip

#set up API parameters
url = "https://api.crunchbase.com/v3.1/odm-organizations"
params = {"user_key":"1d76cc2481225b7b8f41252609efa0ac"}


#Make Get request
response = requests.get(url, params=params)
data = response.json()

#get company name and location info
companies = []
for item in data["data"]["items"]:
    name = item["properties"]["name"]
    location = item["properties"].get("location", {}).get("name")
    companies.append({"name": name, "location": location})


with open("companies.csv", "w", newline="") as csvfile:
    fieldnames = ["name", "location"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for company in companies:
        writer.writerow(company)