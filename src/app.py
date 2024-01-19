#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
    <h1>Welcome to the Greeting App</h1>
    <p>Enter your name to get a greeting:</p>
     <form action="/echo_user_input" method="POST">
        <label for="user_input">Name:</label>
        <input type="text" id="user_input" name="user_input" placeholder="Please enter your name." required>
        <button type="submit">Submit</button>
    </form>
     '''
@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "Hello, " + input_text + "! Hope you are doing great!</br> Thanks for reviewing my assignment"
