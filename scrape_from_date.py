"""Scrape messages from a channel from a given date"""
import datetime
import pandas as pd
import os
import logging

# local imports
from app.telegram_scraper import scrape_channel
from app.utils import update_archive

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

# specify a date
date = "2023-05-15"
start_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

# or use yesterday's date
# start_date = (datetime.datetime.now() - datetime.timedelta(days=1)).date()
# date = start_date.strftime("%Y-%m-%d")

channels = ["creamy_caprice", "DeepStateUA"]  # add more channels here
download = False

# create app here https://my.telegram.org/apps and add variables
api_id = ""
api_hash = ""
username = ""

df = pd.DataFrame()
if not os.path.exists(f"app/scraped_data/{date}"):
    os.mkdir(f"app/scraped_data/{date}")

for ch in channels:
    logging.info(f"Scraping {ch} till date {date} \n")
    file_data = scrape_channel(
        username=username,
        api_id=api_id,
        api_hash=api_hash,
        channel=ch,
        start_date=start_date,
        download=download,
    )
    if file_data:
        df = pd.concat([df, pd.DataFrame(file_data)])

if df.empty:
    print("No data scraped")

else:
    df["message_date"] = pd.to_datetime(df["message_date"])
    df = df.sort_values(by=["message_date"])
    df = df.drop_duplicates(
        subset=["file_size", "duration", "width", "height"], keep="first"
    ).reset_index(drop=True)
    df.to_csv(f"app/scraped_data/{date}/{date}.csv", index=False)

    # update archive
    update_archive(df)
