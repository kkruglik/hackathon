"""Scrape one post from a channel."""
import pandas as pd
import logging

# local imports
from app.telegram_scraper import scrape_channel

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


channel = "milinfolive"
message_id = 78558
api_id = "1562040"
api_hash = "7942e26857e5eecd993ede591b7ddf14"
username = "37127290547"

file_data = scrape_channel(username, api_id, api_hash, channel=channel, message_id=message_id)

df = pd.DataFrame(file_data)
df.to_csv(f"app/scraped_data/{channel}_{str(message_id)}.csv", index=False)
