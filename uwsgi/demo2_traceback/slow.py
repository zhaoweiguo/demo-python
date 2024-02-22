import time

def dormi():
  time.sleep(60)

def dormi2():
  dormi()

def dormi3():
  dormi2()

def dormi4():
  dormi3()

def dormi5():
  dormi4()

def application(e, start_response):
  start_response('200 OK', [('Content-Type', 'text/html')])
  dormi5()
  return [b"hello"]




