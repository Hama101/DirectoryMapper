
# load environment variables from .env file
from dotenv import load_dotenv
import os
from typing import (
    Tuple,
)

load_dotenv()


DOWNLOADS_DIR : str = os.getenv("DOWNLOADS_DIR")

# dirs
ZIP_DIR : str = os.getenv("ZIP_DIR")
IMAGES_DIR : str = os.getenv("IMAGES_DIR")
VIDEOS_DIR : str = os.getenv("VIDEOS_DIR")
AUDIO_DIR : str = os.getenv("AUDIO_DIR")
EXE_DIR : str = os.getenv("EXE_DIR")
PDF_DIR : str = os.getenv("PDF_DIR")
XLXS_DIR : str = os.getenv("XLXS_DIR")
DOC_DIR : str = os.getenv("DOC_DIR")
JSON_DIR : str = os.getenv("JSON_DIR")
OTHERS_DIR : str = os.getenv("OTHERS_DIR")

# extensions
ZIP_EXTENSTIONS : Tuple[str] = tuple(os.getenv("ZIP_EXTENSTIONS").split(","))
IMAGE_EXTENSTIONS : Tuple[str] = tuple(os.getenv("IMAGE_EXTENSTIONS").split(","))
VIDEO_EXTENSTIONS : Tuple[str] = tuple(os.getenv("VIDEO_EXTENSTIONS").split(","))
AUDIO_EXTENSTIONS : Tuple[str] = tuple(os.getenv("AUDIO_EXTENSTIONS").split(","))
EXE_EXTENSTIONS : Tuple[str] = tuple(os.getenv("EXE_EXTENSTIONS").split(","))
PDF_EXTENSTIONS : Tuple[str] = tuple(os.getenv("PDF_EXTENSTIONS").split(","))
XLXS_EXTENSTIONS : Tuple[str] = tuple(os.getenv("XLXS_EXTENSTIONS").split(","))
DOC_EXTENSTIONS : Tuple[str] = tuple(os.getenv("DOC_EXTENSTIONS").split(","))
JSON_EXTENSTIONS : Tuple[str] = tuple(os.getenv("JSON_EXTENSTIONS").split(","))

# sleep time
SLEEP_TIME : int = int(os.getenv("SLEEP_TIME"))


# safe call decorator
def safe_call(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"\033[91m{e}\033[0m")
    return wrapper

if __name__ == "__main__":
    print(DOWNLOADS_DIR)
    print(ZIP_DIR)
    print(IMAGES_DIR)
    print(VIDEOS_DIR)
    print(AUDIO_DIR)
    print(EXE_DIR)
    print(PDF_DIR)
    print(OTHERS_DIR)
    print(ZIP_EXTENSTIONS)
    print(IMAGE_EXTENSTIONS)
    print(VIDEO_EXTENSTIONS)
    print(AUDIO_EXTENSTIONS)
    print(EXE_EXTENSTIONS)
    print(PDF_EXTENSTIONS)
    print(SLEEP_TIME)