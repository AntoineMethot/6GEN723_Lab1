from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    #x = 3/0
    return '<h2>Hello, World!, From AMZJ: 172.16.14.33</h2>'

if __name__=='__main__':
    app.run(host='0.0.0.0',port=3000)