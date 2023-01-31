# IMPORTANT: This currently does not work. However, this may give you
# an idea for how to leverage YouTubeUploader to automate this step



# from youtube_uploader_selenium import YouTubeUploader
# import json

# metaJson="metadata.json"
# tags = ["reddit", "funny", "askreddit", "best", "montage", "compilation"]
# description = """Reddit funny moments compilation from r/askreddit! 
# Be sure to subscribe for daily funny reddit posts. Check out my
# channel for more hilarious reddit clips!
# """

# def __createMetaJson(title):
#   dictionary = {
#       "title": f"{title} #shorts",
#       "description": description,
#       "tags": tags,
#   }
#   json_object = json.dumps(dictionary, indent=4)
#   with open(metaJson, "w") as outfile:
#       outfile.write(json_object)

# def uploadVideo(filePath, title):
#   __createMetaJson(title)
#   uploader = YouTubeUploader(filePath, metaJson)
#   was_video_uploaded, video_id = uploader.upload()
#   assert was_video_uploaded