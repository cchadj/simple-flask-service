from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'server is running'


def main():
    app.run(debug=True, host='localhost', port=5000)


if __name__ == '__main__':
    main()
