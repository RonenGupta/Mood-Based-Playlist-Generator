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
        Analyze user input: {name_entry.get()}. 
        Detect if it’s an emotional tone (e.g., 'happy'), artist (e.g., 'Taylor Swift'), or genre (e.g., 'jazz'). 
        Generate a Spotify-optimized search query (max 250 chars) reflecting the mood, artist style, or genre with evocative phrases like 'dreamy indie folk' or 'introspective rap flows'. 
        Avoid generic terms like 'happy music'; use 'playlist' if needed for curated results.
                """,)
        give_playlist(response.text, name_label)
        print(response.text)
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


