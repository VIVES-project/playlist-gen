import json
import os
import io
from dotenv import load_dotenv
import base64
import traceback
import numpy as np
from PIL import Image
from openai import OpenAI

"""
Image captioning with GPT-4
based on: https://github.com/42lux/CaptainCaption
"""

def generate_description(api_key: str, image: str|np.ndarray, prompt:str, detail:str, max_tokens:int) -> str:

    format = image.split(".")[2]
    if format.upper() not in ["JPEG", "PNG"]:
        raise AssertionError("image format not supported")

    try:
        img = Image.fromarray(image) if isinstance(image, np.ndarray) else Image.open(image)
        img = scale_image(img)

        buffered = io.BytesIO()
        img.save(buffered, format=format)
        img_base64 = base64.b64encode(buffered.getvalue()).decode()

        client = OpenAI(api_key=api_key)
        payload = {
            "model": "gpt-4-turbo",
            "messages": [{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url",
                     "image_url": {"url": f"data:image/jpeg;base64,{img_base64}", "detail": detail}}
                ]
            }],
            "max_tokens": max_tokens
        }

        response = client.chat.completions.create(**payload)
        return response.choices[0].message.content

    except Exception as e:
        with open("error_log.txt", 'a') as log_file:
            log_file.write(str(e) + '\n')
            log_file.write(traceback.format_exc() + '\n')
        return f"Error: {str(e)}"


def scale_image(img: Image):
    max_width = 2048

    if img.width > max_width:
        ratio = max_width / img.width
        new_height = int(img.height * ratio)
        return img.resize((max_width, new_height), Image.Resampling.LANCZOS)
    return img


if __name__ == "__main__":

    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if api_key is None:
        raise KeyError("OPENAI_API_KEY")

    image = "./img/test2.png"
    prompt = """
        The image contains a person. Describe their outfit and the vibe they give off, then suggest two music genres they are most likely to enjoy. 
        Limit it to exactly two. Answer in JSON with the following format: {'person_age':? ,'description': '', 'top_music_genre': ['genre1', 'genre2', '...'], 'top_tags'=['...']}', where top_tags can only have values from this set: ["dating", "violence","world/life","night/time","shake the audience","family/gospel","romantic","communication","obscene", "family/spiritual", "sadness","feelings"]. Provide at least 3 tags
    """
    #prompt = "What is in this image?"

    detail = "low"
    max_tokens = 300

    description = generate_description(api_key, image, prompt, detail, max_tokens)

    print(description)