#!/usr/bin/python3
"""
Flask app that loads product data from JSON, CSV, or SQLite database.
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


# ---------------- JSON ----------------
def load_json():
    """Load data from JSON file."""
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        return []


# ---------------- CSV ----------------
def load_csv():
    """Load data from CSV file."""
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


# ---------------- SQLITE ----------------
def load_sql():
    """Load data from SQLite database."""
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        conn.close()

        return [
            {
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            }
            for row in rows
        ]

    except Exception:
        return []


@app.route("/products")
def products():
    """
    Main route to display products from json, csv, or sql.
    """

    source = request.args.get("source")
    product_id = request.args.get("id")

    data = []

    # -------- SELECT SOURCE --------
    if source == "json":
        data = load_json()

    elif source == "csv":
        data = load_csv()

    elif source == "sql":
        data = load_sql()

    else:
        return render_template(
            "product_display.html",
            error="Wrong source",
            products=[]
        )

    # -------- FILTER BY ID --------
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