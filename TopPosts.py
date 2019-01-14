import praw

# A constantly changing reddit client, which currently:
# prints the titles of the top five NEU submissions off all time.
def main():
    reddit = praw.Reddit(client_id='8QMsNPIUah2_UQ',
                         client_secret='RkyK_Wry0uTZJ3713M_WRSqK1XE',
                         password='this_is_a_project',
                         user_agent='testscript by /u/fakebot3',
                         username='tarmander_jjju')
    r_neu = reddit.subreddit("neu")
    for submission in r_neu.top('all', limit=5):
        print(submission.title + ":", submission.url)
main()