#!/usr/bin/python3
from flask import Flask, request, json

app = Flask(__name__)

@app.route('/get_hello_world', methods=['GET'])
def get_people_count():
    return "Hello world!"
