from flask import Flask, request, jsonify

app = Flask(__name__)

TYRE_DATABASE = [
    {"vehicle_type": "sedan", "driving_style": "city", "weather": "summer", "budget": "economy", "tyre": "Michelin Energy Saver"},
    {"vehicle_type": "SUV", "driving_style": "off-road", "weather": "all-season", "budget": "premium", "tyre": "Goodyear Wrangler"},
    {"vehicle_type": "sports", "driving_style": "performance", "weather": "summer", "budget": "premium", "tyre": "Pirelli P Zero"}
]

@app.route('/recommend', methods=['POST'])
def recommend_tyre():
    data = request.json
    vehicle_type = data.get("vehicle_type", "").lower()
    driving_style = data.get("driving_style", "").lower()
    weather = data.get("weather", "").lower()
    budget = data.get("budget", "").lower()

    filtered_tyres = [tyre for tyre in TYRE_DATABASE if 
                      tyre["vehicle_type"] == vehicle_type and
                      tyre["driving_style"] == driving_style and
                      tyre["weather"] == weather and
                      tyre["budget"] == budget]

    return jsonify({"recommended_tyre": filtered_tyres[0]["tyre"] if filtered_tyres else "No match found."})

if __name__ == '__main__':
    app.run(debug=True)
