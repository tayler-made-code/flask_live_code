from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def woof():
    url = "https://random.dog/woof.json"
    response = json.loads(requests.request("GET", url).text)
    woof = response["url"]
    return woof

def quack():
    url = "https://random-d.uk/api/random"
    response = json.loads(requests.request("GET", url).text)
    quack = response["url"]
    return quack

@app.route('/')
def index():
    return render_template('homepage_index.html')

@app.route('/woof')
def woof_page():
    woof_photo = woof()
    return render_template('woof_index.html', dog_photo=woof_photo)

@app.route('/quack')
def quack_page():
    quack_photo = quack()
    return render_template('quack_index.html', duck_photo=quack_photo)

if __name__ == '__main__':
    app.run(debug=True)