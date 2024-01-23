from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'server is running'


def main():
    app.run(debug=True, host="127.0.0.1", port=5000)


if __name__ == '__main__':
    main()
