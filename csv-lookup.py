import csv 
from models import ImageCaption, SongLookupResult
import random

DATA_PATH = './data/tcc_ceds_music.csv'
# DATA_PATH = './data/small.csv'

def get_top_songs(caption: ImageCaption)->list[SongLookupResult]:
    print(f"Searching songs of the genres: {caption.top_music_genres}, with tags: {caption.top_tags}")

    results = []

    # open csv and read line by line
    # if genre is not in caption.top_music_genres or topic is not in caption.top_tags, skip
    # else, add to results
    
    with open(DATA_PATH) as file_obj: 
        reader_obj = csv.DictReader(file_obj) 
        # Iterate over each row in the csv  
        # file using reader object 
        for row in reader_obj:
            # print(row["genre"], row["topic"])
            if (row["genre"] in caption.top_music_genres) and (row["topic"] in caption.top_tags):
                results.append(f"{row["artist_name"]} - {row["track_name"]}")

    # Return a random sample of 5 results
    return random.sample(results, min(len(results), 5))


# if __name__ == "__main__":
#     test_input = '{"description": "The person is wearing a casual white t-shirt with light blue horizontal stripes. The outfit, coupled with his relaxed posture and the indoor setting, suggests a laid-back, approachable vibe.", "top_music_genres": ["pop", "indie"], "top_tags": ["sadness", "violence"], "title_playlist": "dummy playlist title"}'
#     test_input = ImageCaption(**eval(test_input))

#     print(get_top_songs(test_input))