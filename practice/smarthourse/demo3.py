import sounddevice as sd
import numpy as np
import wave

def record_audio(duration, sample_rate, channels, filename):
    print("开始录音...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
    sd.wait()  # 等待录音完成
    print("录音结束.")

    # 保存录音为WAV文件
    wav_data = np.squeeze(audio)  # 去除多余的维度
    wav_data = np.asarray(wav_data * (2 ** 15 - 1), dtype=np.int16)  # 将音频数据转换为16位整数
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(2)  # 16位采样宽度
    wf.setframerate(sample_rate)
    wf.writeframes(wav_data.tobytes())
    wf.close()
    print(f"保存文件成功: {filename}")

# 设置录音参数
duration = 5  # 录音时长（秒）
sample_rate = 48000  # 采样率
channels = 1  # 声道数
filename = "output.wav"  # 保存的文件名

# 调用录音函数
record_audio(duration, sample_rate, channels, filename)
