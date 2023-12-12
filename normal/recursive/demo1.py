import time

def factorial(n):
    if n == 1:
        return 1
    else:
        print(n)
        print("\n")
        time.sleep(1)
        return n * factorial(n-1)
    
print(factorial(10))