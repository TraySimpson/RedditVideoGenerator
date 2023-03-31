import praw


def __getReddit():
    return praw.Reddit(

    )


reddit = __getReddit()

subreddit = reddit.subreddit("askreddit")

existingPostIds = []
posts = []

for submission in subreddit.top(time_filter="day", limit=5):
    if submission.over_18 or subreddit + submission.id + ".mp4" in existingPostIds:
        continue
    posts.append(submission)
    print(f"[{len(posts)}] {submission.title}     {submission.score}")
    if len(posts) >= 5:
        break

postSelection = int(input("Input :"))


