from flask import Flask, request
import socket


# Get my machine hostname
if (socket.gethostname().find('.') >= 0):
    hostname = socket.gethostname()
else:
    hostname = socket.gethostbyaddr(socket.gethostname())[0]
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello API Server : Default Request from (hostname) : "
    + hostname + "!\n"


@app.route('/getHello')
def getRequestHello():
    return "Hello API Server : GET Request!\n"


@app.route('/createHello', methods=['POST'])
def postRequestHello():
    mydata = request.data
    print("Data:" + mydata)
    assert request.path == '/createHello'
    assert request.method == 'POST'
    data = str(request.form['mykey'])
    # import pdb; pdb.set_trace()
    return "Hello API Server : You sent a " + request.method + \
        "message on route path " + request.path + \
        " \n\tData:" + data + "\n"


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
