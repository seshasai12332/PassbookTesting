from flask import Flask, jsonify, request, make_response
import os

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	if request.method == 'GET':
		data = "Hello World!"
		return jsonify({'data': data})
	else:
		Post_Data = "Hello, This is a POST response"
		return make_response(jsonify({"Data":Post_Data}), 200)

if __name__ == '__main__':
	app.run()
