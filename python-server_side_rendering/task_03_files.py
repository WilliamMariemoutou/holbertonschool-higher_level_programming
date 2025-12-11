def read_json_file():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except Exception:
        return None


def read_csv_file():
    try:
        products = []
        with open("products.csv", "r") as file:
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
