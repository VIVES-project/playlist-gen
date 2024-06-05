from pydantic import BaseModel


class ImageCaption(BaseModel):
    description: str
    top_music_genres: list[str]
    title_playlist: str
    music_energy: str
    music_tempo: str


class SongLookupResult(BaseModel):
    artist: str
    song_name: str


class Song_List(BaseModel):
    song_name_list: list
    song_id_list: list
    song_album_image_list: list


class WeatherData(BaseModel):
    date: str
    time: str
    kind: str
    temp: str
