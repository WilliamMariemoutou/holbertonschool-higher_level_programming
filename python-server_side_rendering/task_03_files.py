from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def load_json_data():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except Exception:
        return []


def load_csv_data():
    products = []
    try:
        with open("products.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception:
        pass
    return products


@app.route('/products')
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source == "json":
        data = load_json_data()
    elif source == "csv":
        data = load_csv_data()
    else:
        return render_template("product_display.html", error="Wrong source", products=[])

    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in data if p["id"] == product_id]
            if not filtered:
                return render_template("product_display.html",
                                       error="Product not found", products=[])
            data = filtered
        except ValueError:
            return render_template("product_display.html", error="Invalid ID", products=[])

    return render_template("product_display.html", products=data, error=None)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
