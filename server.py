from flask import Flask, render_template
import Adafruit_DHT

app=Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

@app.route('/main')
def min():
    sensor = Adafruit_DHT.DHT11
    pin = 26
    humi,temp = Adafruit_DHT.read_retry(sensor,pin)
    DHT = {'temp' : temp, 'humi' : humi}
    return render_template("main.html",**DHT)

if __name__=='__main__':
     app.run(debug=True, host='localhost', port=8000)
