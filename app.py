from flask import Flask, render_template, request, redirect, url_for
import wikipedia

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for("login"))

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username.lower() == "admin" and password == "1234":
            return redirect(url_for("chatbox"))
        else:
            return render_template("login.html", error="Invalid credentials.")
    return render_template("login.html")

@app.route('/chatbox')
def chatbox():
    return render_template("chatbox.html")

@app.route('/get', methods=["GET"])
def get_bot_response():
    user_text = request.args.get("msg")
    try:
        summary = wikipedia.summary(user_text, sentences=2)
    except:
        summary = "I couldn't find a result for that."
    return summary

if __name__ == "__main__":
    app.run(debug=True)
