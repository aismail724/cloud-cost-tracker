# Cloud Cost Tracker

A Flask-based web application that analyzes cloud billing CSV files and visualizes spending by service and by day.

## Features
- Upload cloud billing CSV files
- Total cost summary
- Cost breakdown by service and date
- Interactive charts (Chart.js)
- Clean, responsive UI
- Deployed live on Render

## Tech Stack
- Python
- Flask
- Pandas
- Chart.js
- HTML / CSS
- Render (deployment)

## Live Demo
👉 https://YOUR-RENDER-URL.onrender.com

## How It Works
1. Upload a CSV file containing `Date`, `Service`, and `Cost`
2. The backend parses and aggregates the data
3. Results are displayed in a dashboard with tables and charts

## Example CSV Format
```csv
Date,Service,Cost
2026-01-01,EC2,2.50
2026-01-02,S3,0.40
