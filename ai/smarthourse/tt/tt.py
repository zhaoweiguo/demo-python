import pyaudio 
import wave
import time
import sys

FORMAT = pyaudio.paInt16    # 采样位数
CHANNELS = 1                # 通道数 
RATE = 48000                # 采样率
CHUNK = 1024                # 数据块大小
RECORD_SECONDS = 5          # 录音时长
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()  

frames = []   # 录音数据

def callback(in_data, frame_count, time_info, status): 
    try:
        print("==", frame_count, time_info, status)
        print("=>", len(in_data))
        frames.append(in_data)
        print("->", len(frames))
    except Exception as e:
        print("2++++++++++++++++++++++++++++++")
        print(e)
        print("2++++++++++++++++++++++++++++++")

try: 
    stream = p.open(format=FORMAT,
                    channels=CHANNELS, 
                    rate=RATE, 
                    input=True,
                    input_device_index=1,  
                    frames_per_buffer=CHUNK,
                    stream_callback=callback)
    
except Exception as e:
    print("++++++++++++++++++++++++++++++")
    print(e)
    print("++++++++++++++++++++++++++++++")
    
# 录音 
try:
    stream.start_stream()
    print("* 开始录音")
    while stream.is_active():
        try:
            # print(1)
            time.sleep(0.1)
        except ValueError:
            print("3++++++++++++++++++++++++++++++")
            print("e3-2: ")
            print("3++++++++++++++++++++++++++++++")
        except Exception:
            print("3++++++++++++++++++++++++++++++")
            print("e3: ", sys.exc_info())
            print("3++++++++++++++++++++++++++++++")

except Exception as e:
    print("4++++++++++++++++++++++++++++++")
    print("e4:", e)
    print("4++++++++++++++++++++++++++++++")

# 录音结束
try: 
    stream.stop_stream()  
    print("* 录音结束")
except Exception as e:
    print(e)


time.sleep(1)
print("=======>", len(frames))

# 保存wav文件  
try:
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb') 
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
except Exception as e:
    print(e)
    
try: 
    p.terminate()
except Exception as e:
    print(e)