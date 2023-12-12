import pyaudio
import wave
import pydub

# 定义录音参数
CHUNK = 1024  # 录音数据分段
FORMAT = pyaudio.paInt16  # 录音深度
CHANNELS = 1  # 单声道
RATE = 44100  # 采样率
RECORD_SECONDS = 5  # 录音时长
WAVE_OUTPUT_FILENAME = "output.wav"  # 输出文件名

# 开始录音 
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE, 
                input=True,
                frames_per_buffer=CHUNK)

frames = []
print("正在录音...")
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):  
    data = stream.read(CHUNK)
    frames.append(data)
print("录音结束!")

# 录音结束 
stream.stop_stream()
stream.close()
p.terminate()

# 保存录音 
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

# 播放录音
sound = pydub.AudioSegment.from_wav(WAVE_OUTPUT_FILENAME)
sound.play()

