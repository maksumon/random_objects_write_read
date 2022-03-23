import webbrowser
from flask import Flask, render_template, send_file
from reader import generate_report
from writer import generate_objects
import os

app = Flask(__name__)

# let's define an initial app route to browse the web application's index.html file
@app.route('/')
def welcome():
    return render_template('index.html')

# let's define a "/generate" app route to generate random objects from
# the user interaction and return file name
@app.route('/generate', methods=["GET"])
def generate():
	data = generate_objects()
	return data

# let's define a "/report" app route to generate a report of the random objects count from
# the user interaction and return the result
@app.route('/report', methods=["GET"])
def report():
	generated_report = generate_report()
	return generated_report

# let's define a "/<file_name>" app route to download the generated file from the user interaction
@app.route('/<file_name>', methods=["GET"])
def download(file_name):
	#For windows it needs to use drive name [ex: C:/demo.txt]
    return send_file(file_name, as_attachment=True)

def main():
    # The reloader has not yet run - open the browser
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:5000/')

    # Otherwise, continue as normal
    app.run(debug=True)

if __name__ == '__main__':
    main()