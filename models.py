from pydantic import BaseModel


class ImageCaption(BaseModel):
    description: str
    top_music_genres: list[str]
    top_tags: list[str]
    title_playlist: str


class SongLookupResult(BaseModel):
    artist: str
    song_name: str


class WeatherData(BaseModel):
    date: str
    time: str
    kind: str
    temp: str
