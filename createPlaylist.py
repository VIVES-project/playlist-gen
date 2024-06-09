import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dataModels import Song, WeatherData

load_dotenv()

def create_playlist(song_track_list, playlist_name:str, weather_data:WeatherData, limit=20) -> tuple[str, list[Song]]:
    spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
    spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    redirect_uri = 'https://open.spotify.com/'

    if (spotify_client_id is None) or (spotify_client_secret is None):
        raise KeyError("SPOTIFY_API_KEY")

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                                client_secret=spotify_client_secret,
                                                redirect_uri=redirect_uri,
                                                scope="playlist-modify-public"))

    user_id = sp.current_user()['id']

    # Initialize playlist
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True)
    playlist_url = playlist["id"]
    playlist_url_complete = f'https://open.spotify.com/playlist/{playlist_url}'

    # Get seed songs
    recommended_tracks = recommend_tracks(sp, song_track_list, limit=limit)
    track_ids = map(lambda x: x.song_id, recommended_tracks)
    track_ids = list(track_ids)

    # Populate playlist
    if len(track_ids) > 0:
        sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'], tracks=track_ids)
    else:
        print("No tracks found for the provided song names.")

    print(f'Playlist "{playlist_name}" created successfully! Here is the url: {playlist_url_complete}')
    
    return playlist_url_complete, recommended_tracks


def recommend_tracks(sp:spotipy.Spotify, search_track_list, limit=10, input_track_limit=5) -> list[Song]:
    """
    RECOMMEND TRACKS. Takes a song list and outputs a recommendation list based on inputted songs
    Input the track_list. The input_track limit is set to 5 by default
    """
    search_results = []
    for i in range(input_track_limit):
        results = sp.search(q=search_track_list[i], limit=5, offset=0, type='track', market=None)
        search_results.append(results['tracks']['items'][0]['id'])

    recommendations = sp.recommendations(seed_artists=None, seed_genres=None, seed_tracks=search_results, limit=limit)

    song_list = []
    for i in recommendations['tracks']:
        song_list.append(Song(song_name=i['name'],song_id=i['id'],song_album_image=i['album']['images'][0]['url']))

    return song_list


if __name__ == "__main__":
    
    song_track_list = ['Toe - Boyo', 'Origami JP - Trains', 'Chon - Waterslide', 'Delta Sleep - 21 Letters', 'Tricot - Potage']
    
    create_playlist(
        song_track_list=song_track_list, 
        playlist_name="playlist_name", 
        weather_data=WeatherData(date="09.06.2024", time="18:00",kind="Sunny", temp="25°C")
    )