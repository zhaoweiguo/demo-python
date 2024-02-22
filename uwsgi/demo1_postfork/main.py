from flask import Flask, request, jsonify
from uwsgidecorators import postfork
import time, datetime

app = Flask(__name__)


class SystemCommand(object):
    def __init__(self):
        self.words = {"time": self.gettime()}

    def run(self):
        return self.words

    def update(self):
        self.words = {"time":self.gettime()}

    def gettime(self):
         dt= datetime.datetime.now().strftime("%H:%M:%S")
         return dt


main_instance = SystemCommand()

@postfork
def update_stop_dict():
    main_instance.update()




@app.route("/")
def hello_world():
    rtn = main_instance.run()
    # return jsonify(rtn)
    # print(rtn)
    return jsonify(rtn)


@app.route("/update")
def update_stop_dict_route():
    update_stop_dict()  # 在处理这个路由时触发更新操作
    return jsonify({"success": "ok"})


if __name__ == "__main__":
    app.run()


