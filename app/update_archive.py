import pandas as pd

from .archive_utils import update_archive

new_data = pd.read_csv("app/scraped_data/2023-05-21/2023-05-21.csv")

update_archive(new_data)
