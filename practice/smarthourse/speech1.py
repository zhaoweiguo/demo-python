import speech_recognition as sr

# 创建一个Recognizer对象
r = sr.Recognizer()

# 使用Microphone类创建一个麦克风对象
mic = sr.Microphone()

try:
    # 检查麦克风访问权限
    with mic as source:
        try:
            r.adjust_for_ambient_noise(source)  # 预处理环境噪声
        except sr.UnknownValueError:
            print("无法识别音频")
except sr.RequestError as e:
    print("无法获取麦克风访问权限：{0}".format(e))
except KeyboardInterrupt:
    print("检查被中断")
