import pandas as pd

def update_archive(new_data: pd.DataFrame) -> None:
    """
    Updates the archive with new data by removing duplicates and saving the updated archive to a CSV file.
    Args:
        new_data (pandas.DataFrame): The new data to be added to the archive.
    Returns:
        None.
    """
    archive = pd.read_csv("app/scraped_data/archive.csv", parse_dates=['message_date'])
    # Columns used to identify duplicates
    duplicate_cols = ['file_size', 'duration', 'width', 'height']

    # Concatenate the existing archive with new data
    updated_archive = pd.concat([archive, new_data])

    # Sort the combined archive by message date in ascending order
    updated_archive = updated_archive.sort_values(by="message_date", ascending=True)

    # Remove duplicate rows based on the specified columns
    orig_shape = updated_archive.shape[0]
    updated_archive = updated_archive.drop_duplicates(subset=duplicate_cols, keep="first").reset_index(drop=True)
    new_shape = updated_archive.shape[0]
    print(f"Dropped {orig_shape - new_shape} duplicate rows")

    # Save the updated archive to a CSV file
    updated_archive.to_csv("app/scraped_data/archive.csv", index=False)


def get_archive_slice(start_date: str = None, end_date: str = None):
    """
    Retrieves a slice of a dataframe based on a start date and/or an end date.

    Args:
        df (pandas.DataFrame): The input dataframe.
        start_date (str or None): The start date in 'YYYY-MM-DD' format. Defaults to None.
        end_date (str or None): The end date in 'YYYY-MM-DD' format. Defaults to None.

    Returns:
        pandas.DataFrame: The sliced dataframe.
    """
    df = pd.read_csv("app/scraped_data/archive.csv",  parse_dates=['message_date'])
    if start_date and end_date:
        mask = ((df['message_date'] >= start_date) & (df['message_date'] <= end_date))
    elif start_date:
        mask = df['message_date'] >= start_date
    elif end_date:
        mask = df['message_date'] <= end_date
    else:
        raise ValueError("At least one of start_date or end_date must be provided.")
    return df.loc[mask]