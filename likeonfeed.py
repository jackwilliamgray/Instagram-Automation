from instapy import InstaPy
from instapy import smart_run

## Like all posts on feed

# login credentials
insta_username = ''
insta_password = ''
followers = ''

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
  """ Activity flow """		
  # general settings				
  session.set_do_like(enabled=True,percentage=100)
  # activity
  session.like_by_feed(amount=100, interact=True)