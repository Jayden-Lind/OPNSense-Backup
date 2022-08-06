import sys
import requests
import datetime

if len(sys.argv) != 4:
    sys.exit("Not enough args supplied")
else:
    hostname = sys.argv[1]
    api_key = sys.argv[2]
    api_secret = sys.argv[3]

    backup = requests.get(url=f"https://{hostname}/api/backup/backup/download", verify=False, auth=(api_key, api_secret))

    with open(f"{hostname}-{datetime.datetime.now().strftime('%I_%p_%d_%m_%Y')}.xml", 'wb') as file:
        file.write(backup.content)