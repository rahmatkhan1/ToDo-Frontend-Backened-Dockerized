from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "✅ Flask Backend is Running!"

@app.route('/submit', methods=['POST'])
def submit():
    item_id = request.form.get("item_id")
    item_uuid = request.form.get("item_uuid")
    item_hash = request.form.get("item_hash")

    return f"""
    ✅ Received data from frontend:<br>
    Item ID: {item_id}<br>
    Item UUID: {item_uuid}<br>
    Item Hash: {item_hash}
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


