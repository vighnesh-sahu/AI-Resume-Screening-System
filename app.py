from flask import Flask, render_template, request
from utils.pdf_extractor import extract_text_from_pdf
from utils.text_preprocessing import preprocess_text
from utils.matcher import calculate_similarity

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    score = None

    if request.method == "POST":
        resume = request.files["resume"]
        job_desc = request.form["job_description"]

        resume_path = "temp_resume.pdf"
        resume.save(resume_path)

        resume_text = extract_text_from_pdf(resume_path)
        resume_text = preprocess_text(resume_text)
        job_desc = preprocess_text(job_desc)

        score = calculate_similarity(resume_text, job_desc)

    return render_template("index.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)
