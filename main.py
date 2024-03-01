from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_snippet():
    data = request.json
    private_snippet = data.get('privateSnippet')
    print(f"Received private snippet: {private_snippet}")
    # Here you can log the snippet to a file or database as needed
    return jsonify({"status": "success", "message": "Snippet logged"}), 200

if __name__ == '__main__':
    app.run(debug=True)
