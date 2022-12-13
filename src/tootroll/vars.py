import os
import re

MODULE_NAME = __name__.split(".", 1)[0]

try:
    TOOTROLL_HOME = os.environ["TOOTROLL_HOME"]
except KeyError:
    TOOTROLL_HOME = f'{os.environ.get("HOME", ".")}/.{MODULE_NAME}'

SECRETS_DIR = f"{TOOTROLL_HOME}/.secrets"
DATABASE_DIR = f"{TOOTROLL_HOME}/data"
DEFAULT_SERVERS = [
    "mastodon.cloud",
    "mastodon.online",
    "fosstodon.org",
]


def extract_hostname(url: str) -> str:
    return re.sub(".*://|:.*|/.*", "", url)
