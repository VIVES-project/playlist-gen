from models import ImageCaption, SongLookupResult


def get_top_songs(caption: ImageCaption)->list[SongLookupResult]:
    print(f"Searching songs of the genres: {caption.top_music_genres}, with tags: {caption.top_tags}")

    results = []

    # open csv and read line by line
    # if genre is not in caption.top_music_genres or topic is not in caption.top_tags, skip
    # else, add to results

    return results


if __name__ == "__main__":
    test_input = '{"description": "The person is wearing a casual white t-shirt with light blue horizontal stripes. The outfit, coupled with his relaxed posture and the indoor setting, suggests a laid-back, approachable vibe.", "top_music_genres": ["rock", "jazz"],"top_tags": ["world/life", "night/time", "feelings"]}'
    test_input = ImageCaption(**eval(test_input))

    print(get_top_songs(test_input))