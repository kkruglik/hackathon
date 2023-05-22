import pandas as pd

def update_archive(new_data: pd.DataFrame):
    """
    Updates the archive with new data without duplicates
    :param new_data:
    :return:
    """
    archive = pd.read_csv("./scraped_data/archive.csv",  parse_dates=['message_date'])
    cols = ['file_size', 'duration', 'width', 'height']
    updated_archive = pd.concat([archive, new_data])
    updated_archive = updated_archive.sort_values(by="message_date", ascending=True)
    orig_shape = updated_archive.shape[0]
    updated_archive = updated_archive.drop_duplicates(subset=cols, keep="first").reset_index(drop=True)
    new_shape = updated_archive.shape[0]
    print(f"Dropped {orig_shape - new_shape} duplicate rows")
    updated_archive.to_csv("./scraped_data/archive.csv", index=False)

def get_archive_slice(date: str):
    """
    Returns a slice of the archive for a given date.
    date: str in format (YYYY-MM-DD)
    :return:
    """
    archive = pd.read_csv("./scraped_data/archive.csv",  parse_dates=['message_date'])
    mask = (archive['message_date'] >= date)
    return archive[mask]