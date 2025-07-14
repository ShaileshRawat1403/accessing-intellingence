from langchain.tools import tool
from spotify_utils import retrieve_artist_id, retrieve_tracks

@tool
def get_music_recommendations(artists):
    """Get music recommendations"""
    final_result = {}
    for artist in artists:
        try:
            artist_id = retrieve_artist_id(artist)
            songs = retrieve_tracks(artist_id)
            final_result[artist] = songs
        except Exception as e:
            final_result[artist] = f"Error: {str(e)}"
    return final_result
