from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='build')


@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/<path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)


if __name__ == '__main__':
    app.run(debug=True)