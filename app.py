import os
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv

load_dotenv()

SERVICE_PORT = os.getenv("SERVICE_PORT", 8888)
SERVICE_HOST = os.getenv("SERVICE_HOST", "localhost")

app = Flask(__name__)


@app.route('/')
def index():
    return 'server is running'


@app.route('/hello')
def hello():
    return 'hello'


@app.route('/echo/<text_message>', methods=['GET'])
def echo(text_message: str):
    return text_message


@app.route('/echo-with-query-parameters', methods=['GET'])
def echo_with_query_parameters():
    default_message = 'No message provided.'
    message1 = request.args.get('message1', default_message)
    message2 = request.args.get('message2', default_message)
    return {
        "message1": message1,
        "message2": message2
    }


@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.json
    try:
        num1 = data['num1']
        num2 = data['num2']
        result = num1 * num2
        return jsonify({'result': result})
    except (KeyError, TypeError, ValueError):
        return jsonify({'error': 'Invalid input, please provide two numerical values.'})


@app.route('/download/<path:filename>')
def download_file(filename: str):
    return send_from_directory(
        "uploads",
        filename,
        as_attachment=False
    )


def main():
    app.run(debug=True, host=SERVICE_HOST, port=SERVICE_PORT)


if __name__ == '__main__':
    main()
