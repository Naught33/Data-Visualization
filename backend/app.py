from flask import Flask, request, jsonify
from visualizations import visualize
from flask_cors import CORS
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Flask app and CORS
app = Flask(__name__)
CORS(app)

# Initialize the visualization instance
try:
    logging.info("Initializing visualization instance...")
    vis = visualize()
    logging.info("Visualization instance initialized successfully.")
except Exception as e:
    logging.error(f"Error initializing visualization instance: {e}")
    vis = None

@app.route('/')
def home():
    """Home endpoint to check API health."""
    return jsonify({"message": "Welcome to the Climate Impact and Correlation Analyzer API!"})

@app.route('/show_db', methods=['GET'])
def show_db():
    """Returns the entire dataset."""
    try:
        return vis.show_db()
    except Exception as e:
        logging.error(f"Error in /show_db: {e}")
        return jsonify({"error": "Could not retrieve the dataset"}), 500

@app.route('/show_columns', methods=['GET'])
def show_columns():
    """Returns a list of column names."""
    try:
        return jsonify(vis.show_columns())
    except Exception as e:
        logging.error(f"Error in /show_columns: {e}")
        return jsonify({"error": "Could not retrieve column names"}), 500

@app.route('/count_bar', methods=['POST'])
def count_bar():
    """Returns the count of values in a specified column."""
    try:
        filter = request.json.get('filter')
        if not filter:
            return jsonify({"error": "Filter parameter is required"}), 400
        return vis.count_bar(filter)
    except Exception as e:
        logging.error(f"Error in /count_bar: {e}")
        return jsonify({"error": "Error processing count_bar"}), 500

@app.route('/constrains_bar', methods=['POST'])
def constrains_bar():
    """Filters data based on a constraint and returns counts of another column."""
    try:
        filter1 = request.json.get('filter1')
        constrain = request.json.get('constrain')
        filter2 = request.json.get('filter2')
        if not (filter1 and constrain and filter2):
            return jsonify({"error": "filter1, constrain, and filter2 parameters are required"}), 400
        return vis.constrains_bar(filter1, constrain, filter2)
    except Exception as e:
        logging.error(f"Error in /constrains_bar: {e}")
        return jsonify({"error": "Error processing constrains_bar"}), 500

@app.route('/groupby_histo', methods=['POST'])
def groupby_histo():
    """Groups data by two columns and returns their aggregated counts."""
    try:
        filter1 = request.json.get('filter1')
        filter2 = request.json.get('filter2')
        if not (filter1 and filter2):
            return jsonify({"error": "filter1 and filter2 parameters are required"}), 400
        return vis.groupby_histo(filter1, filter2)
    except Exception as e:
        logging.error(f"Error in /groupby_histo: {e}")
        return jsonify({"error": "Error processing groupby_histo"}), 500

@app.route('/count_line', methods=['POST'])
def count_line():
    """Groups data by a column and returns its counts."""
    try:
        filter = request.json.get('filter')
        if not filter:
            return jsonify({"error": "Filter parameter is required"}), 400
        return vis.count_line(filter)
    except Exception as e:
        logging.error(f"Error in /count_line: {e}")
        return jsonify({"error": "Error processing count_line"}), 500

@app.route('/get_uniq_values', methods=['POST'])
def get_uniq_values():
    """Returns unique values of a specified column."""
    try:
        filter = request.json.get('filter')
        if not filter:
            return jsonify({"error": "Filter parameter is required"}), 400
        return vis.get_uniq_values(filter)
    except Exception as e:
        logging.error(f"Error in /get_uniq_values: {e}")
        return jsonify({"error": "Error processing get_uniq_values"}), 500

if __name__ == '__main__':
    try:
        logging.info("Starting Flask application...")
        app.run(debug=True)
    except Exception as e:
        logging.error(f"Error starting the Flask application: {e}")
