import tweepy
import subprocess
import time
from pathlib import Path


oauth = {}
with open("/Users/eleph/Documents/OAuth/x.txt") as f:
    for line in f:
        key, value = line.strip().split('=', 1)
        oauth[key] = value

client = tweepy.Client(
    consumer_key=oauth['API_KEY'],
    consumer_secret=oauth['API_SECRET'],
    access_token=oauth['ACCESS_TOKEN'],
    access_token_secret=oauth['ACCESS_TOKEN_SECRET']
)

try:
    me = client.get_me()
    my_id = me.data.id
    print("😻Oh my master, You're Here!")
except Exception as e:
    print("🚫Authorize Error! Check API_Key and Access_Key")
    print(f"For Detail:\n{e}")
    exit(0)

# Open Nvim and edit tweet!
now = int(time.time())
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y-%m-%d_%H%M%S", timeArray)
filedir = "/Users/eleph/Documents/Tweet/"
filename = f"{otherStyleTime}.txt"
file = filedir+filename
subprocess.run(["nvim",file])

text = ''
with open(file) as f:
    text = f.read()

if len(text) < 140:
    # Tweet Preview
    print(f"Sure to post(y/n)? This tweet is like this:\n{text}")
else:
    print("😿Damn Twitter limits your expression")
    exit(0)

toPost = input().lower()
while toPost != "y" and toPost != "n":
    print("🙃Excuse me? Enter 'y' or 'n' to confirm please")
    toPost = input().lower()
if toPost.lower() == 'y':
    try:
        client.create_tweet(text = text)
        print("😼Push Successfully! Let's experience more!")
    except Exception as e:
        print("❓Tweet Pushing Error! Check authority of App")
        print(f"For Detail:\n{e}")
        exit(0)
else:
    exit(0)
