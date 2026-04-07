from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from CI/CD Pipeline 🚀"

if __name__ == "__main__":
    print("App loaded successfully")