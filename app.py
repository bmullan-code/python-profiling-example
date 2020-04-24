from flask import Flask
import time
import cProfile
import pstats

app = Flask(__name__)

def hi():
    time.sleep(1.5)
    y = 0
    for x in range(1,999999):
        y = y + 1

    return "hello"

@app.route('/')
def hello():
    cProfile.run('hi()')
    return hi()

if __name__ == '__main__':
    app.run()

