from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio

# download and load all models
preload_models()

# generate audio from text
text_prompt = """
     你好，我是赵卫国，来自山东东平，喜欢写代码、玩游戏.
"""
audio_array = generate_audio(text_prompt)

# save audio to disk
write_wav("./outputs/bark_generation.wav", SAMPLE_RATE, audio_array)
  
# play text in notebook
Audio(audio_array, rate=SAMPLE_RATE)




