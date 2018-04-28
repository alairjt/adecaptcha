import json
from flask import Flask, abort, request
from adecaptcha.decoder import PiDecoder

app = Flask(__name__)

@app.route("/captcha", methods=["POST"])
def parse_captcha():
    if not request.json:
        abort(400)

    body = request.json

    dir_config = './adecaptcha/%s'%(str(body["config_file"]))

    captcha = PiDecoder().decode(dir_config, str(body["url_audio"]))

    if captcha is None:
        abort(400, 'Cannot resolve this audio URL')

    return captcha

app.run(host='0.0.0.0', port=5000, debug=False)