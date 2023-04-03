# Reddit Video Generator

*This project is further explained in [this video](https://youtu.be/ZmSb3LZDdf0)*

*This code is meant only for educational reference and will not be maintained*

---
This program generates a .mp4 video automatically by querying the top post on the
r/askreddit subreddit, and grabbing several comments. To use this program:

1. Install dependencies
```
pip install -r requirements.txt
```

2. Register with Reddit to create an API application [here](https://www.reddit.com/prefs/apps/).

3. Update `reddit.py` with your credentials on lines 46-51.

4. Make a copy of `config.example.ini` and rename it to `config.ini`.

5. Now, you can run the program:
- To be prompted for which post to choose, run:

   ```
   python main.py
   ```

- To create a video for a specific post, run:

   ```
   python main.py <reddit-post-id>
   ```

**Note:** The `reddit-post-id` can be found in the URL of the post, e.g. for the post `https://www.reddit.com/r/AskReddit/comments/abcdef/your_post_title_here/`, the `reddit-post-id` is `abcdef`.
