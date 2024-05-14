from flask import Flask, render_template, request
import os

app = Flask(__name__)

pod_name = os.environ.get('MY_POD_NAME', 'N/A')

@app.route('/')
def index():
    return render_template('index.html', message="Hello world")

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
