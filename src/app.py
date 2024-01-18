#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
    Enter your name to get a greeting:
     <form action="/echo_user_input" method="POST">
         <input name="user_input" placeholder="Please enter name.">
         <input type="submit" value="Submit!">
     </form>
     '''
@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "Hello, " + input_text + "! Hoe you are doing great!</br> Thanks for reviewing my assignment, Please rate it well! :)"