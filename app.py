from flask import *
app = Flask(__name__)
@app.route('/ping')
def ping():
    return jsonify(
        {
            "msg": "test"
        }
    )


if __name__ == '__main__':
    app.run(debug=True, port=5500)