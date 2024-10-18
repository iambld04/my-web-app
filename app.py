from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the form submission and return JSON response
@app.route('/submit', methods=['POST'])
def submit():
    # Extract the data from the form submission
    user_name = request.form.get('name')
    user_email = request.form.get('email')

    # Prepare the response as a JSON object
    user_details = {
        'name': user_name,
        'email': user_email
    }

    # Return the JSON response
    return jsonify(user_details)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
