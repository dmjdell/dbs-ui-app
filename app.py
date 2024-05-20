from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    pod_name = os.environ.get('MY_POD_NAME', 'N/A')
    env_name = os.environ.get('ENV_NAME', 'N/A')    # Get pod name from env
    message = f"Hello world from {pod_name} and {env_name } for GIC"           # Use it in the message
    return render_template('index.html', message=message)

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)