from flask import Flask
from flask import jsonify

from os import environ

app = Flask(__name__)


@app.route('/version')
def version():
    return jsonify({
        'version': '1.0',
        'models': [
        ]
    })


if __name__ == '__main__':
    port = environ.get('APP_PORT', '5000')
    port = int(port)
    app.run(debug=True, host='0.0.0.0', port=port)
