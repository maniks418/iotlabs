
from gpio import PiGpio
from flask import *


app = Flask(__name__)
pi_gpio = PiGpio()
LEDCOUNT = 3


def convertLedState(state):
    if state == 1:
        return 'ON'
    if state == 0:
        return 'OFF'
    return 'Argument error'


@app.route("/")
def index():
    # create an instance of my pi gpio object class.
    ledStates = {}
    for i in range(0, LEDCOUNT):
        ledStates['led'+str(i+1)] = convertLedState(pi_gpio.get_led(i+1))
    return render_template('index.html', result=ledStates)


@app.route("/leds/<int:led_state>", methods=['GET'])
def leds(led_state):
    ledState = {}
    ledState['led'+str(led_state)] = convertLedState(
                                    pi_gpio.get_led(led_state))
    return jsonify(ledState)


@app.route("/ledcmd", methods=['POST'])
def ledcommand():
    cmd_data = request.data
    print("LED Command:" + cmd_data)
    led = int(str(request.form['led']))
    state = str(request.form['state'])
    if(state == 'OFF'):
        pi_gpio.set_led(led, False)
    elif (state == 'ON'):
        pi_gpio.set_led(led, True)
    else:
        return "Argument Error"
    ledState = {}
    ledState['led'+str(led)] = convertLedState(pi_gpio.get_led(led))
    return jsonify(ledState)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
