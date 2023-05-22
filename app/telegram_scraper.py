import logging
from datetime import datetime
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaDocument
from tqdm import tqdm

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.ERROR)


def scrape_channel(
    username: str,
    api_id: str,
    api_hash: str,
    channel: str,
    start_date: datetime = None,
    end_date: datetime = None,
    message_id: int = None,
    download: bool = False,
):
    """Scrape Telegram channel and return a list of dictionaries with file data.

    Args:
        username (str): Telegram username
        api_id (int): Telegram API ID
        api_hash (str): Telegram API hash
        channel (str): Telegram channel name or ID
        start_date (datetime.datetime): Inclusive date from which to scrape messages
        message_id (int): ID of the message to start from. Default None
        download (bool): Whether to download the file or not

    Returns:
        list: List of dictionaries with file data
    """
    file_data = []
    with TelegramClient(username, api_id, api_hash) as client:
        entity = client.get_entity(channel)
        if message_id:
            messages = [client.get_messages(entity, ids=message_id)]
        else:
            messages = client.iter_messages(entity, reverse=False)

        for message in tqdm(messages):
            if message.media and isinstance(message.media, MessageMediaDocument):
                message_date = message.date.date()
                # if start_date and (start_date > message.date.date() <= end_date):
                #     break
                if start_date and message.date.date() < start_date:
                    break
                # Extract message metadata
                message_text = message.message
                message_date = message.date
                peer_id = message.peer_id.channel_id
                post_author = message.post_author

                # Extract file metadata
                document = message.media.document
                file_name = (
                    document.attributes[1].file_name if len(document.attributes) > 1 else "Unknown"
                )
                file_size = document.size
                access_hash = document.access_hash
                file_reference = document.file_reference
                date = document.date
                mime_type = document.mime_type
                duration = document.attributes[0].duration if document.attributes else None
                width = document.attributes[0].w if document.attributes else None
                height = document.attributes[0].h if document.attributes else None

                # Create a dictionary with file data
                file_info = {
                    "file_name": file_name,
                    "message_text": message_text,
                    "message_date": message_date,
                    "peer_id": peer_id,
                    "post_author": post_author,
                    "from": f"https://t.me/{channel}/{message.id}",
                    "file_size": file_size,
                    "access_hash": access_hash,
                    "file_reference": file_reference,
                    "date": date,
                    "mime_type": mime_type,
                    "duration": duration,
                    "width": width,
                    "height": height,
                }

                # Download file
                if download:
                    client.download_media(message.media)

                # Append file data to the list
                file_data.append(file_info)
    return file_data
