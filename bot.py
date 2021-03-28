from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import time

INSTA_USERNAME = ""
INSTA_PASSWORD = ""

set_workspace(path=None)


def job():
    try:
        session = InstaPy(username=INSTA_USERNAME, password=INSTA_PASSWORD).login()
        session.login()
    except Exception as error:
        print(f"Error at initializing session due to {repr(error)}")
    with smart_run(session):
        try:
            session.follow_user_followers(
                usernames=["thoughtforfoodorg"], amount=6000, randomize=False
            )
        except Exception as error:
            print(f"Error {repr(error)} at follow_user_followers")
    session.end()


if __name__ == "__main__":
    job()
