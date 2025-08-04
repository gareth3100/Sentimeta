import praw
from dotenv import load_dotenv
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor
from models.discussions import Discussion 


load_dotenv()

executor = ThreadPoolExecutor()

async def getDiscussionsAsync():
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(executor, getDiscussions)
    return result

def getDiscussions():
    postData = []
    
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
    )

    for submission in reddit.subreddit("TeamfightTactics").hot(limit=10):
        if "Augment Discussion" in submission.title:
            submission.comments.replace_more(limit=0)
            title = submission.title
            selftext = submission.selftext
            topComments = [comment.body for comment in submission.comments if comment.body not in ['[deleted]', '[removed]']]
            discussion =  Discussion(title=title, selftext=selftext, topComments=topComments)
            postData.append(discussion)
    
    return postData


    
        