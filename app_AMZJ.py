from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    #XXX
    return '<h2>Hello, World!, From AMZJ: 172.16.14.33</h2>'

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=3000)