import spotipy
from spotipy.oauth2 import SpotifyOAuth
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
redirect_uri = os.getenv('redirect_uri')

client = genai.Client(api_key = GEMINI_API_KEY)

scope = ["playlist-modify-private", 'playlist-modify-public', 'user-read-playback-state', 'user-modify-playback-state', 'ugc-image-upload']

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = client_id, client_secret = client_secret, redirect_uri = redirect_uri, scope=' '.join(scope)))


def gemini_prompt(name_entry, name_label):
    try:
        response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        The user has expressed the following sentiment: {name_entry.get()}.
        Based on this emotional tone, generate a highly relevant and evocative search query that could be used to find a Spotify playlist. 
        The playlist should reflect the mood in a musically authentic way — considering genre, tempo, and emotional resonance.
        Avoid generic terms like 'happy music' or 'sad songs'. Instead, use expressive phrases like 'melancholic acoustic ballads', 'high-energy workout anthems', or 'soothing lo-fi beats for anxiety'.
        Make sure the query is suitable for Spotify's search engine and likely to return curated playlists that match the sentiment.
        """,
        )
        give_playlist(response.text, name_label)
    except Exception as e:
        print(f"Error: {e}")

def give_playlist(response, name_label):
    try:
        results = sp.search(q=response, type='playlist')
        playlistName = results['playlists']['items'][0]['name']
        playlistOwner = results['playlists']['items'][0]['owner']['display_name']
        name_label.configure(text= f"Playlist Recommendation: {playlistName} Playlist Owner: {playlistOwner}")
        print(f"Playlist Recommendation: {playlistName} Playlist Owner: {playlistOwner}")
    except Exception as e:
        print(f"Error {e}")


