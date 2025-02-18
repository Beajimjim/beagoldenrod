from flask import Flask, jsonify

app = Flask(__name__)

def load_messages():
    messages = []
    try:
        with open("mensajes.txt", "r") as file:
            for line in file:
                parts = line.strip().split(": ", 1)
                if len(parts) == 2:
                    ip, text = parts
                    messages.append({"ip": ip, "text": text})
    except FileNotFoundError:
        pass
    return messages

@app.route("/mensajes", methods=["GET"])
def get_messages():
    return jsonify(load_messages())

if __name__ == "__main__":
    app.run(host="217.154.4.86", port=5000, debug=True)
