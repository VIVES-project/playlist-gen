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

# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])

# Your Spotify API credentials
client_id = spotify_client_id
client_secret = spotify_client_secret
redirect_uri = 'https://open.spotify.com/'

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="playlist-modify-public"))

# RECOMMEND TRACKS. Takes a song list and outputs a recommendation list based on inputted songs
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
    # name_list = [i['name'] for i in recommendations['tracks']]
    # print(name_list)

    # List of IDs (URLs)
    id_list = [i['id'] for i in recommendations['tracks']]
    # print(id_list)

    return id_list

# PLAYLIST CREATION
playlist_name = "Sample Playlist"
playlist_description = "Sample Description"
def create_playlist(user_id=sp.current_user()['id'], playlist_name=playlist_name, playlist_description=playlist_description, limit=20):
    
    # PLAYLIST INITIALIZATION
    # user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=playlist_description)
    playlist_url = playlist["id"]
    playlist_url_complete = f'https://open.spotify.com/playlist/{playlist_url}'

    # <SONG LIST GENERATION>
    song_track_list = [] # Use this variable as the output of the song list generation functions and as input to the recommendation generation
    # 
    # 
    # SAMPLE TRACKS (FOR TESTING)
    song_track_list = ['Toe - Boyo', 'Origami JP - Trains', 'Chon - Waterslide', 'Delta Sleep - 21 Letters', 'Tricot - Potage']

    recommended_tracks = recommend_tracks(song_track_list, limit=limit)

    # # Search for tracks and add them to the playlist
    # track_ids = []
    # # ! TODO - "try" to place the exact song into the generated tracklist
    # for song in recommended_tracks:
    #     # result = sp.search(q=song, type='track', limit=1)
    #     # if result['tracks']['items']:
    #         # track_ids.append(result['tracks']['items'][0]['id'])
    #     track_ids.append(song)

    if recommended_tracks:
        sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'], tracks=recommended_tracks)
    else:
        print("No tracks found for the provided song names.")

    print(f'Playlist "{playlist_name}" created successfully! Here is the url: {playlist_url_complete}')

# SAMPLE [MAIN]

# THE PLAYLIST TITLE DESCRIPTION PARAMETERS
# Input the python-weather 'date' 'time' 'weather' data
# Input the generated 'title' 'description'
date = ""
time = ""
weather = ""
title = ""
description = " "

playlist_name = f"{title}"
playlist_description = f"{date} : {weather} : {description}"

create_playlist(playlist_name=playlist_name, playlist_description=playlist_description)





# # WORST CASE SCENARIO (Draft: Asking ChatGPT to generate a song list)
# ## The Worst Case Scenario
# Insert before if __name__ ...
# def generate_list(api_key: str, prompt:str, detail:str, max_tokens:int) -> str:
#     try:
#         client = OpenAI(api_key=api_key)
#         payload = {
#             "model": "gpt-4-turbo",
#             "messages": [{
#                 "role": "user",
#                 "content": [
#                     {"type": "text", "text": prompt},
#                 ]
#             }],
#             "max_tokens": max_tokens
#         }

#         response = client.chat.completions.create(**payload)
#         # Split comma separated value string
#         songList = response.choices[0].message.content.split(',')
#         return songList

#     except Exception as e:
#         with open("error_log.txt", 'a') as log_file:
#             log_file.write(str(e) + '\n')
#             log_file.write(traceback.format_exc() + '\n')
#         return f"Error: {str(e)}"
# ##

    # INSERT after 'print(description)'
    # # # TEST / EXPERIMENT
    # # Get a list of songs based on the description
    # prompt_list = """
    #     !!!From the previous answer!!!, give me a list of songs in a string of comma separated values
    # """
    # songList = generate_list(api_key, prompt)

    # print(songList)