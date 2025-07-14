import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

def init_spotify_client():
    client_id = os.getenv("SPOTIFY_CLIENT")
    client_secret = os.getenv("SPOTIFY_SECRET")

    if not client_id or not client_secret:
        print("DEBUG: Client ID or Secret is missing.")
        raise EnvironmentError("Spotify credentials are missing.")

    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(auth_manager=auth_manager)

spotify_client = init_spotify_client()

def retrieve_artist_id(artist_name):
    result = spotify_client.search(q=f"artist:{artist_name}", type="artist")
    return result["artists"]["items"][0]["id"] if result["artists"]["items"] else None

def retrieve_tracks(artist_id):
    response = spotify_client.artist_top_tracks(artist_id)
    return [track["name"] for track in response["tracks"][:5]]
