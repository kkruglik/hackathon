"""Scrape one post from a channel."""
import pandas as pd
import logging

# local imports
from app.telegram_scraper import scrape_channel

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


channel = "milinfolive"
message_id = 78558

# create app here https://my.telegram.org/apps and add variables
api_id = ""
api_hash = ""
username = ""

file_data = scrape_channel(username, api_id, api_hash, channel=channel, message_id=message_id)

df = pd.DataFrame(file_data)
df.to_csv(f"app/scraped_data/{channel}_{str(message_id)}.csv", index=False)
