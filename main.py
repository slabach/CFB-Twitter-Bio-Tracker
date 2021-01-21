import tweepy
import time, sys, requests, json


with open("config.json", "r") as c:
    config = json.load(c)

tw_api_secret = requests.get(f'{config['base-url']}/{config['tw-sec']}', headers={'token': config['api-key']}).text
tw_api_token = requests.get(f'{config['base-url']}/{config['tw=tok']}', headers={'token': config['api-key']}).text
tw_consumer_key = requests.get(f'{config['base-url']}/{config['con-key']}', headers={'token': config['api-key']}).text
tw_consumer_sec = requests.get(f'{config['base-url']}/{config['con-sec']}', headers={'token': config['api-key']}).text

tw_api_secret_j = json.loads(tw_api_secret)
tw_api_token_j = json.loads(tw_api_token)
tw_consumer_key_j = json.loads(tw_consumer_key)
tw_consumer_sec_j = json.loads(tw_consumer_sec)

api_secret = tw_api_secret_j['value']
api_token = tw_api_token_j['value']
consumer_key = tw_consumer_key_j['value']
consumer_secret = tw_consumer_sec_j['value']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(api_token, api_secret)
api = tweepy.API(auth)

myself = config['user']
my_ins = api.get_user(myself)
counter = 0
max_rep = int(sys.argv[1])
print(f"Cycles to run: {max_rep}")
# api.send_direct_message(my_ins.id, 'test')

twthandle = config['handles']
bio = []
for i in range(len(twthandle)):
    user = api.get_user(twthandle[i])
    bio.append(user.description)
    msg = f'START: {twthandle[i]}\n\n{user.description}'
    # print(msg)
    # api.send_direct_message(my_ins.id, msg)

# 12 per hr
while counter < max_rep:
    for i in range(len(twthandle)):
        user = api.get_user(twthandle[i])
        b = user.description
        if bio[i] != b:
            msg = f"CHANGE:\n\n@{twthandle[i]} changed their Twitter Bio from: '{bio[i]}' to '{b}'."
            api.send_direct_message(my_ins.id, msg)
            bio[i] = b
            print(msg)
    time.sleep(300)
    counter = counter + 1
    # print(f"")

print(f"{max_rep + 1} cycles completed")
