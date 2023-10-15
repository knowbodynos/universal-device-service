import os

import imgbbpy


def get_image_url(img_filepath, expiration=60):
    imgbb_client = imgbbpy.SyncClient(os.getenv("IMGBB_API_KEY"))
    image = imgbb_client.upload(file=img_filepath, expiration=expiration)
    return image.url
