from flask import Flask, jsonify

# 创建Flask应用程序对象
app = Flask(__name__)

# 在此处创建应用上下文
with app.app_context():
    # 执行需要在应用上下文中运行的代码
    label = "label"
    score = 37.7
    value = jsonify({"code": 10000, "data": {"trend": label, "score": score}, "message":"success"})
    print(value)



