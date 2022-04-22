# spotifyHomeAmbientePlayer

This is a little script i made which resumes music if not already playing. You need to make an Spotify project and add an `REDIRECT_URI` to it (it can be anything). Then you need to copy the `CLIENT_ID`, `CLIENT_SECRET` and the `REDIRECT_URI` you just set. Paste it into the `credentials.py`. Then you need to get your Device id.

```py
SPOTIPY_CLIENT_ID = 'your-client-id'
SPOTIPY_CLIENT_SECRET = 'your-client-secret'
SPOTIPY_REDIRECT_URI = 'your-redirect-uri'
SCOPE = "user-read-currently-playing user-modify-playback-state user-read-playback-state streaming"
DEVICE_ID = 'your-device-id'
```

If you have any questions let me know :)
