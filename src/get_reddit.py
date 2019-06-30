#import The Python Reddit API Wrapper (PRAW)
import praw
import os

#pass credentials to reddit api
reddit = praw.Reddit(client_id=os.environ.get("REDDIT_ID"),
    client_secret=os.environ.get("REDDIT_SECRET"), user_agent= os.environ.get("REDDIT_USER"))

for submission in reddit.subreddit('askreddit').rising(limit=10):
    print(submission.title)
