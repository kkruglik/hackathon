# Develop a tool for finding visual duplicates for independent Russian media

The task is to develop a tool in which it will be possible to upload links to several telegram channels and / or tweeters, and after that the tool will parse video or photo materials from them and, as a result, will produce unique ones.

This will solve the problem in which the user is faced with a very large number of reposts and reuploads of materials, as a result, one can drown in this amount of repetitive information.

## project structure
### app
- `app/telegram_scraper.py` - this script allows you to scrape a Telegram channel and retrieve information about files shared in the channel. You can also choose to download the files if needed.
- `app/utils.py` - script for updating archive of existing telegram videos without duplicates

## scripts
- `./scrape_from_date.py` - a script for getting a list of videos from different telegram channels from a certain date. After scraping, all video data without duplicates is written to the `app/scraping_data/archive.csv`.
- `./scrape_channel.py` - a script for getting a list of videos from the whole channel
- `./scrape_cone_post.py` - a script for getting a one video from the channel
- `./scrape_cone_post.py` - a script for getting list of videos from differents channels

## notebooks
- `research/get-embeddings.ipynb` - notebook with exctracting video embeddings using deep learning

