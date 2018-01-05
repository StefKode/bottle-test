#!/usr/bin/python
import time
from bottle import Bottle, run, static_file, response

app = Bottle()

@app.route('/events')
def page_index():
        try:
            response.content_type = 'text/event-stream'
            response.cache_control = 'no-cache' 
            yield 'retry: 100\n\n'
            i = 1
            while True:
                yield 'data: %i\n\n' % i
                i += 1
                time.sleep(0.2)
        except:
            print("event exception")

@app.route('/')
def page_index():
       return static_file('index.html', root='pages/')

app.run(threaded=True, host='0.0.0.0', port=8080)
