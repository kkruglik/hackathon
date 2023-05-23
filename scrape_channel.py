"""Scrape channel"""
import pandas as pd
import logging

# local imports
from app.telegram_scraper import scrape_channel

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

api_id = "1562040"
api_hash = "7942e26857e5eecd993ede591b7ddf14"
username = "37127290547"
channels = ["creamy_caprice"]
download = False

df = pd.DataFrame()

for ch in channels:
    logging.info(f"Scraping {ch} \n")
    file_data = scrape_channel(
        username=username,
        api_id=api_id,
        api_hash=api_hash,
        channel=ch,
        download=download
    )
    if file_data:
        df = pd.concat([df, pd.DataFrame(file_data)])

if df.empty:
    print("No data scraped")

else:
    df.to_csv(f"app/scraped_data/{channels[0]}.csv", index=False)
