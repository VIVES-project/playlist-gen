from pydantic import BaseModel

class ImageCaption(BaseModel):
    description: str
    top_music_genres: list[str]
    top_tags: list[str]

class SongLookupResult(BaseModel):
    artist: str
    song_name: str