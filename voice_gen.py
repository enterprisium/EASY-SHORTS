import os
import elevenlabs

# Set the API key as an environment variable
os.environ["ELEVENLABS_API_KEY"] = "sk_45fe7923b58a44371ab2667045e1e9b50e40b8250d4b2b24" 

# Now you can use the ElevenLabs library
def generate_voice_over(script):
    voice = elevenlabs.Voice(
        voice_id = "ErXwobaYiN019PkySvjV",
        settings= elevenlabs.VoiceSettings(
            stability=0.5,
            similarity_boost=0.75
        )
    )

    voice_over = elevenlabs.generate(
        text=script, 
        voice=voice)
    elevenlabs.save(voice_over, "voice_over.mp3")
