from flask import Flask, render_template, request
from sentiment import analyze_sentiment
import pandas as pd
import os

app = Flask(__name__)

CSV_FILE = "reviews.csv"

if not os.path.exists(CSV_FILE):
    pd.DataFrame(columns=["Review", "Sentiment", "Confidence"]).to_csv(CSV_FILE, index=False)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        review = request.form["review"]

        analysis = analyze_sentiment(review)

        result = analysis

        df = pd.read_csv(CSV_FILE)

        new_row = {
            "Review": review,
            "Sentiment": analysis["label"],
            "Confidence": analysis["score"]
        }

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)