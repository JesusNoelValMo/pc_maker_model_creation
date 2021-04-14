import joblib
import numpy as np

from flask import Flask
from flask import jsonify, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app,supports_credentials=True, resources={r'/.*': {'origins': '*'}})
app.config['CORS_HEADERS'] = 'Content-Type'
#cors = CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/hello', methods=['GET'])
def predict_happiness():
    return jsonify({'Message': 'Hello'})

@app.route('/try', methods=['GET', 'POST'])
@cross_origin(allow_headers=['Content-Type' ], supports_credentials=True)
def predict_heart_disease():
    if request.method == 'POST':
        #age = request.form.get('age')
        pass
        if prediction[0] == 1:
            pass
        else:
            pass
        
if __name__ == "__main__":
    app.run()
