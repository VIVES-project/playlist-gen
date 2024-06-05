import csv 
from models import ImageCaption, SongLookupResult
import random

DATA_PATH = './data/dataset_new.csv'

def get_top_songs(caption: ImageCaption) -> list[SongLookupResult]:
    print(f"Searching songs of the genres: {caption.top_music_genres}, with tempo >= {caption.music_tempo} and energy >= {caption.music_energy}")

    results = []
    
    with open(DATA_PATH, encoding="utf8") as file_obj: 
        reader_obj = csv.DictReader(file_obj) 
        for row in reader_obj:
            tempo = float(row["tempo"])
            energy = float(row["energy"])

            if (row["track_genre"] in caption.top_music_genres) \
                and (energy >= float(caption.music_energy)) \
                    and (tempo >= float(caption.music_tempo)):
                
                results.append(f"{row['artists']} - {row['track_name']}")

    # Return a random sample of 5 results
    return random.sample(results, min(len(results), 5))


if __name__ == "__main__":
    test_input = '{"description": "The person in the image is wearing a black hoodie with a bold, white graphic print that suggests a connection to the alternative or metal music scene. Their relaxed pose and confident expression give off a cool, laid-back vibe, reflecting a youthful and energetic spirit.","top_music_genres": ["metal", "punk-rock"],"title_playlist": "Sunny Metal Vibes","music_energy": "0.750","music_tempo": "120"}'
    test_input = ImageCaption(**eval(test_input))

    print(get_top_songs(test_input))