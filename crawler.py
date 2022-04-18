from Scweet.scweet import scrape
from Scweet.user import get_user_information, get_users_following, get_users_followers

data = scrape(words=[''],since="2013-1-1", until="2013-12-31",
              interval=10, headless=False, display_type="Top", 
              filter_replies=False,lang = 'de')


"""
Scrape tweets.

optional arguments:
  -h, --help            show this help message and exit
  --words WORDS         Words to search for. they should be separated by "//" : Cat//Dog.
  --from_account FROM_ACCOUNT
                        Tweets posted by "from_account" account.
  --to_account TO_ACCOUNT
                        Tweets posted in response to "to_account" account.
  --mention_account MENTION_ACCOUNT
                        Tweets that mention "mention_account" account.         
  --hashtag HASHTAG
                        Tweets containing #hashtag
  --until UNTIL         End date for search query. example : %Y-%m-%d.
  --since SINCE
                        Start date for search query. example : %Y-%m-%d.
  --interval INTERVAL   Interval days between each start date and end date for
                        search queries. example : 5.
  --lang LANG           Tweets language. Example : "en" for english and "fr"
                        for french.
  --headless HEADLESS   Headless webdrives or not. True or False
  --limit LIMIT         Limit tweets to be scraped.
  --display_type DISPLAY_TYPE
                        Display type of Twitter page : Latest or Top tweets
  --resume RESUME       Resume the last scraping. specify the csv file path.
  --proxy PROXY         Proxy server
  --proximity PROXIMITY Proximity
  --geocode GEOCODE     Geographical location coordinates to center the
                        search (), radius. No compatible with proximity
  --minreplies MINREPLIES
                        Min. number of replies to the tweet
  --minlikes MINLIKES   Min. number of likes to the tweet
  --minretweets MINRETWEETS
                        Min. number of retweets to the tweet
"""