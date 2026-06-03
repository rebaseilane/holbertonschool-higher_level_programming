#!/usr/bin/python3
"""
Flask app that reads JSON data and renders it using Jinja templates.
"""

from flask import Flask, render_template
import json

app = Flask(__name__)


def load_items():
    """
    Reads items from items.json file.

    Returns:
        list: list of items or empty list if file is invalid
    """
    try:
        with open("items.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data.get("items", [])
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


@app.route("/items")
def items():
    """
    Route that displays items from JSON file.
    """
    items_list = load_items()
    return render_template("items.html", items=items_list)


if __name__ == "__main__":
    app.run(debug=True, port=5000)