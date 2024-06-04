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

# Create a new playlist
user_id = sp.current_user()['id']
playlist_name = 'Cool & Edgy Playlist'
playlist_description = 'A playlist that captures the cool and edgy vibe of metal and punk rock music.'
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=playlist_description)
playlist_url = playlist["id"]
playlist_url_complete = f'https://open.spotify.com/playlist/{playlist_url}'

# List of song names (you can customize this list)
song_names = [
    "Rebel Yell",
    "Black Hoodie Anthem",
    "Edge of Darkness",
    "Metal Mayhem",
    "Punk Rock Revolution",
    "Confident Chaos",
    "Rebellious Riffs",
    "Bold Graphic",
    "Heavy Metal Heart",
    "Punk Pose",
    "Edgy Expression",
    "Cool and Defiant",
    "Underscored Rebellion",
    "Bold and Brash",
    "Rock Rebel",
    "Metallic Confidence",
    "Graphic Noise",
    "Heavy Vibes",
    "Punk Power",
    "Rebel Sound"
]

# Search for tracks and add them to the playlist
track_ids = []
for song in song_names:
    result = sp.search(q=song, type='track', limit=1)
    if result['tracks']['items']:
        track_ids.append(result['tracks']['items'][0]['id'])

if track_ids:
    sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'], tracks=track_ids)
else:
    print("No tracks found for the provided song names.")

print(f'Playlist "{playlist_name}" created successfully! Here is the url: {playlist_url_complete}')
