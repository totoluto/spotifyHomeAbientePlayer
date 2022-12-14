import time
import urllib
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credetials

#Configs
SPOTIPY_CLIENT_ID = credetials.SPOTIPY_CLIENT_ID
SPOTIPY_CLIENT_SECRET = credetials.SPOTIPY_CLIENT_SECRET
SPOTIPY_REDIRECT_URI = credetials.SPOTIPY_REDIRECT_URI
SCOPE = credetials.SCOPE
DEVICE_ID = credetials.DEVICE_ID
PLY_URI = credetials.PLY_URI

#Spotify definition of authentication
spfy = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                     client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE))

def internet_on():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False

start_time = '09:00:00'
end_time = '20:00:00'
start_time = time.strptime(start_time, '%H:%M:%S')
end_time = time.strptime(end_time, '%H:%M:%S')


# main loop
while True:
    if not internet_on():
        print("No connection")
    else:
        now = time.localtime()
        playing = spfy.current_user_playing_track()
        if playing is None or (playing.get('is_playing') == False and playing != None):
            spfy.start_playback(device_id=DEVICE_ID, context_uri=PLY_URI)
            print("Started to play")
        if start_time <= now <= end_time:
            spfy.volume(100, device_id=DEVICE_ID)
        else:
            spfy.volume(0, device_id=DEVICE_ID)
    time.sleep(300)
