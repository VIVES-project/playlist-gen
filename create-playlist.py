import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from dataModels import Song

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
def recommend_tracks(search_track_list, limit=10, input_track_limit=5)->list[Song]:
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

    song_list = []
    for i in recommendations['tracks']:
        song_list.append(Song(song_name=i['name'],song_id=i['id'],song_album_image=i['album']['images'][0]['url']))

    # List of Names (Optional, For Debugging Purposes)
    # name_list = [i['name'] for i in recommendations['tracks']]
    # print(name_list)

    # List of IDs (URLs)
    # id_list = [i['id'] for i in recommendations['tracks']]
    # print(id_list)

    return song_list

# PLAYLIST CREATION
playlist_name = "Sample Playlist"
playlist_description = "Sample Description"
def create_playlist(song_track_list, playlist_name, weather_date, limit=20, user_id=sp.current_user()['id']):
    
    # PLAYLIST INITIALIZATION
    # user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True) #, description=playlist_description
    playlist_url = playlist["id"]
    playlist_url_complete = f'https://open.spotify.com/playlist/{playlist_url}'

    recommended_tracks = recommend_tracks(song_track_list, limit=limit)
    # print(f"Track Names: {track_names}\n Track IDs: {track_ids}\n Track Album Image Links: {track_album_images}\n")
    print(recommended_tracks)

    # track_names = []
    # track_ids = []
    # track_album_images = []

    # for song in recommended_tracks:
    #     track_names.append(song.song_name)
    #     track_ids.append(song.song_id)
    #     track_album_images.append(song.song_album_image)

    # # Search for tracks and add them to the playlist
    # track_ids = []
    # # ! TODO - "try" to place the exact song into the generated tracklist
    # for song in recommended_tracks:
    #     # result = sp.search(q=song, type='track', limit=1)
    #     # if result['tracks']['items']:
    #         # track_ids.append(result['tracks']['items'][0]['id'])
    #     track_ids.append(song)

    track_ids = map(lambda x: x.song_id, recommended_tracks)
    print()
    print(list(track_ids))
    # # We input the ids
    # if track_ids:
    #     sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'], tracks=list(track_ids))
    # else:
    #     print("No tracks found for the provided song names.")

    # print(f'Playlist "{playlist_name}" created successfully! Here is the url: {playlist_url_complete}')


# SAMPLE [MAIN]

# THE PLAYLIST TITLE DESCRIPTION PARAMETERS
# Input the python-weather 'date' 'time' 'weather' data
# Input the generated 'title' 'description'

if __name__ == "__main__":
    song_track_list = ['Toe - Boyo', 'Origami JP - Trains', 'Chon - Waterslide', 'Delta Sleep - 21 Letters', 'Tricot - Potage']
    create_playlist(song_track_list=song_track_list, playlist_name="playlist_name", weather_date="weather_data")

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