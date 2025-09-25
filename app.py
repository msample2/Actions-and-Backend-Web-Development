from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html><body>
        <h1>Home Page</h1>
        <p>Welcompe to the backend demo.</p>
        <a href="/square?num=5">Go to Square Page</a><br>
        <a href="/add?x=3&y=7">Go to Add Page</a><br>
        <a href="/about">Go to About Page</a>
    </body></html>
    """

@app.route("/square")
def square():
    num = int(request.args.get("num", 2))
    result = num * num
    return f"""
    <html><body>
        <h1>Square Page</h1>
        <p>The square of {num} is {result}.</p>
        <a href="/">Back to Home</a>
    </body></html>
    """

@app.route("/add")
def add():
    x = int(request.args.get("x", 1))
    y = int(request.args.get("y", 1))
    result = x + y
    return f"""
    <html><body>
        <h1>Add Page</h1>
        <p>{x} + {y} = {result}</p>
        <a href="/">Back to Home</a>
    </body></html>
    """

@app.route("/about")
def about():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <html><body>
        <h1>About Page</h1>
        <p>This backend app was generated at {now}.</p>
        <a href="/">Back to Home</a>
    </body></html>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)

