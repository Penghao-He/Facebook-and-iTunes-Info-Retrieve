__authors__ = 'Penghao He'
## 506 F17
## Final Project
import json
import webbrowser
import requests
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import facebook_compliance_fix
APP_ID     = '2064743460481802'
APP_SECRET = '212bc688c40af2d8cad28a47be01f84b'

# Global facebook_session variable, needed for handling FB access below
facebook_session = False

# Function to make a request to Facebook provided.
# Reference: https://requests-oauthlib.readthedocs.io/en/latest/examples/facebook.html
def makeFacebookRequest(baseURL, params = {}):
    global facebook_session
    if not facebook_session:
        # OAuth endpoints given in the Facebook API documentation
        authorization_base_url = 'https://www.facebook.com/dialog/oauth'
        token_url = 'https://graph.facebook.com/oauth/access_token'
        redirect_uri = 'https://www.programsinformationpeople.org/runestone/oauth'

        scope = ['user_posts','pages_messaging','user_managed_groups','user_status','user_likes']
        facebook = OAuth2Session(APP_ID, redirect_uri=redirect_uri, scope=scope)
        facebook_session = facebook_compliance_fix(facebook)

        authorization_url, state = facebook_session.authorization_url(authorization_base_url)
        print('Opening browser to {} for authorization'.format(authorization_url))
        webbrowser.open(authorization_url)

        redirect_response = input('Paste the full redirect URL here: ')
        facebook_session.fetch_token(token_url, client_secret=APP_SECRET, authorization_response=redirect_response.strip())

    return facebook_session.get(baseURL, params=params)

def make_one_fb_request():
    r = makeFacebookRequest('https://graph.facebook.com/863704576974900/feed',{'fields':"likes,comments,message,from,updated_time", 'limit':50})
    current_user = json.loads(r.content)
    return current_user['data']

cache_info = make_one_fb_request()

with open('stopwords', 'r') as sfin:
    stopword = [ii[:-1] for ii in sfin.readlines()]

class Post():
    def __init__(self, post_dict={}):
        if 'message' in post_dict:
            self.message = post_dict['message']
        else:
            self.message = ''
        if 'comments' in post_dict:
            self.comments = post_dict['comments']['data']
        else:
            self.comments = []
        if 'likes' in post_dict:
            self.likes = post_dict['likes']['data']
        else:
            self.likes = []
        if 'from' in post_dict:
            self.name = post_dict['from']['name']
        else:
            self.name = ''
        if 'updated_time' in post_dict:
            self.updated_time = post_dict['updated_time']
        else:
            self.updated_time = ''

    def __str__(self):
        return "Message: {}\nFrom: {}\nOn: {}".format(self.message, self.name, self.updated_time)

    def all_word(self):
        words = []
        for ii in self.message.split():
            if ii not in stopword:
                words.append(ii)
        return words

instance_list = []
for ii in cache_info:
    instance_list.append(Post(ii))

all_word = {}
for ii in instance_list:
    for word in ii.all_word():
        if word in all_word:
            all_word[word] += 1
        else:
            all_word[word] = 1
most_comword = ''
num = 0
for ii in all_word.keys():
    if all_word[ii] > num:
        num = all_word[ii]
        most_comword = ii
print("The most common word that is not a stopword: "+most_comword)

##### START OF CACHE-SPECIFIC FUNCTIONS

CACHE_FILENAME = 'SI506finalproject_cache.json'
CACHE = None

def save_cache_to_file():
    if CACHE is not None:
        f = open(CACHE_FILENAME, 'w')
        f.write(json.dumps(CACHE))
        f.close()
        print('Saved cache to', CACHE_FILENAME)

def load_cache_from_file():
    global CACHE
    try:
        f = open(CACHE_FILENAME, 'r')
        CACHE = json.loads(f.read())
        f.close()
        print('Loaded cache from', CACHE_FILENAME)
    except:
        # Cache file does not exist, initialize an empty cache
        CACHE = {}
        save_cache_to_file()

def construct_cache_key(name, mtype):
    return '#'.join(name.split()) + '_' + mtype

### END OF CACHE-SPECIFIC FUNCTIONS

def get_from_itunes(name, mtype="song"):
    request_key = construct_cache_key(name, mtype)
    if request_key in CACHE:
        # The response is already present in our cache
        return CACHE[request_key]

    baseurl = "https://itunes.apple.com/search"
    parameters = {}
    parameters["term"] = name
    parameters["entity"] = mtype
    print("Making request to iTunes API...")
    response = requests.get(baseurl, params=parameters)
    python_obj = json.loads(response.text)
    final_list = []
    for item in python_obj["results"]:
        dic = {}
        dic['artist_name'] = item["artistName"]
        dic["track_title"] = item["trackName"]
        dic['track_duration'] = item["trackTimeMillis"]
        dic['collection_name'] = item["collectionName"]
        dic['country'] = item["country"]
        dic['track_url'] = item['trackViewUrl']
        final_list.append(dic)


    # Cache this response and save the cache to file
    CACHE[request_key] = final_list
    save_cache_to_file()

    return final_list

load_cache_from_file()
song_list = get_from_itunes(most_comword)

class Song:
    def __init__(self, dic):
        self.artist_name = dic['artist_name']
        self.track_title = dic['track_title']
        self.track_duration = dic['track_duration']
        self.collection_name = dic['collection_name']
        self.country = dic['country']
        self.track_url = dic['track_url']

    def __str__(self):
        return "{} (Album: {}) by {} | {} ms, in {}".format(self.track_title, self.collection_name, self.artist_name, self.track_duration, self.country)

    def show_track_url(self):
        print('Redirecting to the store page of', self.track_title)
        webbrowser.open(self.track_url)

song_instance = []
for ii in song_list:
    song_instance.append(Song(ii))

song_instance_sorted = sorted(song_instance, key = lambda x: x.track_duration)

song_instance_sorted[0].show_track_url()

with open('Song.csv', 'w') as song_out:
    song_out.write('Song title,Artist,Length,Album,Country\n')
    for ii in song_instance_sorted:
        song_out.write("{},{},{},{},{}\n".format(ii.track_title, ii.artist_name, ii.track_duration, ii.collection_name, ii.country))