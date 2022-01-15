import json
import ast
import os
import random
import pickle
import datetime
import json
import cherrypy
from flask import Flask,request,jsonify,Response
from flask import make_response, current_app
from flask_cors import CORS
from datetime import timedelta
from functools import update_wrapper
import jsonpickle

from flask import flash,redirect,Response
from werkzeug.utils import secure_filename


app  = Flask(__name__)
CORS(app)

try:
    with open('model.pkl' , 'rb') as f:
        model_bce = pickle.load(f)
        
    with open('compile_success_lab_en.pkl' , 'rb') as f:
        lab_en_compile_success = pickle.load(f)

    with open('tx_file_type_lab_en.pkl' , 'rb') as f:
        lab_en_tx_file_type = pickle.load(f)

    with open('tx_difficulty_lab_en.pkl' , 'rb') as f:
        lab_en_tx_diff = pickle.load(f)

    with open('features_list.pkl' , 'rb') as f:
        features_list = pickle.load(f)
except Exception as e:
    print("Exception in loading the models and others  ",str(e))


def crossdomain(origin=None, methods=None, headers=None, max_age=21600, attach_to_all=True, automatic_options=True):
    """Decorator function that allows crossdomain requests.
      Courtesy of
      https://blog.skyred.fi/articles/better-crossdomain-snippet-for-flask.html
    """
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, list):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, list):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        """ Determines which methods are allowed
        """
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        """The decorator function
        """
        def wrapped_function(*args, **kwargs):
            """Caries out the actual cross domain code
            """
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route("/")
@app.route("/get_bce",methods = ["GET","POST","OPTIONS","HEAD"])
@crossdomain(origin='*')
def predict_bce():
    description = request.get_json()
    # print(description)
    x_test = dict()
    for feature in features_list:
        x_test[feature] = description[feature]

    x_test['tx_difficulty'] = lab_en_tx_diff.transform([x_test['tx_difficulty']])[0]
    x_test['compile_success'] = lab_en_compile_success.transform([x_test['compile_success']])[0]
    x_test['tx_file_type'] = lab_en_tx_file_type.transform([x_test['tx_file_type']])[0]

    pred_bce = model_bce.predict(x_test)
    response = dict()
    response['avg_bce'] = pred_bce[0]
    return Response(response=jsonpickle.encode(response), status=200, mimetype="application/json")


# if __name__ == "__main__":
#     app.secret_key = "123456789"
#     app.run(host="0.0.0.0",port = 9813,debug = True,threaded=False)
#     app.run(host = "127.0.0.1",debug = True)

socket_host = "127.0.0.1"
socket_port = 9813
thread_pool = 10

cherrypy.tree.graft(app, '/')
cherrypy.config.update({'server.socket_host': socket_host,
                        'server.socket_port': socket_port,
                        'tools.proxy.on': True,
                        # 'tools.proxy.base': proxy_base,
                        'engine.autoreload.on': False,
                        'server.thread_pool': thread_pool
                        })

if __name__ == '__main__':
    cherrypy.engine.start()