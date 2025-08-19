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
        client.max_output_tokens = 250
        response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
            Analyze this input: {name_entry.get()}.

            Determine whether it's a mood (e.g., 'happy'), an artist (e.g., 'Taylor Swift'), or a genre (e.g., 'jazz').

            Then generate a short, natural Spotify search query that a typical user might type to find a playlist. Use descriptive but simple phrases like 'chill indie playlist' or 'energetic workout mix'. Include the word 'playlist' if it helps improve results. Avoid overly complex or poetic language. Output only the query—no labels, titles, or extra formatting.
            """
        ,)
        max_chars = 250
        output = response.text[:max_chars]
        give_playlist(output, name_label)
        print(output)
    except Exception as e:
        print(f"Error: {e}")

def give_playlist(response, name_label):
    try:
        results = sp.search(q=response, type='playlist')
        playlistName = results['playlists']['items'][0]['name']
        playlistOwner = results['playlists']['items'][0]['owner']['display_name']
        if playlistName and playlistOwner:
            name_label.configure(text= f"Playlist Recommendation: {playlistName} Playlist Owner: {playlistOwner}")
            print(f"Playlist Recommendation: {playlistName} Playlist Owner: {playlistOwner}")
        else:
            print(f"There was no recommendation! Please give a better description.")
    except Exception as e:
        print(f"Error {e}\n If this was a NoneType Error, the AI could not understand! Please give a valid mood, and/or a specific artist/genre clearly.")


