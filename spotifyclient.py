from multiprocessing.connection import wait
from pprint import pprint
import sched
import time
import urllib
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credetials

SPOTIPY_CLIENT_ID = credetials.SPOTIPY_CLIENT_ID
SPOTIPY_CLIENT_SECRET = credetials.SPOTIPY_CLIENT_SECRET
SPOTIPY_REDIRECT_URI = credetials.SPOTIPY_REDIRECT_URI
SCOPE = credetials.SCOPE
DEVICE_ID = credetials.DEVICE_ID

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                     client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE))

def internet_on():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False

# main loop
s = sched.scheduler(time.time, time.sleep)

def listener(sc):
    if internet_on() != True:
        pprint("No connection")
        sc.enter(300, 1, listener, (sc,))
    else:
        playing = sp.current_user_playing_track()
        if playing is None:
            sp.start_playback(device_id=DEVICE_ID)
            pprint("Started to play")
            sc.enter(300, 1, listener, (sc,))
        elif playing.get('is_playing') == False and playing != None:
            sp.start_playback(device_id=DEVICE_ID)
            pprint("Started to play")
            sc.enter(300, 1, listener, (sc,))
        else:
            sc.enter(300, 1, listener, (sc,))
s.enter(1, 1, listener, (s,))
s.run()
