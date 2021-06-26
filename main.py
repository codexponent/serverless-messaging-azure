# # Importing Libraries
from app import app
from azure.storage.queue import (
        QueueClient,
        BinaryBase64EncodePolicy,
        BinaryBase64DecodePolicy
)
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect, url_for, render_template

# # Setting up configparser
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

# Retrieve the connection string from an environment
# variable named AZURE_STORAGE_CONNECTION_STRING
connect_str = config['STORAGE']['conn_string']
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
	message_request= request.form.get("message", "")

	# Instantiate a QueueClient object which will
	# be used to create and manipulate the queue
	q_name = "myqueue-items"
	queue_client = QueueClient.from_connection_string(connect_str, q_name)

	# # Add Base64 Encoding and Decoding Policy
	queue_client.message_encode_policy = BinaryBase64EncodePolicy()
	queue_client.message_decode_policy = BinaryBase64DecodePolicy()

	# # Sending the message
	message = message_request
	message_bytes = message.encode('ascii')
	queue_client.send_message(
		queue_client.message_encode_policy.encode(content=message_bytes)
		)
	
	return render_template('upload.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)