from flask import Flask, jsonify, request
from models.theater import Theater  # Import the Theater model
from config import session  # Import the existing session object from config.py

app = Flask(__name__)

@app.route('/theaters', methods=['GET'])
# Function to retrieve all theaters
def get_theaters():
    theaters = session.query(Theater).all()
    return jsonify([theater.serialize() for theater in theaters])

@app.route('/theaters/<int:theater_id>', methods=['GET'])
# Function to retrieve a specific theater by ID
def get_theater(theater_id):
    theater = session.query(Theater).filter(Theater.id == theater_id).first()
    if theater:
        return jsonify(theater.serialize())
    else:
        return jsonify(message="Theater not found"), 404

# Function to create a new theater
@app.route('/theaters', methods=['POST'])
def create_theater(theater_data):
    theater_data = request.json
    if theater_data:
        new_theater = Theater(**theater_data)
        session.add(new_theater)
        session.commit()
        return jsonify(new_theater.serialize()), 201
    else:
        return jsonify(message="Invalid theater data"), 400

# Function to update an existing theater
@app.route('/theaters/<int:theater_id>', methods=['PUT'])
def update_theater(theater_id):
    updated_theater_data = request.json
    theater = session.query(Theater).filter(Theater.id == theater_id).first()
    if theater:
        for key, value in updated_theater_data.items():
            setattr(theater, key, value)
        session.commit()
        return jsonify(theater.serialize())
    else:
        return jsonify(message="Theater not found"), 404

# Function to delete an existing theater
@app.route('/theaters/<int:theater_id>', methods=['DELETE'])
def delete_theater(theater_id):
    theater = session.query(Theater).filter(Theater.id == theater_id).first()
    if theater:
        session.delete(theater)
        session.commit()
        return jsonify(message="Theater deleted"), 200
    else:
        return jsonify(message="Theater not found"), 404

if __name__ == '__main__':
    app.run(debug=True)


