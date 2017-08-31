from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def index():
	os.system('python speech.py')
	return "finished"

if __name__ == "__main__":
	app.run()	
