#!/usr/bin/python3
"""
Flask app that reads JSON or CSV product data and displays it dynamically.
"""

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def load_json():
    """Load products from JSON file."""
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        return []


def load_csv():
    """Load products from CSV file."""
    try:
        with open("products.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return [
                {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                }
                for row in reader
            ]
    except Exception:
        return []


@app.route("/products")
def products():
    """
    Route to display products from JSON or CSV with optional filtering.
    """

    source = request.args.get("source")
    product_id = request.args.get("id")

    data = []

    if source == "json":
        data = load_json()

    elif source == "csv":
        data = load_csv()

    else:
        return render_template(
            "product_display.html",
            error="Wrong source",
            products=[]
        )

    # Filter by id if provided
    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if int(p["id"]) == product_id]

            if not data:
                return render_template(
                    "product_display.html",
                    error="Product not found",
                    products=[]
                )
        except ValueError:
            return render_template(
                "product_display.html",
                error="Product not found",
                products=[]
            )

    return render_template(
        "product_display.html",
        products=data,
        error=None
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)