from flask import Flask
app = Flask(__name__)



@app.route('/')
def handler():
    return render_template('handle.html')