from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/about', methods=['GET'])
def about():
    url = 'https://api.github.com/users/Fikayomi31'

    response = requests.get(url)
    # Convert the response to JSON
    data = response.json()  

    # Extract the desired information
    output_data = {
        "gender": "Male", 
        "github_url": data.get("html_url", ""),
        "name": data.get("name", "")
    }

    return jsonify(output_data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
