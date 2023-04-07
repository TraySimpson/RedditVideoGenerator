# Reddit Video Generator

*This project is further explained in [this video](https://youtu.be/ZmSb3LZDdf0)*

*This code is meant only for educational reference and will not be maintained*

---
This program generates a .mp4 video automatically by querying the top post on the
r/askreddit subreddit, and grabbing several comments. To use this program:
- Install dependencies
- Register with Reddit to create and API application [here](https://www.reddit.com/prefs/apps/)
- Use the credentials from the previous step to update reddit.py line 46-51
- Make a copy of config.example.ini and rename to config.ini

Now, you can run `python main.py` to be prompted for which post to choose. Alternatively,
you can run `python main.py <reddit-post-id>` to create a video for a specific post.
