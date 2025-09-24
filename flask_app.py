from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Load your data using a relative path
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "data.csv")
df = pd.read_csv(CSV_FILE)

# Convert date/time columns safely
if 'Date and Time' in df.columns:
    df['Date and Time'] = pd.to_datetime(df['Date and Time'], errors='coerce')
    df.dropna(subset=['Date and Time'], inplace=True)

if 'Time' in df.columns:
    df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S', errors='coerce').dt.hour
    df.dropna(subset=['Hour'], inplace=True)
    df['Hour'] = df['Hour'].astype(int)

@app.route("/questions-per-month")
def questions_per_month():
    monthly = df.groupby([df['Date and Time'].dt.to_period('M'), 'Tag']).size().unstack(fill_value=0)
    top_tags = monthly.sum().sort_values(ascending=False).head(10).index
    monthly = monthly[top_tags]
    labels = monthly.index.astype(str).tolist()
    datasets = [
        {"label": tag, "data": monthly[tag].tolist()} for tag in top_tags
    ]
    return jsonify({"labels": labels, "datasets": datasets})

@app.route("/yearly-top-tags")
def yearly_top():
    yearly = df.groupby([df['Date and Time'].dt.year, 'Tag']).size().unstack(fill_value=0)
    top_tags = yearly.sum().sort_values(ascending=False).head(7).index
    yearly = yearly[top_tags]
    labels = yearly.index.astype(str).tolist()
    datasets = [
        {"label": tag, "data": yearly[tag].tolist()} for tag in top_tags
    ]
    return jsonify({"labels": labels, "datasets": datasets})

@app.route("/tag-rank-shift")
def tag_rank_shift():
    monthly_counts = df.groupby([df['Date and Time'].dt.to_period('M'), 'Tag']).size().unstack(fill_value=0)
    monthly_ranks = monthly_counts.rank(axis=1, method='min', ascending=False)
    top_tags = monthly_counts.sum().sort_values(ascending=False).head(7).index
    monthly_ranks = monthly_ranks[top_tags].fillna(len(monthly_counts.columns))
    labels = monthly_ranks.index.astype(str).tolist()
    datasets = [
        {"label": tag, "data": monthly_ranks[tag].tolist()} for tag in top_tags
    ]
    return jsonify({"labels": labels, "datasets": datasets})

@app.route("/python-related-tags")
def python_related_tags():
    py_keywords = ["numpy", "pandas", "matplotlib", "scipy", "seaborn"]
    filtered = df[df['Tag'].str.lower().isin(py_keywords)]
    monthly = filtered.groupby([filtered['Date and Time'].dt.to_period('M'), 'Tag']).size().unstack(fill_value=0)
    labels = monthly.index.astype(str).tolist()
    datasets = [
        {"label": tag, "data": monthly[tag].tolist()} for tag in monthly.columns
    ]
    return jsonify({"labels": labels, "datasets": datasets})

@app.route("/hourly-trend")
def hourly_trend():
    hourly = df.groupby(['Hour', 'Tag']).size().unstack(fill_value=0)
    top_tags = hourly.sum().sort_values(ascending=False).head(5).index
    hourly = hourly[top_tags].fillna(0)
    labels = hourly.index.astype(str).tolist()
    datasets = [
        {"label": tag, "data": hourly[tag].tolist()} for tag in top_tags
    ]
    return jsonify({"labels": labels, "datasets": datasets})

if __name__ == "__main__":
    app.run(debug=True)