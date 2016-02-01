from flask import Flask,request,url_for

app = Flask(__name__)

@app.route('/')
def helloworld():
    return 'hello world.'

@app.route('/user', methods = ['POST'])
def user():
    return "hello user"

@app.route('/user/<id>')
def user_id(id):
    return "hello user" + id

@app.route('/query_user')
def query_user():
    id = request.args.get('id')
    return "query user" + id

@app.route('/query_url')
def query_url():
    return "query url: " + url_for('query_user')

if __name__ == '__main__':
    app.run()