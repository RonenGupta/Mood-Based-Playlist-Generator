from transformers import pipeline
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
    
pipeline = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

def synthesise_input(name_entry, name_label):
    user_input = name_entry.get()
    if user_input:
        user_input = [user_input]
        user_input = pipeline(user_input)
        name_label.config(text= f"{user_input[0][0]['label']} || Detected Score: {round(user_input[0][0]['score'], 2)}")
        print(f"Detected Sentiment: {user_input[0][0]['label']} || Detected Score: {round(user_input[0][0]['score'], 2)}")
    else:
        print("Please enter a mood!")

