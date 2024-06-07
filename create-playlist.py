import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from getWeather import getweather
import asyncio
from dataModels import Song



import streamlit as st
from PIL import Image
import numpy as np

from csvLookup import get_top_songs
from imgCaption import generate_caption



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
    recommended_tracks = sp.recommendations(seed_artists=None, seed_genres=None, seed_tracks=search_results, limit=limit)

    song_list = []
    for i in recommended_tracks['tracks']:
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
def create_playlist(song_track_list, playlist_name, weather_data, user_id=sp.current_user()['id'])->str:
    
    # PLAYLIST INITIALIZATION
    # user_id = sp.current_user()['id']
    playlist_description = f"Generated on {weather_data.date}, {weather_data.time}. Where the temperature is {weather_data.temp}, and the weather is {weather_data.kind}"
    # print(playlist_description)
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=playlist_description)
    playlist_url = playlist["id"]
    playlist_url_complete = f'https://open.spotify.com/playlist/{playlist_url}'

    # We input the ids
    if song_track_list:
        sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'], tracks=song_track_list)
    else:
        print("No tracks found for the provided song names.")
    
    return playlist_url_complete

    # print(f'Playlist "{playlist_name}" created successfully! Here is the url: {playlist_url_complete}')

# SAMPLE [MAIN]
if __name__ == "__main__":
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    # Placeholder
    song_track_list = ['Toe - Boyo', 'Origami JP - Trains', 'Chon - Waterslide', 'Delta Sleep - 21 Letters', 'Tricot - Potage']
    
    weather_data=asyncio.run(getweather())

    img_file_buffer = st.camera_input("Take a picture")
    csv_songs = song_track_list

    if img_file_buffer is not None:
        img = Image.open(img_file_buffer)

        img_array = np.array(img)

        st.write("Preparing your playlist...")

        caption = generate_caption(img_array, format="PNG", weather_desc="sunny")

        st.header("Description")
        st.write(caption)

        csv_songs = get_top_songs(caption)
        st.header("Songs from csv")
        st.write(csv_songs)
        
        recommended_tracks = recommend_tracks(csv_songs,limit=20)
        track_ids = map(lambda x: x.song_id, recommended_tracks)
        track_names = map(lambda x: x.song_name, recommended_tracks)
        track_ids = list(track_ids)
        track_names = list(track_names)

        st.header("Songs to Place on Playlist")
        st.write(track_names)

        song_track_list=track_ids
        playlist_name = caption.title_playlist
        st.header("Creating Playlist: " + f"{weather_data.date} " + f"{playlist_name}")
        url = create_playlist(song_track_list=song_track_list, playlist_name=playlist_name, weather_data=weather_data)
        st.write(f"Spotify Playlist Creation Successful! here is the link: {url}")