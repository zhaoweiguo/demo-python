import pyaudio

p = pyaudio.PyAudio()

device_index = 1  # 录音设备的索引

try:
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100,
                    input=True, frames_per_buffer=1024, input_device_index=device_index)
except OSError as e:
    print("录音设备不可用:", e)
