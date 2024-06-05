import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

# Example usage
spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

if (spotify_client_id is None) or (spotify_client_secret is None):
    raise KeyError("SPOTIFY_API_KEY")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=spotify_client_id,
                                                           client_secret=spotify_client_secret))

# Your Spotify API credentials
client_id = spotify_client_id
client_secret = spotify_client_secret
redirect_uri = 'https://open.spotify.com/'

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="playlist-modify-public"))

# Create a new playlist
user_id = sp.current_user()['id']
# playlist_name = 'Cool & Edgy Playlist'
# playlist_description = 'A playlist that captures the cool and edgy vibe of metal and punk rock music.'
# playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=playlist_description)
# playlist_url = playlist["id"]
# playlist_url_complete = f'https://open.spotify.com/playlist/{playlist_url}'

# Input the track_list. The input_track limit is set to 5 by default
def recommend_tracks(search_track_list, limit=10, input_track_limit=5):
    # # SEARCH
    # name_results = []
    search_results = []

    for i in range(input_track_limit):
        results = sp.search(q=search_track_list[i], limit=5, offset=0, type='track', market=None)
        # name_results.append(results['tracks']['items'][0]['name'])
        search_results.append(results['tracks']['items'][0]['id'])

    # # Printing For Debugging
    # print(search_results)
    # print(name_results)

    # # RECOMMENDATION
    recommendations = sp.recommendations(seed_artists=None, seed_genres=None, seed_tracks=search_results, limit=limit)

    # List of Names (Optional, For Debugging Purposes)
    name_list = [i['name'] for i in recommendations['tracks']]
    print(name_list)

    # List of IDs (URLs)
    id_list = [i['id'] for i in recommendations['tracks']]
    print(id_list)

    return name_list

# # Search for tracks and add them to the playlist
# track_ids = []
# for song in song_names:
#     result = sp.search(q=song, type='track', limit=1)
#     if result['tracks']['items']:
#         track_ids.append(result['tracks']['items'][0]['id'])

# if track_ids:
#     sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'], tracks=track_ids)
# else:
#     print("No tracks found for the provided song names.")

# print(f'Playlist "{playlist_name}" created successfully! Here is the url: {playlist_url_complete}')

# SAMPLE
input_tracks = ['Toe - Boyo', 'Origami JP - Trains', 'Chon - Waterslide', 'Delta Sleep - 21 Letters', 'Tricot - Potage'] # Input track list as  here
recommended_tracks = recommend_tracks(input_tracks)