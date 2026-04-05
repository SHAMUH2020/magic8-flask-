from flask import Flask, render_template, request
import random

app = Flask(__name__)

responses = [
    "Yes, definitely.",
    "It is certain.",
    "Without a doubt.",
    "Signs point to yes.",
    "Most likely.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Cannot predict now.",
    "Don't count on it.",
    "My reply is no.",
    "Very doubtful.",
    "Outlook not so good."
]

@app.route("/", methods=["GET", "POST"])
def home():
    question = ""
    answer = ""

    if request.method == "POST":
        question = request.form.get("question", "").strip()
        if question:
            answer = random.choice(responses)

    return render_template("index.html", question=question, answer=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)