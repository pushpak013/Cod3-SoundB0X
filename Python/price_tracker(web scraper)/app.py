from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime
from tracker import get_price  # Assuming this is defined elsewhere

app = Flask(__name__)

DATA_FILE = 'data/tracked.json'

# Ensure data directory and file exist
os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)  # Start with an empty list


def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Fix corrupted or empty JSON file
        return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)


@app.route('/')
def index():
    data = load_data()
    return render_template('index.html', tracked=data)


@app.route('/', methods=['POST'])
def add():
    url = request.form['url']
    data = load_data()
    new_id = max([item[0] for item in data], default=0) + 1
    print(f"URL submitted: {url}")
    title, price = get_price(url)

    data.append([new_id, url, title, price])
    save_data(data)
    return redirect(url_for('index'))



# DATA_FILE = 'data/tracked.json'

# def load_data():
#     if not os.path.exists(DATA_FILE):
#         return []
#     with open(DATA_FILE, 'r') as f:
#         return json.load(f)

# def save_data(data):
#     with open(DATA_FILE, 'w') as f:
#         json.dump(data, f, indent=2)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/add', methods=['POST'])
# def add_product():
#     url = request.form['url']
#     desired_price = float(request.form['desired_price'])

#     title, current_price = get_price(url)
#     if title and current_price:
#         data = load_data()
#         product = {
#             "url": url,
#             "title": title,
#             "desired_price": desired_price,
#             "price_history": [
#                 {
#                     "date": datetime.now().strftime("%Y-%m-%d"),
#                     "price": current_price
#                 }
#             ]
#         }
#         data.append(product)
#         save_data(data)
#     return redirect(url_for('track'))

# @app.route('/track')
# def track():
#     data = load_data()
#     # Update latest prices
#     for product in data:
#         _, current_price = get_price(product["url"])
#         if current_price:
#             product["price_history"].append({
#                 "date": datetime.now().strftime("%Y-%m-%d"),
#                 "price": current_price
#             })
#     save_data(data)
#     return render_template('track.html', products=data)


if __name__ == '__main__':
    app.run(debug=True)
