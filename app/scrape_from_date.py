import datetime
import pandas as pd
import os
import logging

# local imports
from .telegram_scraper import scrape_channel
from .archive_utils import update_archive

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

date = "2023-05-21"  # inclusive date
till_date = datetime.datetime.strptime(date, "%Y-%m-%d").date() #.replace(tzinfo=timezone.utc)
api_id = "1562040"
api_hash = "7942e26857e5eecd993ede591b7ddf14"
username = "37127290547"
channels = ["creamy_caprice", "DeepStateUA"]  # add more channels here
download = False

df = pd.DataFrame()
if not os.path.exists(f"./scraped_data/{date}"):
    os.mkdir(f"./scraped_data/{date}")

for ch in channels:
    logging.info(f"Scraping {ch} till date {date} \n")
    file_data = scrape_channel(
        username=username,
        api_id=api_id,
        api_hash=api_hash,
        channel=ch,
        start_date=till_date,
        download=download,
    )
    if file_data:
        df = pd.concat([df, pd.DataFrame(file_data)])

if df.empty:
    print("No data scraped")

else:
    df["message_date"] = pd.to_datetime(df["message_date"])
    df = df.sort_values(by=["message_date"])
    df = df.drop_duplicates(subset=['file_size', 'duration', 'width', 'height'], keep="first").reset_index(drop=True)
    df.to_csv(f"./scraped_data/{date}/{date}.csv", index=False)

    # update archive
    update_archive(df)