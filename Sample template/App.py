from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video = request.files["video"]
        video.save(os.path.join("static", video.filename))
        return f"Uploaded {video.filename} successfully."
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
