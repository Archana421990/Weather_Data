from flask import Flask, jsonify
#import fcntl
app = Flask(__name__)
@app.route('/weather', methods=['GET'])
def get_weather():
    return jsonify({"city": "mumbai", "temperature": "-20°C", "weather": "rainy"})
    if __name__ == '__main__':
        app.run(debug=True)
