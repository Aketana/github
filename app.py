from flask import Flask
from database import get_connection

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

@app.route("/users")
def get_all_users():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("SELECT id, name, job FROM users ORDER BY id")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [
        {
            "id": row[0],
            "name": row[1],
            "job": row[2]
        }
        for row in rows
    ]

@app.route("/users/<int:id>")
def get_user(id):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute(
        "SELECT id, name, job FROM users WHERE id = %s",
        (id,)
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        return {"error": "User not found"}, 404

    return {
        "id": row[0],
        "name": row[1],
        "job": row[2]
    }


@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  
