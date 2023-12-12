import pyaudio
import wave

# 打开麦克风并开始录音  
p = pyaudio.PyAudio()

# 查看录音设备
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(info)
    # if info["maxInputChannels"] > 0:
    #     print("录音设备:", i, info["name"], info["maxInputChannels"], info["defaultSampleRate"]) 
    # if info["maxOutputChannels"] > 0:
    #     print("播放设备:", i, info["name"], info["maxOutputChannels"], info["defaultSampleRate"])

device_index=3
stream = p.open(format=pyaudio.paInt16, channels=1, rate=48000, input=True)

print("开始录音,请说话......")

# 录音并获取音频流 
audio = []
while True:
    data = stream.read(1024) 
    audio.append(data)
    if stream.stopped:
        break  

# 关闭流和 PyAudio  
stream.stop_stream()
stream.close()
p.terminate()  

# 将音频流保存为 wav 文件
wave_file = wave.open("recording.wav", "wb")
wave_file.setnchannels(1)  
wave_file.setsampwidth(2)
wave_file.setframerate(16000)
wave_file.writeframes(b''.join(audio))
wave_file.close()

print("录音完成。录音文件保存在 recording.wav")