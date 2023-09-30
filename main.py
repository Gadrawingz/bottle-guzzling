from bottle import route, run, template


@route('/welcome')
def welcome():
    return "Hello Bottle World!"

# In case I may use one route or another...
@route('/')
@route('/home')
def home():
    return "Homepage"

@route('/developer/<username>')
def greetDeveloper(username='gadiradufasha'):
    result = template('Hi {{username}}, Waguan?', username=username)
    return result

run(host='localhost', port=8080, debug=True)