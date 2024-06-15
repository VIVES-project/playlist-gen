import streamlit as st
from PIL import Image
import numpy as np

from createPlaylist import create_playlist
from csvLookup import get_top_songs
from dataModels import WeatherData
from imgCaption import generate_caption

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    img = Image.open(img_file_buffer)

    img_array = np.array(img)

    st.write("Preparing your playlist...")

    caption = generate_caption(img_array, format="PNG", weather_desc="cloudy")

    st.header(caption.title_playlist)
    st.write(caption.description)

    st.subheader("Genres:")
    st.write(caption.top_music_genres)
    
    st.metric("Tempo", caption.music_tempo)
    st.metric("Energy", caption.music_energy)

    csv_songs = get_top_songs(caption)

    playlist_link, playlist_songs = create_playlist(
        song_track_list=csv_songs, 
        playlist_name=caption.title_playlist, 
        weather_data=WeatherData(date="09.06.2024", time="18:00", kind="cloudy", temp="25°C")
    )

    st.subheader(playlist_link)