import requests
import base64

# Define your access token and user ID
# access_token = 'YOUR_ACCESS_TOKEN'
# user_id = 'YOUR_USER_ID'

#
def get_token(spotify_client_id, spotify_client_secret):
    # Encode the client ID and client secret
    authorization = base64.b64encode(f"{spotify_client_id}:{spotify_client_secret}".encode()).decode()

    # Define the headers and payload for the POST request
    headers = {
        'Authorization': f'Basic {authorization}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {
        'grant_type': 'client_credentials'
    }

    # Make the POST request to the Spotify token endpoint
    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response to get the access token
        return response.json().get('access_token')
    else:
        # Handle error
        raise Exception(f"Failed to get access token: {response.status_code} {response.text}")

# Example usage
spotify_client_id = 'df6017b470b049f593c9b7f1b306d4ba'
spotify_client_secret = 'c6d29a92c7da46a3b5212e58a6e5fd63'
access_token = get_token(spotify_client_id, spotify_client_secret)
print(access_token)
#

# Define the playlist details
playlist_name = 'Heavy Metal and Punk Vibes'
playlist_description = 'A playlist featuring heavy metal and punk songs.'

# Define the songs
songs = [
    ("Black Sabbath", "Paranoid"),
    ("The Clash", "London Calling"),
    ("Iron Maiden", "The Trooper"),
    ("Ramones", "Blitzkrieg Bop"),
    ("Metallica", "Enter Sandman"),
    ("Sex Pistols", "Anarchy in the U.K."),
    ("Motörhead", "Ace of Spades"),
    ("The Misfits", "Last Caress"),
    ("Slayer", "Raining Blood"),
    ("Dead Kennedys", "Holiday in Cambodia")
]

# Create headers for the requests
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Step 1: Create a new playlist
create_playlist_url = f'https://api.spotify.com/v1/users/{spotify_client_id}/playlists'
playlist_data = {
    'name': playlist_name,
    'description': playlist_description,
    'public': False
}
response = requests.post(create_playlist_url, headers=headers, json=playlist_data)
response_data = response.json()
if (response_data["error"] != None):
    print(response_data["error"])
    raise RuntimeError("The Request was not successful")
playlist_id = response_data['id']

# Step 2: Search for each track to get their Spotify URIs
track_uris = []
search_url = 'https://api.spotify.com/v1/search'
for artist, track in songs:
    query = f'{track} {artist}'
    params = {
        'q': query,
        'type': 'track',
        'limit': 1
    }
    response = requests.get(search_url, headers=headers, params=params)
    response_data = response.json()
    if response_data['tracks']['items']:
        track_uri = response_data['tracks']['items'][0]['uri']
        track_uris.append(track_uri)

# Step 3: Add the tracks to the playlist
add_tracks_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
add_tracks_data = {
    'uris': track_uris
}
response = requests.post(add_tracks_url, headers=headers, json=add_tracks_data)

if response.status_code == 201:
    print(f'Successfully created playlist: {playlist_name}')
else:
    print(f'Failed to create playlist: {response.json()}')





