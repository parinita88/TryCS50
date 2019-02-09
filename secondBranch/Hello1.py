from flask import Flask, render_template
app=Flask(_name_)
@app.route("/")
def index():
    render_template("1.html")
