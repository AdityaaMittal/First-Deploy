from flask import Flask
app = Flask("My App")

@app.route("/", methods=["GET"])
def welcome():
    return "<h1>Welcome to my app!</h1>"

if __name__ == "__main__":
    app.run()