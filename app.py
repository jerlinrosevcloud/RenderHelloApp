from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
        <p>Paas</p>
        <h1>A Simple Web Application</h1>
        <h2>Cloud Computing Experiment</h2>
        <h3>Done by Jerlin Rose V</h3>
    """

@app.route("/about")
def about():
    return """
        <p>Welcome to the About Page</p>
        <h1>This is A Simple Web Application</h1>
        <h2>Built to test Platform as a Service</h2>
        <h3>Thank You !!! ByeBye</h3>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)