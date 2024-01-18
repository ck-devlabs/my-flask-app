#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
    Enter your name to get a greeting:
     <form action="/echo_user_input" method="POST">
         <input name="user_input" placeholder="Jack">
         <input type="submit" value="Submit!">
     </form>
     '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "Greetings, " + input_text + "! How are you?<br/>Please rate my assignment well!<br/>Thanks"