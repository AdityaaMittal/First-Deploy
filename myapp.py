from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('myapp.html')

@app.route('/button_action')
def button_action():
    # Return a JSON response that will be displayed in the HTML
    return jsonify(message="Button was clicked!")

if __name__ == "__main__":
    app.run(debug=True)
