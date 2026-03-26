from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 lyx AI 已上线成功！"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
