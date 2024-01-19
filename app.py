from flask import Flask, request, jsonify

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


def main():
    app.run(debug=True, host="0.0.0.0", port=5000)


if __name__ == '__main__':
    main()
