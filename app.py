from flask import Flask
from flask import jsonify

from os import environ

app = Flask(__name__)


@app.route('/version')
def version():
    return jsonify({
        'version': '1.0',
        'models': [
        ],
        'seed': 111
    })


if __name__ == '__main__':
    port = environ.get('APP_PORT', '5000')
    port = int(port)
    debug = 'DEBUG' in environ
    app.run(debug=debug, host='0.0.0.0', port=port)
