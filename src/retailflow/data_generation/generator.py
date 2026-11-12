"""Deterministic, deliberately imperfect source data for the RetailFlow lab."""
from __future__ import annotations
import csv, json, random
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

SEED = 20241120
CATEGORIES = ["Electronics", "Home", "Books", "Fitness", "electronics "]

def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)

def generate_raw_data(output_dir: str | Path, customers: int = 30, orders: int = 90) -> dict[str, int]:
    """Create repeatable CSV/JSON input with visible quality defects for teaching."""
    rng, out = random.Random(SEED), Path(output_dir)
    base = datetime(2024, 1, 1, tzinfo=timezone.utc)
    customer_rows = [{"customer_id": f"C{i:03}", "name": f"Customer {i}", "email": None if i == 7 else f"customer{i}@example.com", "country": rng.choice(["US", "EG", "GB"]), "created_at": (base + timedelta(days=i)).isoformat()} for i in range(1, customers + 1)]
    customer_rows.append(customer_rows[2].copy())  # intentional duplicate
    products = [{"product_id": f"P{i:03}", "product_name": f"Product {i}", "category": CATEGORIES[(i-1) % len(CATEGORIES)], "unit_price": round(8 + i * 3.75, 2)} for i in range(1, 16)]
    products[4]["unit_price"] = "not_a_price"
    order_rows, item_rows, payment_rows = [], [], []
    for i in range(1, orders + 1):
        ts = base + timedelta(days=rng.randrange(100), hours=rng.randrange(24))
        status = rng.choices(["completed", "cancelled", "pending"], weights=[.78, .12, .10])[0]
        oid, cid = f"O{i:04}", f"C{rng.randint(1, customers):03}"
        order_rows.append({"order_id": oid, "customer_id": cid, "order_timestamp": "not-a-timestamp" if i == 4 else ts.isoformat(), "status": status})
        total = 0.0
        for line in range(1, rng.randint(2, 4)):
            # Keep one malformed catalog price for the cleaning lesson, but never use it
            # to manufacture a transaction whose expected revenue is ambiguous.
            product = products[[j for j, p in enumerate(products) if p["unit_price"] != "not_a_price"][rng.randrange(14)]]
            qty = rng.randint(1, 3); price = float(product["unit_price"])
            total += qty * price
            item_rows.append({"order_item_id": f"{oid}-{line}", "order_id": oid, "product_id": product["product_id"], "quantity": qty, "unit_price": price})
        payment_rows.append({"payment_id": f"PAY{i:04}", "order_id": oid, "amount": round(total, 2), "payment_method": rng.choice(["card", "wallet", "cash"]), "paid_at": ts.isoformat()})
    order_rows.append(order_rows[0].copy())
    inventory = [{"product_id": p["product_id"], "snapshot_date": "2024-04-10", "on_hand": rng.randint(0, 120)} for p in products]
    events = [{"event_id": f"E{i:04}", "event_time": (base + timedelta(minutes=i)).isoformat(), "event_type": rng.choice(["page_view", "add_to_cart", "purchase"]), "customer_id": f"C{rng.randint(1, customers):03}", "attributes": {"page": "/products", "campaign": "spring"}} for i in range(1, 151)]
    for name, rows in {"customers":customer_rows, "products":products, "orders":order_rows, "order_items":item_rows, "payments":payment_rows, "inventory":inventory}.items(): _write_csv(out / f"{name}.csv", rows)
    with (out / "website_events.json").open("w", encoding="utf-8") as f:
        for event in events: f.write(json.dumps(event) + "\n")
    (out / "malformed_orders.csv").write_text("order_id,customer_id\nBROKEN,\"unterminated\n", encoding="utf-8")
    return {"customers":len(customer_rows), "products":len(products), "orders":len(order_rows), "order_items":len(item_rows), "events":len(events)}

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(); parser.add_argument("--output", default="data/raw")
    print(generate_raw_data(parser.parse_args().output))
