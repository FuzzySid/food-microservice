from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

order_id = 1

# This can be fetched from the database
orders = {}


@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)


@app.route('/orders', methods=['POST'])
def create_order():
    global order_id
    meal_id = request.json['meal_id']
    meal_service_url = f'http://127.0.0.1:5001/meals/{meal_id}'
    meal_response = requests.get(meal_service_url)
    print(meal_response)

    if meal_response.status_code == 200:
        meal = meal_response.json()
        order = {'id': order_id, 'meal': meal}
        orders[order_id] = order
        order_id += 1
        return jsonify(order), 201
    else:
        return jsonify({'error': 'Meal not found'}), 404


if __name__ == '__main__':
    app.run(port=5002)
