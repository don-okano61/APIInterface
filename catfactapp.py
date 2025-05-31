import requests
from flask import Flask, jsonify

# Flask API für den Service
app = Flask(__name__)

# Cat Facts API URL
URL = "https://catfact.ninja/fact"

# Funktion zur Extraktion der Katzen-Fakten
def get_cat_fact():
    response = requests.get(URL)
    
    if response.status_code == 200:
        fact = response.json()["fact"]
        return fact
    else:
        return "❌ Fehler beim Abrufen der Katzen-Fakten"

# API-Endpunkt für externe Services
@app.route("/get_cat_fact", methods=["GET"])
def api_get_cat_fact():
    fact = get_cat_fact()
    return jsonify({"cat_fact": fact})

# Flask API starten
if __name__ == "__main__":
    app.run(debug=True, port=5000)