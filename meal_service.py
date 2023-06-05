from flask import Flask, jsonify

app = Flask(__name__)

meals = [
   
  {
    "id":1,
    "meal": "Pizza",
    "restaurant": {
      "name": "Pizza Hut",
      "location": "New York, NY"
    }
  },
  {
    "id":2,
    "meal": "Burger",
    "restaurant": {
      "name": "McDonald's",
      "location": "Los Angeles, CA"
    }
  },
  {
    "id":3,
    "meal": "Tacos",
    "restaurant": {
      "name": "Taco Bell",
      "location": "Chicago, IL"
    }
  }

]


@app.route('/meals', methods=['GET'])
def get_meals():
    return jsonify(meals)

@app.route('/meals/<int:meal_id>', methods=['GET'])
def get_book(meal_id):
    for meal in meals:
        print(meal)
        if meal['id'] == meal_id:
            return jsonify(meal)
    return jsonify({'error': 'Meal not found'}), 404

if __name__ == '__main__':
    app.run(port=5001)
