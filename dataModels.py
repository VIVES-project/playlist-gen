from pydantic import BaseModel

class ImageCaption(BaseModel):
    description: str
    top_music_genres: list[str]
    title_playlist: str
    music_energy: str
    music_tempo: str

class Song(BaseModel):
    song_name: str
    song_id: str
    song_album_image: str

class WeatherData(BaseModel):
    date: str
    time: str
    kind: str
    temp: str
