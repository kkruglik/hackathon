import pandas as pd
import logging

# local imports
from app.telegram_scraper import scrape_channel

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.ERROR)

api_id = "1562040"
api_hash = "7942e26857e5eecd993ede591b7ddf14"
username = "37127290547"
download = False

urls = pd.read_csv("archive.csv").url.to_list()
df = pd.DataFrame()

for url in urls:
    try:
        channel = url.split("https://t.me/")[1].split("/")[0]
        message_id = int(url.split("https://t.me/")[1].split("/")[1])
        file_data = scrape_channel(
            username=username,
            api_id=api_id,
            api_hash=api_hash,
            channel=channel,
            message_id=message_id,
            download=download
        )
        if file_data:
            df = pd.concat([df, pd.DataFrame(file_data)])
    except Exception as e:
        logging.error(e)

df.to_csv("app/scraped_data/archive.csv", index=False)