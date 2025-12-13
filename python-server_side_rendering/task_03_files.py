#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)


def read_json_file():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "products.json")

        with open(file_path, "r") as file:
            return json.load(file)
    except Exception:
        return None


def read_csv_file():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "products.csv")

        products = []
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return products
    except Exception:
        return None


@app.route("/products")
def display_products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ["json", "csv"]:
        return render_template(
            "product_display.html",
            error="Wrong source"
        )

    if source == "json":
        data = read_json_file()
    else:
        data = read_csv_file()

    if data is None:
        return render_template(
            "product_display.html",
            error="Product not found"
        )

    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                "product_display.html",
                error="Product not found"
            )

        data = [p for p in data if p["id"] == product_id]

        if not data:
            return render_template(
                "product_display.html",
                error="Product not found"
            )

    return render_template(
        "product_display.html",
        products=data
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
