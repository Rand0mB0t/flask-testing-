from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'THis is the index page'


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port='4000')


