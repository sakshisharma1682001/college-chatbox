from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>College Chatbox</h2>

    <input type="text" id="msg" placeholder="Ask a question">
    <button onclick="sendMsg()">Send</button>

    <p id="reply"></p>

    <script>
    async function sendMsg() {
        let msg = document.getElementById('msg').value;

        let response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({message: msg})
        });

        let data = await response.json();
        document.getElementById('reply').innerText = data.reply;
    }
    </script>
    """

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"].lower().strip()

    if "fee" in user_message or "fees" in user_message:
        return jsonify({"reply": "B.Tech fees is ₹80,000 per year."})

    elif "admission" in user_message:
        return jsonify({"reply": "Admissions are open from June to August."})

    elif "library" in user_message:
        return jsonify({"reply": "Library is open from 9 AM to 5 PM."})

    elif "hostel" in user_message:
        return jsonify({"reply": "Hostel facility is available for boys and girls."})

    return jsonify({"reply": "Sorry, I don't have information about that."})

if __name__ == "__main__":
    app.run(debug=True)