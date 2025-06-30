from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard_page():
    return render_template("index.html", active_section="dashboard-section")

@app.route("/story")
def story_page():
    return render_template("index.html", active_section="story-section")

@app.route("/about")
def about_page():
    return render_template("index.html", active_section="about-section")

if __name__ == "__main__":
    app.run(debug=True, port=2323)