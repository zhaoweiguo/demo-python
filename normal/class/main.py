import sub


sub = sub.Sub()

class Main(object):
    def __init__(self):
        print("main init")



def init():
    main = Main()


if __name__ == '__main__':
    print("+++++")
    sub.run("hello")


