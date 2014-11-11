from datetime import datetime
from flask import Flask, url_for, render_template, request
app = Flask(__name__)

def current_time_string():
	return datetime.now().strftime("%I:%M:%S %p")

@app.route('/')
def index():
	now = current_time_string()
	return render_template('index.html')	

@app.route('/do_ping', methods=['POST'])
def do_ping():
	ip = request.form['ip']
	interval = request.form['interval']
	return render_template('pinger.html', ip=ip, interval=interval)

@app.route('/test_ajax', methods=['GET'])
def test_ajax():
	return current_time_string()

if __name__ == '__main__':
	app.debug = True
	app.run()