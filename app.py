from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes and methods

@app.route('/', methods=['GET'])
def get_ip():
    user_ip = request.remote_addr
    return f'Your IP address is: {user_ip}. Next time, dont click on random links over the internet. You should be glad i am not logging this.'

if __name__ == '__main__':
    app.run()