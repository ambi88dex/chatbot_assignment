from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/response', methods=['POST'])
def response():
    data = request.get_json()

    if 'input_text' in data:
        input_text = data['input_text']
        server_response = f"Server response for : {input_text}"
        return jsonify({"response": server_response})
    else:
        return jsonify({"error": "Input text not provided"})
    

if __name__ == "__main__":
    app.run(debug=True)