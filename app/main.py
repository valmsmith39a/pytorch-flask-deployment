from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Deploy PyTorch with Flask</h1>'''

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        return jsonify({'test': 'test_result'})

app.run()