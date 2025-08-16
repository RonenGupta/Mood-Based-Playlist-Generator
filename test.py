import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="0057749368e44ce4bf093449ebd20550",
    client_secret="faaff0f8f6b641fbb83916074c4f3365",
    redirect_uri="https://example.org/callback",
    scope=scope))

results = sp.currently_playing()
print(results['item']['name'])
print(results['item']['artists'][0]['name'])