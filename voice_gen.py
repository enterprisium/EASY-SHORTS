import os
from elevenlabs import save
from elevenlabs.client import ElevenLabs

# Set the API key as an environment variable
os.environ["ELEVENLABS_API_KEY"] = "sk_45fe7923b58a44371ab2667045e1e9b50e40b8250d4b2b24"

# Initialize the ElevenLabs client
client = ElevenLabs(api_key=os.environ["ELEVENLABS_API_KEY"])

def generate_voice_over(script):
    # Define the voice and model settings
    VOICE = "Antoni"  # This is the voice ID for "Antoni"
    MODEL = "eleven_multilingual_v2"

    # Generate the audio
    audio = client.generate(
        text=script,
        voice=VOICE,
        model=MODEL
    )

    # Save the generated audio
    save(audio, "voice_over.mp3")
