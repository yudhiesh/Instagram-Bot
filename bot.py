import logging
import argparse
from typing import List

from instapy import InstaPy, smart_run

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

def convert(string: str) -> List[str]:
    """
    Converts a string to a list of strings
    """
    li = list(string.split(" "))
    return li

parser = argparse.ArgumentParser()
parser.add_argument(
    "--instagram_login", action="store", help="Your instagram login", required=True
)
parser.add_argument(
    "--instagram_password",
    action="store",
    help="Your instagram password",
    required=True,
)
parser.add_argument(
    "--to_follow",
    action="store",
    help="Follow the users of this account",
    required=True,
)
parser.add_argument(
    "--amount", action="store", help="The amount of users to follow", required=True
)
args = parser.parse_args()

instagram_login = args.instagram_login
instagram_password = args.instagram_password
instagram_to_follow = convert(args.to_follow)
instagram_amount = args.amount

logging.info(f"{instagram_to_follow}")
assert isinstance(instagram_to_follow, list)


session = InstaPy(username=instagram_login, password=instagram_password)

with smart_run(session):
    session.follow_user_followers(
        usernames=instagram_to_follow, amount=instagram_amount, randomize=False
    )

