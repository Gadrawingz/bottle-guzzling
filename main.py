from bottle import route, run

@route('/welcome')
def welcome():
    return "Hello Bottle World!"

# In case I may use one route or another...
@route('/')
@route('/home')
def home():
    return "Homepage"


run(host='localhost', port=8080, debug=True)