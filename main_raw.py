from azure.storage.queue import (
        QueueClient,
        BinaryBase64EncodePolicy,
        BinaryBase64DecodePolicy
)

import os, uuid
import base64
import json

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

# Retrieve the connection string from an environment
# variable named AZURE_STORAGE_CONNECTION_STRING
connect_str = config['STORAGE']['conn_string']


# Instantiate a QueueClient object which will
# be used to create and manipulate the queue
q_name = "myqueue-items"
queue_client = QueueClient.from_connection_string(connect_str, q_name)

# # Add Base64 Encoding and Decoding Policy
queue_client.message_encode_policy = BinaryBase64EncodePolicy()
queue_client.message_decode_policy = BinaryBase64DecodePolicy()

# # Sending the message
message = 'Hello World'
message_bytes = message.encode('ascii')
queue_client.send_message(
    queue_client.message_encode_policy.encode(content=message_bytes)
    )