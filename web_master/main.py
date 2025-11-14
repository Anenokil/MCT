from flask import Flask, request

app = Flask(__name__)

ping_count = 0
ip_addresses = set()


@app.route('/ping')
def ping():
    global ping_count, ip_addresses

    ping_count += 1

    client_ip = request.remote_addr
    ip_addresses.add(client_ip)

    return 'pong'


@app.route('/visits')
def visits():
    return f'{ping_count}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
