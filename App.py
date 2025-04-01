from flask import Flask, request, render_template  # Import necessary Flask modules

app = Flask(__name__)  # Initialize the Flask application

# Knowledge Base: Flower Data
flower_data = {
    "rose": {"color": "red", "petals": "multiple"},
    "sunflower": {"color": "yellow", "petals": "many"},
    "tulip": {"color": "red", "petals": "few"},
    "lily": {"color": "white", "petals": "six"},
    "daisy": {"color": "white", "petals": "many"}
}

# Inference Engine: Identify Flower with Rules
def identify_flower(color, petals):
    """
    This function takes user input (color and petal count) and matches it with predefined rules 
    to identify a flower based on its characteristics.
    """
    rules = [
        ("red", "multiple", "If a flower has red color and multiple petals, THEN it might be a Rose."),
        ("yellow", "many", "If a flower has yellow color and many petals, THEN it might be a Sunflower."),
        ("red", "few", "If a flower has red color and few petals, THEN it might be a Tulip."),
        ("white", "six", "If a flower has white color and six petals, THEN it might be a Lily."),
        ("white", "many", "If a flower has white color and many petals, THEN it might be a Daisy."),
    ]
    
    # Loop through the predefined rules to find a match
    for rule_color, rule_petals, description in rules:
        if rule_color == color.lower() and rule_petals == petals.lower():
            return description  # Return the corresponding flower description if found

    return "No matching flower found based on the provided color and petal count."

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Handles the homepage route. 
    If the user submits the form (POST request), it processes the input and identifies the flower.
    If it's a GET request, it simply renders the form page.
    """
    if request.method == "POST":
        color = request.form.get("color")  # Get the color input from the form
        petals = request.form.get("petals")  # Get the petal count input from the form

        # Debugging: Print received input values to the terminal
        print(f"Received input - Color: {color}, Petals: {petals}")

        flower_description = identify_flower(color, petals)  # Call the identification function

        # Debugging: Print the result to check if the correct flower is being identified
        print(f"Diagnosis: {flower_description}")  

        # Brings the result page with the identified flower description
        return render_template("result.html", flower_description=flower_description)
    
    return render_template("index.html")  # Brings the input form page if it's a GET request

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode for troubleshooting
