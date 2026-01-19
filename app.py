from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    uploaded_file = request.files.get("csv_file")

    if uploaded_file is None:
        return "No file uploaded", 400

 
    df = pd.read_csv(uploaded_file)


    df["Cost"] = pd.to_numeric(df["Cost"])


    total_cost = df["Cost"].sum()


    cost_per_service = df.groupby("Service")["Cost"].sum().to_dict()
    cost_per_day = df.groupby("Date")["Cost"].sum().to_dict()


    daily_items = sorted(cost_per_day.items(), key=lambda x: x[0])
    daily_labels = [d for d, _ in daily_items]
    daily_values = [v for _, v in daily_items]


    service_items = sorted(cost_per_service.items(), key=lambda x: x[1], reverse=True)
    service_labels = [s for s, _ in service_items]
    service_values = [v for _, v in service_items]

    return render_template(
        "results.html",
        total_cost=round(total_cost, 2),
        cost_per_service=cost_per_service,
        cost_per_day=cost_per_day,
        daily_labels=daily_labels,
        daily_values=daily_values,
        service_labels=service_labels,
        service_values=service_values,
        filename=uploaded_file.filename,
    )


if __name__ == "__main__":
    app.run(debug=True)

