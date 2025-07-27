from flask import Flask, render_template, request
from parse_resume import parse_resume
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resume_text = ""
    if request.method == "POST":
        file = request.files["resume"]
        if file:
            file_path = os.path.join("uploads", file.filename)
            file.save(file_path)
            resume_text = parse_resume(file_path)
    return render_template("index.html", resume_text=resume_text)

if __name__ == "__main__":
    app.run(debug=True)
