import os
import requests
import pyperclip
import argparse
import json
from playsound import playsound
from dotenv import load_dotenv
from settings import VOICE_IDS

load_dotenv()

# Move the global variables to environment variables
XI_API_KEY = os.getenv("XI_API_KEY")
TEMP_AUDIO_FILE = "/Users/USERNAME/_temp_tts_audio.mp3"
VOICES_URL = "https://api.elevenlabs.io/v1/voices"


# Define chunk size for audio file
CHUNK_SIZE = 1024

# Define headers
headers = {
    "Accept": "audio/mp3",
    "Content-Type": "application/json",
    "xi-api-key": XI_API_KEY,
}


def generate_audio(text="No Text Given. Please give me some text to read.", voice_id=VOICE_IDS['default']):
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
            "style": 0,
            "use_speaker_boost": True,
        },
    }

    voice_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    response = requests.post(voice_url, json=data, headers=headers)
    with open(TEMP_AUDIO_FILE, "wb") as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)


def play_audio():
    if os.path.exists(TEMP_AUDIO_FILE):
        playsound(TEMP_AUDIO_FILE)
    else:
        print(f"No such file:{TEMP_AUDIO_FILE}")


def get_voices():
    # Define URL and headers
    url = VOICES_URL
    my_headers = {"Accept": "application/json", "xi-api-key": XI_API_KEY}
    response = requests.get(url, headers=my_headers)
    json_data = json.loads(response.text)
    print("Getting voices...")
    for voice in json_data["voices"]:
        name = voice["name"]
        voice_id = voice["voice_id"]
        category = voice["category"]
        description = voice["description"]
        gender = voice["labels"].get("gender", "Unknown")
        age = voice["labels"].get("age", "Unknown")
        use_case = voice["labels"].get("use case", "Unknown")
        print(f"{name}({voice_id}) - {category}({gender}-{age}-{use_case}) : {description}")


def main():
    # Create the parser
    parser = argparse.ArgumentParser()

    # Add an argument
    parser.add_argument('character', type=str, nargs='?', default='joanne', help='The character to read the text')

    # Parse the arguments
    args = parser.parse_args()

    # Use the dictionary to get the voice ID
    new_voice_id = VOICE_IDS.get(args.character.lower(), VOICE_IDS['default'])

    text = pyperclip.paste()
    generate_audio(text, voice_id=new_voice_id)
    play_audio()
    print(text)


if __name__ == "__main__":
     main()
#     get_voices()