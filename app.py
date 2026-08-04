from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello! My Python application is running on Render.</h1>

    <p>Welcome to my first Flask application.</p>

    <p>This application is deployed on Render.</p>

    <p>Thank you for visiting!</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)