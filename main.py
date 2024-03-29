from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/log', methods=['POST'])
def log_snippet():
    data = request.json
    private_snippet = data.get('privateSnippet')
    print(f"Received private snippet: {private_snippet}")
    # Log the snippet to a file or database as needed
    return jsonify({"status": "success", "message": "Snippet logged"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=10000)
