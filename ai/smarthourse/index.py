import openai, os

openai.api_key = os.getenv("OPENAI_API_KEY")

audio_file= open("./ai/openai/smarthourse/voice.mp3", "rb")

transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript)
print(transcript['text'])



