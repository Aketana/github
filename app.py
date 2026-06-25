from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 GitHub Actions Lab</h1>
    <h2>Hello from Flask running in Docker</h2>
    """

@app.route("/health")
def health():
    return {
        "status": "OK",
        "version": "1.0",
        "message": "Application is running"
    }

@app.route("/about")
def about():
    return {
        "author": "Aketana",
        "lab": "GitHub Actions + Docker"
    }

@app.route("/me")
def me():
    return {
        "name": "Aketana",
        "job": "DevOps Learner",
        "lab": "GitHub Actions"
    }
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)