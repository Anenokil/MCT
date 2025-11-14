from flask import Flask

app = Flask(__name__)

ping_count = 0


@app.route('/ping')
def ping():
    global ping_count
    ping_count += 1
    return 'pong'


@app.route('/visits')
def visits():
    return f'{ping_count}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
