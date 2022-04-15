import json
import requests

from dotenv import load_dotenv

load_dotenv()

AIO_URL = os.getenv("AIO_URL")


def get_next_color():
    try:
        response = requests.get(AIO_URL + "/colors")
        next_color = json.loads(response.content)["NEXT_COLOR"]
    except requests.exceptions.RequestException:
        next_color = "blue"
    return next_color
